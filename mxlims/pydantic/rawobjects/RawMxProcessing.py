# generated by datamodel-codegen:
#   filename:  rawobjects/RawMxProcessing.json

from __future__ import annotations

from typing import Literal, Optional

from pydantic import Field

from ..core.Job import Job
from ..datatypes.SpaceGroupName import SpaceGroupName
from ..datatypes.UnitCell import UnitCell


class RawMxProcessing(Job):
    """
    Crystallography Processing calculation,
    """

    mxlims_type: Literal["MXProcessing"] = Field(
        "MXProcessing",
        alias="mxlimsType",
        description="Type of MXLIMS object.",
        title="Mxlims Type",
    )
    space_group_name: Optional[SpaceGroupName] = Field(
        None,
        alias="spaceGroupName",
        description="Name of space group, to use for processing input. Names may include alternative settings. Matches mmCIF item symmetry.space_group_name_H-M (https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_symmetry.space_group_name_H-M.html).",
        title="Space Group Name",
    )
    unit_cell: Optional[UnitCell] = Field(
        None,
        alias="unitCell",
        description="Unit cell of crystal, to use for processing input.",
    )
