from unittest import TestCase
import converter


class Test(TestCase):
    def test_check(self):
        self.assertEqual(converter.convert(72, "in", "cm"), 183, "Inch to cm fail")
        self.assertEqual(converter.convert(0, "°C", "°F"), 32, "°C to °F fail")
