# generated by datamodel-codegen:
#   filename:  rawobjects/RawWellDrop.json

from __future__ import annotations

from typing import Literal

from pydantic import Field, conint

from ..core.LogisticalSample import LogisticalSample


class RawWellDrop(LogisticalSample):
    """
    A drop in a well in a crystallization plate
    """

    mxlims_type: Literal["WellDrop"] = Field(
        "WellDrop",
        alias="mxlimsType",
        description="The type of MXLIMS object.",
        title="Mxlims Type",
    )
    drop_number: conint(ge=1) = Field(
        ...,
        alias="dropNumber",
        description="The drop number. This should be validated against the plateType's numberSubPositions property.",
    )
