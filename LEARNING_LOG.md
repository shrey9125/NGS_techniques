# Learning log

## 2026-08-27 — repository setup and first tutorial

### What I learned

- An NGS platform is the reading technology; an assay is the biological measurement; a pipeline turns reads into evidence.
- FASTQ stores sequences plus per-base quality scores, while FASTA stores sequences without qualities.
- Depth is the number of observations at a position. Variant allele fraction is alternate support divided by depth.
- Random errors can be separated from stronger variant evidence using depth, support, quality, and context, although real variant callers are much more sophisticated than fixed thresholds.
- A reproducible project records inputs, versions, parameters, outputs, and learning notes.

### Tutorial result

The first run mapped 600 reads at a mean target depth of 187.5× and recovered both planted variants:

- position 80, T>A: 126/265 reads, observed VAF 47.5% (simulated 50%);
- position 165, C>T: 83/278 reads, observed VAF 29.9% (simulated 27%).

The observed VAFs differ from the configured fractions because each read is a random draw and only reads overlapping a site contribute to that site's fraction. This is ordinary sampling variation.

### Questions I still have

- How do production aligners index a genome instead of comparing every position?
- How do probabilistic callers use base quality and mapping quality?
- When should I choose WGS, WES, or a targeted panel?
