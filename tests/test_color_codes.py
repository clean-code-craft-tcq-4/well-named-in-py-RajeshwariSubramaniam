from unittest import TestCase

from cable_color_codes.get_color_codes import (
    get_color_from_pair_number,
    get_pair_number_from_color
)


class TestCablesPair(TestCase):
    def test_number_to_pair(self):
        pair_number = 4
        expected_major_color = 'White'
        expected_minor_color = 'Brown'
        major_color, minor_color = get_color_from_pair_number(pair_number)
        self.assertEqual(major_color, expected_major_color.lower())
        self.assertEqual(minor_color, expected_minor_color.lower())

    def test_pair_to_number(self):
        major_color = 'Black'
        minor_color = 'Orange'
        expected_pair_number = 12
        pair_number = get_pair_number_from_color(major_color, minor_color)
        self.assertEqual(pair_number, expected_pair_number)
