#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$repo_dir"

mkdir -p data/generated results/fastqc
python3 scripts/simulate_reads.py --output-dir data/generated --reads 600 --read-length 75 --error-rate 0.003 --seed 42

if command -v fastqc >/dev/null 2>&1; then
  fastqc --quiet --outdir results/fastqc data/generated/reads.fastq
  echo "FastQC report: results/fastqc/reads_fastqc.html"
else
  echo "FastQC is not installed; continuing with the Python-only tutorial."
fi

python3 scripts/call_variants.py \
  --reference data/generated/reference.fasta \
  --reads data/generated/reads.fastq \
  --output results/variant_calls.tsv \
  --report results/report.md

python3 -m unittest discover -s tests -v
echo "Tutorial complete. Read results/report.md next."
