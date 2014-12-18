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

    def test_empty_tag_has_correct_length(self):
        tag = Tag()
        self.assertEqual(Tag.SIZE, len(tag))

    def test_tag_has_correct_length(self):
        for tag_name in ('foo', 'bar', 'baz', '1'):
            tag = Tag(tag_name)
            self.assertEqual(Tag.SIZE, len(tag))

    def test_tag_with_invalid_length_raises_valueerror(self):
        with self.assertRaises(ValueError):
            tag = Tag('123456789')

    def test_tag_has_correct_data(self):
        tag = Tag('foo')
        self.assertEqual('foo\x00\x00\x00\x00\x00', tag.data)
        tag = Tag('abcdefgh')
        self.assertEqual('abcdefgh', tag.data)

    def test_tag_has_correct_string_representation(self):
        tag = Tag('foo')
        self.assertEqual('foo', str(tag))



class TestPrefix(unittest.TestCase):
    def test_init(self):
        prefix = Prefix()


class TestMessage(unittest.TestCase):
    def test_init(self):
        message = Message()
