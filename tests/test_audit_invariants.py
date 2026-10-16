"""Run: python3 -m unittest discover -s tests -v"""
import pathlib
import sys
import unittest
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
from audit_invariants import compare

class InvariantsTest(unittest.TestCase):
    def test_same_numbers_citations(self):
        self.assertEqual(compare("Accuracy là 87,3% [12].", "Accuracy đạt 87,3% [12]."), [])

    def test_modified_number(self):
        issues = compare("F1 = 0.81 [5]", "F1 = 0.91 [5]")
        self.assertTrue(any(i["category"] == "numbers" for i in issues))

    def test_modified_citation(self):
        issues = compare("Theo [6]", "Theo [7]")
        self.assertTrue(any(i["category"] == "bracket_citations" for i in issues))

    def test_modality_caution(self):
        issues = compare("Mô hình có thể phù hợp.", "Mô hình phù hợp.")
        self.assertTrue(any(i["category"] == "modality_negation_language_cues" for i in issues))

if __name__ == "__main__":
    unittest.main()

class ExtraInvariantsTest(unittest.TestCase):
    def test_latex_citation(self):
        issues = compare(r"Theo \cite{nguyen2023}", r"Theo \cite{tran2024}")
        self.assertTrue(any(i["category"] == "latex_citations" for i in issues))

    def test_doi_preserved(self):
        self.assertFalse(compare("DOI 10.1016/j.patter.2023.100779", "Xem 10.1016/j.patter.2023.100779"))

    def test_removed_negation_caution(self):
        issues = compare("Mô hình không chứng minh điều này.", "Mô hình chứng minh điều này.")
        self.assertTrue(any(i["category"] == "modality_negation_language_cues" for i in issues))
