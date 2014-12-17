# coding=utf-8
# Filename: test_controlhost.py
"""

"""
from __future__ import division, absolute_import, print_function

import unittest

from controlhost import Tag, Message, Prefix


class TestTag(unittest.TestCase):
    def test_init(self):
        tag = Tag()


class TestMessage(unittest.TestCase):
    def test_init(self):
        message = Message()


class TestPrefix(unittest.TestCase):
    def test_init(self):
        prefix = Prefix()
