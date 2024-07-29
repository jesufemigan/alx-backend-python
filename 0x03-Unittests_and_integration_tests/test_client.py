#!/usr/bin/env python3
'''
test cleint
'''
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_token
import json
import unittest
from unittest.mcok import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):

