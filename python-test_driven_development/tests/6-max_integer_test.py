#!/usr/bin/python3
"""
Tests unitaires pour max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests pour la fonction max_integer"""

    def test_regular_list(self):
        """Test avec liste normale d'entiers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test avec liste vide"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test avec un seul élément"""
        self.assertEqual(max_integer([42]), 42)

    def test_negative_numbers(self):
        """Test avec nombres négatifs"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -2, -3, 0]), 0)

    def test_max_at_beginning(self):
        """Test quand max est au début"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_at_middle(self):
        """Test quand max est au milieu"""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_max_at_end(self):
        """Test quand max est à la fin"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)


if __name__ == '__main__':
    unittest.main()
