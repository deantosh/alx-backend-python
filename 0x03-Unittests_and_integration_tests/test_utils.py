#!/usr/bin/env python3
"""
Unit tests for access_nested_map and get_json functions in utils module.
"""
import unittest

from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Defines a test for access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map_execution"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Defines a tests for utils.get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def TestGetJson(self, test_url, test_payload, mock_get):
        """Tests get_json function"""

        # Configure mock to return a response with test_payload as json data
        mock_get.return_value.json.return_value = test_payload

        # Call get_json with url
        result = get_json(test_url)

        # Assert that the result is equal to the test_payload
        self.assertEqual(result, test_payload)

        # Assert that requests.get was called exactly once with the correct URL
        mock_get.assert_called_once_with(test_url)


class TestClass:
    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """Test utils.memoize decorator"""

    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_method):
        """Test memoize decorator to ensure caching works"""

        test_instance = TestClass()

        # Call the property twice and verify results
        result1 = test_instance.a_property
        result2 = test_instance.a_property

        # Assert both calls return the correct value
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)

        # Ensure a_method was only called once due to memoization
        mock_method.assert_called_once()
