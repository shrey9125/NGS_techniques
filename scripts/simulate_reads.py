#!/usr/bin/env python3
"""Create a tiny deterministic reference and synthetic targeted DNA reads."""

import argparse
import json
import random
from pathlib import Path

BASES = "ACGT"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--reads", type=int, default=600)
    parser.add_argument("--read-length", type=int, default=75)
    parser.add_argument("--error-rate", type=float, default=0.003)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    if args.read_length >= 240:
        raise SystemExit("read length must be shorter than the 240 bp reference")

    rng = random.Random(args.seed)
    reference = "".join(rng.choice(BASES) for _ in range(240))
    variants = {80: (next(b for b in BASES if b != reference[79]), 0.50),
                165: (next(b for b in reversed(BASES) if b != reference[164]), 0.27)}

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "reference.fasta").write_text(
        ">synthetic_target\n" + reference + "\n", encoding="utf-8"
    )

    with (args.output_dir / "reads.fastq").open("w", encoding="utf-8") as handle:
        for number in range(1, args.reads + 1):
            start = rng.randint(0, len(reference) - args.read_length)
            read = list(reference[start:start + args.read_length])
            for position, (alternate, fraction) in variants.items():
                offset = position - 1 - start
                if 0 <= offset < args.read_length and rng.random() < fraction:
                    read[offset] = alternate
            for offset, base in enumerate(read):
                if rng.random() < args.error_rate:
                    read[offset] = rng.choice([b for b in BASES if b != base])
            handle.write(f"@synthetic_{number} start={start + 1}\n{''.join(read)}\n+\n{'I' * args.read_length}\n")

    truth = {
        "seed": args.seed,
        "reference_length": len(reference),
        "read_length": args.read_length,
        "read_count": args.reads,
        "error_rate": args.error_rate,
        "variants": [
            {"position": pos, "reference": reference[pos - 1], "alternate": alt, "fraction": fraction}
            for pos, (alt, fraction) in variants.items()
        ],
    }
    (args.output_dir / "truth.json").write_text(json.dumps(truth, indent=2) + "\n", encoding="utf-8")
    print(f"Generated {args.reads} reads and 2 truth variants in {args.output_dir}")


if __name__ == "__main__":
    main()
