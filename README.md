# NGS Techniques: learn by doing

This repository is a practical introduction to next-generation sequencing (NGS). It separates three ideas that are often mixed together:

1. **Platform** — how molecules are read (short-read sequencing, PacBio HiFi, Oxford Nanopore).
2. **Assay** — which biological signal is captured (WGS, RNA-seq, ATAC-seq, 16S, and so on).
3. **Analysis** — how reads become evidence (QC, alignment or assembly, quantification, statistics, interpretation).

Start with [the technique map](docs/technique-map.md), then follow [the learning path](docs/learning-path.md). The map covers the major established technique families; no finite list can include every named protocol or commercial variation.

## First hands-on tutorial

The included tutorial models a small targeted DNA sequencing experiment. It requires only Python 3; FastQC is optional and is used automatically when installed.

```bash
./run_tutorial.sh
```

It will:

- create a reproducible reference sequence and synthetic FASTQ reads;
- introduce two known variants plus realistic sequencing errors;
- optionally run FastQC;
- align the tiny reads with a transparent teaching algorithm;
- calculate coverage and allele fractions;
- write variant calls to `results/variant_calls.tsv` and an explanation to `results/report.md`;
- run automated tests.

Read [Tutorial 1](tutorials/01-targeted-dna-variant-calling.md) before examining the result. This teaching caller is deliberately simple and must not be used for real research or clinical decisions.

## Repository layout

```text
docs/          technique map, glossary, and study plan
tutorials/     guided practical exercises
scripts/       reproducible tutorial code
tests/         automated checks
results/       small, human-readable tutorial outputs
LEARNING_LOG.md notes about what was learned
```

## What to learn next

After Tutorial 1, replace one component at a time with production tools: FastQC/MultiQC for QC, fastp or Cutadapt for trimming, BWA-MEM2 for short DNA reads, minimap2 for long reads, samtools for BAM processing, and a validated caller or workflow for variants. Workflow frameworks such as Nextflow/nf-core or Snakemake make analyses reproducible.

## Reproducibility rules

- Never commit identifiable human sequencing data or credentials.
- Record reference genome build, annotation release, software versions, parameters, and checksums.
- Keep raw data read-only and separate from derived outputs.
- Use synthetic or explicitly public data for tutorials.
- Treat clinical interpretation as a separate, governed process.

## Authoritative starting points

- [Illumina sequencing methods](https://supportassets.illumina.com/techniques/sequencing.html)
- [PacBio sequencing methods](https://www.pacb.com/products-and-services/applications/)
- [How Oxford Nanopore sequencing works](https://nanoporetech.com/platform/technology/)
- [10x Genomics single-cell gene expression](https://www.10xgenomics.com/products/single-cell-gene-expression)
- [nf-core training](https://training.nf-co.re/)
- [Bioconductor RNA-seq workflow](https://bioconductor.org/help/workflows/rnaseqGene/)

## License

Code is released under the MIT License. Educational text is provided for learning and is not medical advice.
