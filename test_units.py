from unittest import TestCase
import units


class Test(TestCase):
    def test_check(self):
        self.assertEqual(units.convert(72, "in", "cm"), 183, "Inch to cm fail")
        self.assertEqual(units.convert(0, "°C", "°F"), 32, "°C to °F fail")
