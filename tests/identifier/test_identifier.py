from src.identifier.identifier import Identifier
import unittest


class TestIdentifier(unittest.TestCase):
    def setUp(self):
        self.id_obj = Identifier()

    def test_invalid_identifier_short_length(self):
        assert self.id_obj.validate_identifier("") == "Inválido"

    def test_invalid_identifier_long_length(self):
        assert self.id_obj.validate_identifier("abc1234") == "Inválido"

    def test_invalid_identifier_contains_special_characters(self):
        assert self.id_obj.validate_identifier("abc1%") == "Inválido"

    def test_invalid_identifier_does_not_start_with_letter(self):
        assert self.id_obj.validate_identifier("1abc") == "Inválido"

    def test_valid_identifier_length_maximum(self):
        assert self.id_obj.validate_identifier("abc123") == "Válido"
