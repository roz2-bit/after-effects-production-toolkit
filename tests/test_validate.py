import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate", ROOT / "scripts" / "validate.py")
VALIDATE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(VALIDATE)


class ValidatorTests(unittest.TestCase):
    def test_required_files_exist(self):
        errors = []
        VALIDATE.check_required(errors)
        self.assertEqual(errors, [])

    def test_links_are_valid(self):
        errors = []
        VALIDATE.check_links(errors)
        self.assertEqual(errors, [])

    def test_json_templates_parse(self):
        errors = []
        VALIDATE.check_json(errors)
        self.assertEqual(errors, [])

    def test_examples_are_explicit(self):
        errors = []
        VALIDATE.check_placeholders(errors)
        self.assertEqual(errors, [])


if __name__ == "__main__":
    unittest.main()

