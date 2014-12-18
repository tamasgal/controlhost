# coding=utf-8
# Filename: __init__.py
"""
A set of classes and tools wich uses the ControlHost protocol.

"""
from __future__ import absolute_import

from controlhost.__version__ import version

__author__ = "Tamas Gal"
__copyright__ = ("Copyright 2014, Tamas Gal and the KM3NeT collaboration "
                 "(http://km3net.org)")
__credits__ = []
__license__ = "MIT"
__version__ = version
__maintainer__ = "Tamas Gal"
__email__ = "tgal@km3net.de"
__status__ = "Development"


class Tag(object):
    """Represents the tag in a ControlHost Prefix."""
    SIZE = 8

    def __init__(self, data=None):
        self._data = b''
        self.data = data

    @property
    def data(self):
        """The byte data"""
        return self._data

    @data.setter
    def data(self, value):
        """Set the byte data and fill up the bytes to fit the size."""
        if not value:
            value = b''
        if len(value) > self.SIZE:
            raise ValueError("The maximum tag size is {0}".format(self.SIZE))
        self._data = value
        while len(self._data) < self.SIZE:
            self._data += b'\x00'

    def __str__(self):
        return str(self.data).strip('\x00')

    def __len__(self):
        return len(self._data)


class Prefix(object):
    """The prefix of a ControlHost message."""
    pass


class Message(object):
    """The representation of a ControlHost message."""
    pass
