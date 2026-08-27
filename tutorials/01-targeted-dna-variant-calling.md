# Tutorial 1: targeted DNA variant calling

## Goal

Understand how FASTQ reads become a small variant table. The data are synthetic, so the true variants are known and no download or private data is needed.

## Before running

Predict what should happen when:

- a variant is present in roughly half the molecules;
- a variant is present in roughly one quarter of molecules;
- random sequencing errors appear at much lower fractions;
- depth is too low to support a confident conclusion.

## Run

From the repository root:

```bash
./run_tutorial.sh
```

The simulation uses a fixed random seed, so results are reproducible. Read `results/report.md` and `results/variant_calls.tsv` afterward. If FastQC is installed, open the HTML file under `results/fastqc/`.

## Follow the data

1. `data/generated/reference.fasta` contains the reference.
2. `data/generated/reads.fastq` contains reads and Phred quality strings.
3. The teaching aligner compares each read with every possible reference window and chooses the window with the fewest mismatches.
4. A pileup counts A/C/G/T observations at every position.
5. A site is reported when depth is at least 20, alternate support is at least 5 reads, and alternate fraction is at least 0.20.

These rules illustrate thresholds; real callers use probabilistic models, mapping and base qualities, strand/context evidence, duplicate handling, local assembly, calibration, and carefully validated filters.

## Questions to answer in your learning log

1. Which two positions were called, and what were their observed VAFs?
2. Why are random sequencing errors not normally called here?
3. How could PCR duplicates make the reported VAF misleading?
4. Why can a repetitive reference cause the teaching aligner to fail?
5. Which extra controls and metadata would a real experiment require?

## Safe extensions

- Change `--reads` or `--error-rate` in `run_tutorial.sh` and compare results.
- Raise the minimum alternate fraction in `scripts/call_variants.py`.
- Add a third low-frequency variant and measure whether it is detected.
- Plot coverage using a language/library of your choice.

Never use this script for patient, diagnostic, or publication-grade analysis.
