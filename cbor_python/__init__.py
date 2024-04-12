#!/usr/bin/env python3

from typing import List
from .initial_byte_table import *
from .major_type_table import *
from .tag_table import *

def loads(data: int|bytearray):
    """Deserialize a CBOR data item with the generic data model in RFC 8949.
    """

    raise NotImplementedError("I cannot deserialize yet!")

def dumps():
    """Print out a representation of CBOB instance data.
    """
    raise NotImplementedError("I cannot print yet!")
