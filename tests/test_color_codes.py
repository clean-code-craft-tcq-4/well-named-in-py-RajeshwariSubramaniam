from unittest import TestCase

from cable_color_codes.get_color_codes import (
    get_color_from_pair_number,
    get_pair_number_from_color
)


class TestCablesPair(TestCase):
    def test_get_color_from_pair_number(self):
        pair_number = 4
        expected_major_color = 'White'
        expected_minor_color = 'Brown'
        major_color, minor_color = get_color_from_pair_number(pair_number)
        self.assertEqual(expected_major_color.lower(), major_color)
        self.assertEqual(expected_minor_color.lower(), minor_color)

    def test_get_pair_number_from_color(self):
        major_color = 'Black'
        minor_color = 'Orange'
        expected_pair_number = 12
        pair_number = get_pair_number_from_color(major_color, minor_color)
        self.assertEqual(expected_pair_number, pair_number)
