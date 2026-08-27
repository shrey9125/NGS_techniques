# Map of major NGS techniques

## How to choose

Begin with the biological question, not the sequencer:

- **What exists in the genome?** Use WGS, WES, a targeted panel, or amplicon sequencing.
- **What is expressed?** Use bulk, single-cell, spatial, small-RNA, or long-read RNA sequencing.
- **How is DNA regulated?** Use ATAC-seq, ChIP-seq, CUT&RUN/CUT&Tag, methylation sequencing, or chromosome-conformation assays.
- **Which organisms are present?** Use marker-gene amplicons, shotgun metagenomics, metatranscriptomics, or isolate WGS.
- **Do repeats, haplotypes, isoforms, or structural variants matter?** Strongly consider long reads.

Technique names describe library preparation and biological signal. The same assay can sometimes be read on different platforms.

## DNA sequence and variation

| Technique | Measures | Best for | Main limitation | Typical analysis |
|---|---|---|---|---|
| Whole-genome sequencing (WGS) | Nearly all genomic DNA | SNVs, indels, CNVs, SVs, discovery | Cost and interpretation burden | QC → align/assemble → call → annotate |
| Whole-exome sequencing (WES) | Protein-coding exons captured by probes | Coding variants at lower cost than WGS | Misses noncoding regions; uneven capture | QC → align → call in targets → annotate |
| Targeted hybrid-capture panel | Selected genes/regions | Deep, focused testing | Cannot discover outside panel | QC → align → call → target coverage QC |
| Amplicon sequencing | PCR-selected loci | Very deep small targets; microbial markers | Primer bias and allele dropout | Demultiplex → trim primers → align/denoise |
| Low-pass WGS | Sparse genome-wide signal | CNVs, ancestry, imputation | Weak direct rare-variant sensitivity | Align → bin/normalize or impute |
| Cell-free DNA sequencing | Short circulating DNA fragments | Liquid-biopsy research, prenatal research | Low signal; pre-analytical sensitivity | UMI consensus → error suppression → call |
| Ancient/degraded DNA sequencing | Damaged, short DNA | Archaeogenomics and degraded samples | Contamination and damage | Authenticate damage → map → genotype |
| De novo genome sequencing | Reads without relying on a finished reference | New organisms and assemblies | Assembly/QC complexity | QC → assemble → polish → assess → annotate |

## RNA and translation

| Technique | Measures | Best for | Main limitation | Typical analysis |
|---|---|---|---|---|
| Bulk mRNA-seq | Polyadenylated transcript abundance | Differential gene expression | Averages across cells | QC → splice-aware align/pseudoalign → count → statistics |
| Total RNA-seq | Coding and many noncoding RNAs after depletion | Broad transcriptome, degraded samples | rRNA depletion quality matters | QC → align → quantify → statistics |
| 3′/5′ tag RNA-seq | One end-tag per transcript | Cost-efficient expression counting | Limited isoform information | UMI handling → map → count |
| Small RNA-seq | miRNA and other short RNAs | Small-RNA discovery/quantification | Adapter dimers and specialized mapping | Trim → size-select → map → quantify |
| Long-read RNA-seq / Iso-Seq | Full-length transcript molecules | Isoforms, fusions, allele-specific transcripts | Lower throughput or higher per-base cost | Map → collapse isoforms → quantify |
| Direct RNA nanopore sequencing | Native RNA signal | Isoforms and RNA modifications research | RNA input and error-model challenges | Basecall → map → isoform/modification analysis |
| Ribo-seq | Ribosome-protected fragments | Translation and reading frames | Exacting wet-lab protocol | Trim → remove rRNA → map → P-site analysis |
| PRO-seq/GRO-seq | Nascent transcription | Polymerase activity | Specialized library preparation | Map → strand-aware transcription analysis |
| CLIP-seq family | RNA bound by a chosen protein | RNA–protein interactions | Crosslink and antibody biases | Deduplicate → map → peak/site calling |

## Epigenome and genome regulation

| Technique | Signal | Key question | Important caveat |
|---|---|---|---|
| ChIP-seq | Antibody-enriched protein-bound DNA | Where is a transcription factor or histone mark? | Antibody quality and controls are critical |
| CUT&RUN / CUT&Tag | Targeted cleavage/tagmentation near chromatin proteins | Similar questions with lower input/background | Protocol-specific controls still matter |
| ATAC-seq | Accessible chromatin | Which regulatory regions are open? | Mitochondrial reads and cell quality can dominate |
| DNase-seq / MNase-seq | Nuclease accessibility or nucleosome protection | Chromatin organization | Digestion conditions affect signal |
| WGBS | Bisulfite-converted DNA | Genome-wide cytosine methylation | DNA damage, reduced sequence complexity, cannot inherently separate 5mC/5hmC |
| RRBS | Restriction-enriched bisulfite DNA | CpG-rich methylation at lower cost | Nonuniform, restricted genomic coverage |
| Enzymatic methyl-seq | Enzymatic conversion signal | Methylation with less DNA damage | Assay-specific conversion QC required |
| Native long-read methylation | Kinetic/electrical signal alongside sequence | Phased methylation over long molecules | Platform/model-specific calibration |
| Hi-C and related 3C assays | Pairwise physical DNA contacts | 3D genome and scaffolding | Resolution depends strongly on depth |

## Microbes and communities

| Technique | Answers | Resolution | Main bias |
|---|---|---|---|
| 16S/18S/ITS amplicon | Who is present? | Usually genus-level; sometimes species-level | Primer choice, copy number, contamination |
| Shotgun metagenomics | Who is present and what genes exist? | Species/strain and functional potential | Host DNA and database bias |
| Metatranscriptomics | Which community genes are expressed? | Community activity | RNA instability and compositionality |
| Isolate WGS | What genome does a cultured isolate have? | Strain/genome | Requires culture; mixed samples complicate assembly |
| Viral sequencing | Which viral genomes/variants are present? | Depends on enrichment and depth | Low input and contamination |

## Single-cell, spatial, and multi-omic assays

| Technique | Unit measured | Typical use | Main challenge |
|---|---|---|---|
| scRNA-seq | Individual cells | Cell types, states, trajectories | Dropouts, doublets, batch effects |
| snRNA-seq | Individual nuclei | Frozen/difficult tissues | Nuclear RNA differs from whole-cell RNA |
| scATAC-seq | Chromatin accessibility per cell | Regulatory cell states | Sparse count matrix |
| Single-cell DNA-seq | Genome per cell | Mosaicism, tumor evolution, CNVs | Amplification bias and allelic dropout |
| CITE-seq | RNA plus antibody-derived protein tags | Joint transcript/protein phenotyping | Antibody panel and background correction |
| Multiome RNA+ATAC | Expression and accessibility in the same cell | Link regulatory state to expression | Cost, sparsity, integration |
| Spatial transcriptomics | RNA with tissue coordinates | Tissue architecture | Resolution, capture efficiency, segmentation |
| Immune repertoire sequencing | BCR/TCR rearrangements | Clonotypes and immune response | PCR bias and correct chain pairing |

## Platform families

| Platform family | Core strength | Trade-off | Common fits |
|---|---|---|---|
| Illumina short reads | High accuracy and throughput | Short molecules obscure long repeats and phasing | WGS, WES, panels, bulk/scRNA-seq, epigenomics |
| PacBio HiFi | Long, highly accurate consensus reads | Input/cost/throughput must match project | Assembly, SVs, phasing, full-length isoforms, methylation |
| Oxford Nanopore | Real-time, native DNA/RNA, very long reads, flexible scale | Accuracy and output depend on chemistry/basecalling/workflow | Rapid sequencing, assembly, SVs, direct RNA, native modifications |

## Universal analysis concepts

Every project needs experimental design, biological replicates, negative/positive controls, metadata, sample QC, library QC, sequencing QC, an explicit reference/database version, contamination checks, and a statistical plan. Read depth cannot repair confounding or poor biological replication.

For production analyses, prefer community-reviewed workflows and validate the exact pipeline for the intended use. The tutorial in this repository explains concepts; it is not a clinical pipeline.
