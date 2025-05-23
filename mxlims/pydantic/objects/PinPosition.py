# generated by datamodel-codegen:
#   filename:  objects/PinPosition.json

from __future__ import annotations

from typing import List, Optional, Union

from pydantic import Field

from ..rawobjects.RawPinPosition import RawPinPosition
from .Crystal import Crystal
from .MxExperiment import MxExperiment
from .MxProcessing import MxProcessing


class PinPosition(RawPinPosition):
    """
    An independent Position within a Pin where crystals can be located, with typed JSON containment lists.
    """

    contents: Optional[List[Crystal]] = Field(None, min_length=1)
    jobs: Optional[List[Union[MxExperiment, MxProcessing]]] = None
