# generated by datamodel-codegen:
#   filename:  objects/Dewar.json

from __future__ import annotations

from typing import List, Optional

from pydantic import Field

from ..rawobjects.RawDewar import RawDewar
from .Puck import Puck


class Dewar(RawDewar):
    """
    A dewar containing pucks with mounted crystals on pins, with typed JSON containment lists.
    """

    contents: Optional[List[Puck]] = Field(None, min_length=1)
