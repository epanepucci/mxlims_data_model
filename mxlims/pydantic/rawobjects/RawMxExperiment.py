# generated by datamodel-codegen:
#   filename:  rawobjects/RawMxExperiment.json

from __future__ import annotations

from typing import Literal, Optional

from pydantic import Field, confloat, conint

from ..core.Job import Job
from ..datatypes.SpaceGroupName import SpaceGroupName
from ..datatypes.UnitCell import UnitCell


class RawMxExperiment(Job):
    """
    Crystallography experiment, producing data
    """

    mxlims_type: Literal["MxExperiment"] = Field(
        "MxExperiment",
        alias="mxlimsType",
        description="The type of MXLIMS object.",
        title="Mxlims Type",
    )
    experiment_strategy: Optional[str] = Field(
        None,
        alias="experimentStrategy",
        description="Experiment strategy indicator",
        examples=[
            "OSC",
            "Helical",
            "MXPressE",
            "GPhL.native.basic",
            "GPhL.SAD.advanced",
            "GPhL.2wvlMAD.basic",
        ],
        title="Experiment Strategy",
    )
    expected_resolution: Optional[confloat(ge=0.0)] = Field(
        None,
        alias="expectedResolution",
        description="The resolution expected in the experiment - for positioning the detector and setting up the experiment",
        title="Expected Resolution",
    )
    target_completeness: Optional[confloat(ge=0.0, le=100.0)] = Field(
        None,
        alias="targetCompleteness",
        description="Minimal completeness expected from experiment",
        title="Target Completeness",
    )
    target_multiplicity: Optional[confloat(ge=0.0)] = Field(
        None,
        alias="targetMultiplicity",
        description="Minimal multiplicity expected from experiment",
        title="Target Multiplicity",
    )
    dose_budget: Optional[confloat(ge=0.0)] = Field(
        None,
        alias="doseBudget",
        description="Dose (MGy) to be used in experiment",
        title="Dose Budget",
    )
    snapshot_count: Optional[conint(ge=0)] = Field(
        0,
        alias="snapshotCount",
        description="Number of snapshots to acquire after each (re)centring",
        title="Snapshot Count",
    )
    wedge_width: Optional[confloat(ge=0.0)] = Field(
        None,
        alias="wedgeWidth",
        description="Wedge width (in degrees) to use for interleaving",
        title="Wedge Width",
    )
    measured_flux: Optional[confloat(ge=0.0)] = Field(
        None,
        alias="measuredFlux",
        description="Measured value of beam flux in photons/s",
        title="Measured Flux",
    )
    radiation_dose: Optional[confloat(ge=0.0)] = Field(
        None,
        alias="radiationDose",
        description="Total radiation dose absorbed during experiment",
        title="Radiation Dose",
    )
    space_group_name: Optional[SpaceGroupName] = Field(
        None,
        alias="spaceGroupName",
        description="Name of space group, as determined during characterisation. Names may include alternative settings. Matches mmCIF item symmetry.space_group_name_H-M (https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_symmetry.space_group_name_H-M.html).",
        title="Space Group Name",
    )
    unit_cell: Optional[UnitCell] = Field(
        None,
        alias="unitCell",
        description="Unit cell of crystal, as determined during characterisation.",
    )
