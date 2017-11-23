from django.http import QueryDict
from django.test import tag
from tests.BaseTestWithDB import BaseTestWithDB
from resources.generators.BinaryWindowsResourceGenerator import BinaryWindowsResourceGenerator


@tag("resource")
class BinaryWindowsResourceGeneratorTest(BaseTestWithDB):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = "en"

    def test_subtitle_4_binary_dots_a4(self):
        query = QueryDict("number_bits=4&value_type=binary&dot_counts=yes&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - binary - with dot counts - a4"
        )

    def test_subtitle_4_binary_dots_letter(self):
        query = QueryDict("number_bits=4&value_type=binary&dot_counts=yes&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - binary - with dot counts - letter"
        )

    def test_subtitle_4_lightbulb_dots_a4(self):
        query = QueryDict("number_bits=4&value_type=lightbulb&dot_counts=yes&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - lightbulb - with dot counts - a4"
        )

    def test_subtitle_4_lightbulb_dots_letter(self):
        query = QueryDict("number_bits=4&value_type=lightbulb&dot_counts=yes&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - lightbulb - with dot counts - letter"
        )

    def test_subtitle_4_binary_no_dots_a4(self):
        query = QueryDict("number_bits=4&value_type=binary&dot_counts=no&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - binary - without dot counts - a4"
        )

    def test_subtitle_4_binary_no_dots_letter(self):
        query = QueryDict("number_bits=4&value_type=binary&dot_counts=no&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - binary - without dot counts - letter"
        )

    def test_subtitle_4_lightbulb_no_dots_a4(self):
        query = QueryDict("number_bits=4&value_type=lightbulb&dot_counts=no&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - lightbulb - without dot counts - a4"
        )

    def test_subtitle_4_lightbulb_no_dots_letter(self):
        query = QueryDict("number_bits=4&value_type=lightbulb&dot_counts=no&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "4 bits - lightbulb - without dot counts - letter"
        )

    def test_subtitle_8_binary_dots_a4(self):
        query = QueryDict("number_bits=8&value_type=binary&dot_counts=yes&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - binary - with dot counts - a4"
        )

    def test_subtitle_8_binary_dots_letter(self):
        query = QueryDict("number_bits=8&value_type=binary&dot_counts=yes&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - binary - with dot counts - letter"
        )

    def test_subtitle_8_lightbulb_dots_a4(self):
        query = QueryDict("number_bits=8&value_type=lightbulb&dot_counts=yes&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - lightbulb - with dot counts - a4"
        )

    def test_subtitle_8_lightbulb_dots_letter(self):
        query = QueryDict("number_bits=8&value_type=lightbulb&dot_counts=yes&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - lightbulb - with dot counts - letter"
        )

    def test_subtitle_8_binary_no_dots_a4(self):
        query = QueryDict("number_bits=8&value_type=binary&dot_counts=no&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - binary - without dot counts - a4"
        )

    def test_subtitle_8_binary_no_dots_letter(self):
        query = QueryDict("number_bits=8&value_type=binary&dot_counts=no&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - binary - without dot counts - letter"
        )

    def test_subtitle_8_lightbulb_no_dots_a4(self):
        query = QueryDict("number_bits=8&value_type=lightbulb&dot_counts=no&paper_size=a4")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - lightbulb - without dot counts - a4"
        )

    def test_subtitle_8_lightbulb_no_dots_letter(self):
        query = QueryDict("number_bits=8&value_type=lightbulb&dot_counts=no&paper_size=letter")
        generator = BinaryWindowsResourceGenerator(query)
        self.assertEqual(
            generator.subtitle,
            "8 bits - lightbulb - without dot counts - letter"
        )
