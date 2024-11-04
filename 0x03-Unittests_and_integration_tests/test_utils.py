#!/usr/bin/env python3
"""
Unit tests for access_nested_map and get_json functions in utils module.
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import access_nested_map, get_json


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
