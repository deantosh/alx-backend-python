#!/usr/bin/env python3
"""
In a new test_client.py file, declare the TestGithubOrgClient
(unittest.TestCase)class and implement the test_org method.
This method should test that GithubOrgClient.org returns the correct value.
Use @patch as a decorator to make sure get_json is called once with the
expected
argument but make sure it is not executed.
Use @parameterized.expand as a decorator to parametrize the test with a couple
of org examples to pass to GithubOrgClient, in this order:
  - google
  - abc
Of course, no external HTTP calls should be made.
"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test client.GithubOrgClient class"""
    @parameterized.expand([
        ("google", {"name": "google", "description": "A technology company."}),
        ("abc", {"name": "abc", "description": "An example organization."}),
    ])
    @patch('requests.get')
    def test_org(self, org_name, org_result, mock_get):
        """Test GithubOrgClient.org returns the correct value"""

        # Configure the mock return value as JSON
        mock_get.return_value.JSON.return_value = org_result

        org_instance = GithubOrgClient(org_name)

        # Call the org property
        response = org_instance.org

        self.assertEqual(response["name"], org_name)
        self.assertEqual(response["description"], org_result["description"])

        # verify thet requests.get was called once with expected url
        mock_get.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the expected value."""
        with patch('client.GithubOrgClient.org',
                   new_property=property(lambda self: {
                       "repos_url": "https://api.github.com/orgs/google/repos"
                   })):

            org_instance = GithubOrgClient("google")

            # Call the _public_repos_url method
            url = org_instance._public_repos_url()

            self.assertEqual(url, "https://api.github.com/orgs/google/repos")
