#!/usr/bin/env python3
"""
Familiarize yourself with the utils.access_nested_map function and understand
its purpose. Play with it in the Python console to make sure you understand.
 - In this task you will write the first unit test for utils.access_nested_map.
 - Create a TestAccessNestedMap class that inherits from unittest.TestCase.
 - Implement the TestAccessNestedMap.test_access_nested_map method to test that
   the method returns what it is supposed to.
 - Decorate the method with @parameterized.expand to test the function for
   following inputs:
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


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


"""
Familiarize yourself with the utils.get_json function.
Define the TestGetJson(unittest.TestCase) class and implement the
TestGetJson.test_get_json method to test that utils.get_json returns the
expected result.
We don’t want to make any actual external HTTP calls. Use unittest.mock.patch
to patch requests.get. Make sure it returns a Mock object with a json method
that returns test_payload which you parametrize alongside the test_url that
you will
pass to get_json with the following inputs:
"""


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
