import csv
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TutorialTest(unittest.TestCase):
    def test_expected_variants_are_recovered(self):
        with tempfile.TemporaryDirectory() as temporary:
            work = Path(temporary)
            subprocess.run([
                "python3", str(ROOT / "scripts/simulate_reads.py"),
                "--output-dir", str(work / "data")
            ], check=True)
            subprocess.run([
                "python3", str(ROOT / "scripts/call_variants.py"),
                "--reference", str(work / "data/reference.fasta"),
                "--reads", str(work / "data/reads.fastq"),
                "--output", str(work / "calls.tsv"),
                "--report", str(work / "report.md")
            ], check=True)
            with (work / "calls.tsv").open() as handle:
                calls = list(csv.DictReader(handle, delimiter="\t"))
            self.assertEqual([int(row["position"]) for row in calls], [80, 165])
            self.assertTrue((work / "report.md").read_text().startswith("# Tutorial result"))


if __name__ == "__main__":
    unittest.main()
