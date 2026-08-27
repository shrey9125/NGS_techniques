#!/usr/bin/env python3
"""Transparent toy aligner and pileup caller for the synthetic tutorial only."""

import argparse
from collections import Counter
from pathlib import Path


def read_fasta(path: Path) -> str:
    return "".join(line.strip() for line in path.read_text(encoding="utf-8").splitlines() if not line.startswith(">"))


def read_fastq(path: Path):
    with path.open(encoding="utf-8") as handle:
        while True:
            name = handle.readline().rstrip()
            if not name:
                return
            sequence = handle.readline().rstrip()
            plus = handle.readline().rstrip()
            qualities = handle.readline().rstrip()
            if not name.startswith("@") or plus != "+" or len(sequence) != len(qualities):
                raise ValueError(f"Malformed FASTQ record near {name!r}")
            yield sequence


def best_start(reference: str, read: str) -> tuple[int, int]:
    candidates = []
    for start in range(len(reference) - len(read) + 1):
        mismatches = sum(a != b for a, b in zip(read, reference[start:start + len(read)]))
        candidates.append((mismatches, start))
    return min(candidates)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", type=Path, required=True)
    parser.add_argument("--reads", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--min-depth", type=int, default=20)
    parser.add_argument("--min-alt-count", type=int, default=5)
    parser.add_argument("--min-alt-fraction", type=float, default=0.20)
    args = parser.parse_args()

    reference = read_fasta(args.reference)
    pileup = [Counter() for _ in reference]
    mapped = 0
    total_mismatches = 0
    for read in read_fastq(args.reads):
        mismatches, start = best_start(reference, read)
        mapped += 1
        total_mismatches += mismatches
        for offset, base in enumerate(read):
            pileup[start + offset][base] += 1

    calls = []
    for index, counts in enumerate(pileup):
        ref = reference[index]
        depth = sum(counts.values())
        alternatives = [(count, base) for base, count in counts.items() if base != ref]
        if not alternatives or depth < args.min_depth:
            continue
        alt_count, alt = max(alternatives)
        fraction = alt_count / depth
        if alt_count >= args.min_alt_count and fraction >= args.min_alt_fraction:
            calls.append((index + 1, ref, alt, depth, alt_count, fraction))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        handle.write("position\treference\talternate\tdepth\talt_count\talt_fraction\n")
        for pos, ref, alt, depth, alt_count, fraction in calls:
            handle.write(f"{pos}\t{ref}\t{alt}\t{depth}\t{alt_count}\t{fraction:.3f}\n")

    mean_depth = sum(sum(c.values()) for c in pileup) / len(pileup)
    call_lines = "\n".join(
        f"- Position {pos}: {ref}>{alt}, depth {depth}, {alt_count} alternate reads, VAF {fraction:.1%}"
        for pos, ref, alt, depth, alt_count, fraction in calls
    ) or "- No variants passed the tutorial thresholds."
    args.report.write_text(
        "# Tutorial result\n\n"
        f"- Reads mapped: {mapped}\n"
        f"- Mean target depth: {mean_depth:.1f}×\n"
        f"- Mean mismatches per read: {total_mismatches / mapped:.2f}\n"
        f"- Variants passing thresholds: {len(calls)}\n\n"
        "## Calls\n\n" + call_lines + "\n\n"
        "The variant allele fraction is alternate-supporting reads divided by total depth at the site. "
        "Small discrepancies from the simulated fraction are normal sampling variation. Random errors are usually "
        "too rare to cross the thresholds. This simplified result is educational, not research- or clinical-grade.\n",
        encoding="utf-8",
    )
    print(f"Mapped {mapped} reads; wrote {len(calls)} calls to {args.output}")


if __name__ == "__main__":
    main()
