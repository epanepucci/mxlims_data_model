#! /usr/bin/env python
# encoding: utf-8
#
"""

License:

This file is part of the MXLIMS collaboration.

MXLIMS models and code are free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

MXLIMS is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with MXLIMS. If not, see <https://www.gnu.org/licenses/>.
"""

__copyright__ = """ Copyright © 2024 -  2024 MXLIMS collaboration."""
__author__ = "rhfogh"
__date__ = "18/10/2024"


import enum
from typing import Optional, Dict, List, Tuple, Union, Literal

from pydantic import BaseModel, Field

from mxlims.pydantic import core


class PdbxSignalType(str, enum.Enum):
    """Observability criterion. Matches mmCIF item reflns.pdbx_signal_type

    https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_signal_type.html)
    """

    I_over_sigma = "local <I/sigmaI>"
    wCC_half = "local wCC_half"


class QualityFactorType(str, enum.Enum):
    """Name for quality factor type, used in QualityFactor class"""

    R_merge = "R(merge)"
    R_meas = "R(meas)"
    R_pim = "R(pim)"
    I_over_SigI = "I/SigI"
    CC_half = "CC(1/2)"
    CC_ano = "CC(ano)"
    SigAno = "SigAno"
    Completeness = "Completeness"
    CompletenessSpherical = "CompletenessSpherical"
    CompletenessEllipsoidal = "CompletenessEllipsoidal"
    Redundancy = "Redundancy"
    CompletenessAno = "CompletenessAno"
    CompletenessAnoSpherical = "CompletenessAnoSpherical"
    CompletenessAnoEllipsoidal = "CompletenessAnoEllipsoidal"
    RedundancyAno = "RedundancyAno"


class ReflectionBinningMode(str, enum.Enum):
    """Reflection binning mode for binning reflection statistics"""

    equal_volume = "equal_volume"
    equal_number = "equal_number"
    dstar_equidistant = "dstar_equidistant"
    dstar2_equidistant = "dstar2_equidistant"


class FileType(str, enum.Enum):
    """Name for file type, used in ReflectionSet class"""

    MTZ_scaled_merged = "scaled and merged MTZ"
    MTZ_scaled_unmerged = "scaled and unmerged MTZ"
    MTZ_unmerged = "unmerged MTZ"
    XDS_INTEGRATE = (
        "XDS INTEGRATE.HKL; unmerged "
        "(https://xds.mr.mpg.de/html_doc/xds_files.html#INTEGRATE.HKL)"
    )
    XDS_ASCII = (
        "XDS XDS_ASCII.HKL; scaled and unmerged "
        "(https://xds.mr.mpg.de/html_doc/xds_files.html#XDS_ASCII.HKL)"
    )


class UnitCell(BaseModel):
    """Crystallographic unit cell,

    matches mmCIF items cell.length_{a,b,c} and cell.angle_{alpha,beta,gamma} in category
    cell (https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Categories/cell.html)
    """

    a: float = Field(frozen=True, ge=0, description="A axis length (A)")
    b: float = Field(frozen=True, ge=0, description="B axis length (A)")
    c: float = Field(frozen=True, ge=0, description="C axis length (A)")
    alpha: float = Field(frozen=True, ge=0, description="alpha angle (degree)")
    beta: float = Field(frozen=True, ge=0, description="beta angle (degree)")
    gamma: float = Field(frozen=True, ge=0, description="gamma angle (degree)")


class Tensor(BaseModel):
    """Tensor"""

    eigenvalues: Tuple[float, float, float] = Field(description="Eigenvalues of tensor")
    eigenvectors: List[Tuple[float, float, float]] = Field(
        description="Eigenvectors (unit vectors) of tensor, "
        "in same order as eigenvalues"
    )


class QualityFactor(BaseModel):
    """Reflection shell quality factor. Enumerated type with associated value

    Correspondence with mmCIF items:

      Overall (mmCIF reflns category, https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Categories/reflns.html)

        R(merge)                      reflns.pdbx_Rmerge_I_obs                                 https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_Rmerge_I_obs.html
        R(meas)                       reflns.pdbx_Rrim_I_all                                   https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_Rrim_I_all.html
        R(pim)                        reflns.pdbx_Rpim_I_all                                   https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_Rpim_I_all.html
        I/SigI                        reflns.pdbx_netI_over_sigmaI                             https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_netI_over_sigmaI.html
        CC(1/2)                       reflns.pdbx_CC_half                                      https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_CC_half.html
        CC(ano)                       reflns.pdbx_CC_half_anomalous                            https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_CC_half_anomalous.html
        SigAno                        reflns.pdbx_absDiff_over_sigma_anomalous                 https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_absDiff_over_sigma_anomalous.html
        Completeness                  reflns.percent_possible_obs                              https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.percent_possible_obs.html
        CompletenessSpherical         reflns.pdbx_percent_possible_spherical_anomalous         https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_percent_possible_spherical_anomalous.html
        CompletenessEllipsoidal       reflns.pdbx_percent_possible_ellipsoidal_anomalous       https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_percent_possible_ellipsoidal_anomalous.html
        Redundancy                    reflns.pdbx_redundancy                                   https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_redundancy.html
        CompletenessAno               reflns.pdbx_percent_possible_anomalous                   https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_percent_possible_anomalous.html
        CompletenessAnoSpherical      reflns.pdbx_percent_possible_spherical_anomalous         https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_percent_possible_spherical_anomalous.html
        CompletenessAnoEllipsoidal    reflns.pdbx_percent_possible_ellipsoidal_anomalous       https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_percent_possible_ellipsoidal_anomalous.html
        RedundancyAno                 reflns.pdbx_redundancy_anomalous                         https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_redundancy_anomalous.html

      Resolution shell (mmCIF reflns_shell category, https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.number_unique_all.html):

        R(merge)                      reflns_shell.pdbx_Rmerge_I_obs                           https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_Rmerge_I_obs.html
        R(meas)                       reflns_shell.pdbx_Rrim_I_all                             https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_Rrim_I_all.html
        R(pim)                        reflns_shell.pdbx_Rpim_I_all                             https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_Rpim_I_all.html
        I/SigI                        reflns_shell.meanI_over_sigI_obs                         https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.meanI_over_sigI_obs.html
        CC(1/2)                       reflns_shell.pdbx_CC_half                                https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_CC_half.html
        CC(ano)                       reflns_shell.pdbx_CC_half_anomalous                      https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_CC_half_anomalous.html
        SigAno                        reflns_shell.pdbx_absDiff_over_sigma_anomalous           https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_absDiff_over_sigma_anomalous.html
        Completeness                  reflns_shell.percent_possible_all                        https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.percent_possible_all.html
        CompletenessSpherical         reflns_shell.pdbx_percent_possible_spherical_anomalous   https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_percent_possible_spherical_anomalous.html
        CompletenessEllipsoidal       reflns_shell.pdbx_percent_possible_ellipsoidal_anomalous https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_percent_possible_ellipsoidal_anomalous.html
        Redundancy                    reflns_shell.pdbx_redundancy                             https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_redundancy.html
        CompletenessAno               reflns_shell.pdbx_percent_possible_anomalous             https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_percent_possible_anomalous.html
        CompletenessAnoSpherical      reflns_shell.pdbx_percent_possible_spherical_anomalous   https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_percent_possible_spherical_anomalous.html
        CompletenessAnoEllipsoidal    reflns_shell.pdbx_percent_possible_ellipsoidal_anomalous https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_percent_possible_ellipsoidal_anomalous.html
        RedundancyAno                 reflns_shell.pdbx_redundancy_anomalous                   https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_redundancy_anomalous.html

    Completeness values are given in %, 0 <= Completeness <= 100"""

    type: QualityFactorType = Field(description="Quality factor type")
    value: float = Field(description="Quality factor value")


class Macromolecule(BaseModel):
    """Macromolecule - main molecule under investigation

    #NB model still incomplete"""

    acronym: str = Field(description="Acronynm - short synonym of macromolecule")
    name: Optional[str] = Field(
        default=None,
        description="Human readable name of macromolecule",
    )
    identifiers: Dict[str, str] = Field(
        default_factory=dict,
        description="Dictionary str:str  of contextName: identifier."
        "contextName could refer to a LIMS, database, or web site "
        "but could also be e.g. 'sequence'",
    )


class Component(BaseModel):
    """Additional component of sample ('ligand')

    #NB model still incomplete"""

    acronym: str = Field(
        description="Acronynm - short synonym of component (e.g. 'lig1'"
    )
    name: Optional[str] = Field(
        default=None, description="Human readable name of component"
    )
    identifiers: Dict[str, str] = Field(
        default_factory=dict,
        description="Dictionary str:str of contextName: identifier."
        "contectName will typically refer to a LIMS, database, or web site "
        "but could also be e.g. 'smiles'",
    )


class MXExperiment(core.Job):
    """MX Crystallographic data acquisition experiment."""

    mxlims_type: Literal["MXExperiment"] = Field(
        default="MXExperiment",
        description="The type of MXLIMS object.",
    )
    experiment_strategy: Optional[str] = Field(
        default=None,
        description="Experiment strategy indicator",
        json_schema_extra={
            "examples": [
                "OSC",
                "Helical",
                "MXPressE",
                "GPhL.native.basic",
                "GPhL.SAD.advanced",
                "GPhL.2wvlMAD.basic",
            ],
        },
    )
    expected_resolution: Optional[float] = Field(
        default=None,
        ge=0,
        description="The resolution expected in the experiment "
        "- for positioning the detector and setting up the experiment",
    )
    target_completeness: Optional[float] = Field(
        default=None,
        ge=0.0,
        le=100.0,
        description="Minimal completeness expected from experiment",
    )
    target_multiplicity: Optional[float] = Field(
        default=None,
        ge=0,
        description="Minimal multiplicity expected from experiment",
    )
    dose_budget: Optional[float] = Field(
        default=None,
        ge=0,
        description="Dose (MGy) to be used in experiment",
    )
    snapshot_count: Optional[int] = Field(
        default=None,
        ge=0,
        description="Number of snapshots to acquire after each (re)centring",
    )
    wedge_width: Optional[float] = Field(
        default=None,
        ge=0,
        description="Wedge width (in degrees) to use for interleaving",
    )
    measured_flux: Optional[float] = Field(
        default=None,
        ge=0,
        description="Measured value of beam flux in photons/s",
    )
    radiation_dose: Optional[float] = Field(
        default=None,
        ge=0,
        description="Total radiation dose absorbed during experiment",
    )
    unit_cell: Optional[UnitCell] = Field(
        default=None,
        description="Crystallographic unit cell, "
        "as determined during characterisation",
    )
    space_group_name: Optional[str] = Field(
        default=None,
        description="Name of space group, as determined during characterisation. "
        "Names may include alternative settings.",
    )
    # Overriding superclass fields, for more precise typing
    sample: Optional["MXSample"] = Field(
        default=None,
        frozen=True,
        description="MX Crystallographic sample relevant to Job.",
    )
    # NB logistical_sample should be typed more precisely, once we have that modeled
    logistical_sample: Optional[core.LogisticalSample] = Field(
        default=None,
        frozen=True,
        description="Logistical Sample or Sample location relevant to Job."
        "Overridden by Dataset.logistical_sample; return link for Logisticalsample.jobs",
    )
    templates: List["CollectionSweep"] = Field(
        default_factory=list,
        discriminator="mxlims_type",
        description="Templates with parameters for output datasets ",
    )
    reference_data: List["ReflectionSet"] = Field(
        default_factory=list,
        discriminator="mxlims_type",
        description="Reference data sets, e.g. a reference MTZ file, ",
    )
    results: List["CollectionSweep"] = Field(
        default_factory=list,
        discriminator="mxlims_type",
        description="Datasets produced by Job (match Dataset.source_ref)",
    )


class MXExperimentRef(core.MxlimsObjectRef):
    """Reference to MXExperiment object, for use in JSON files."""

    target_type: Literal["MXExperiment"]= Field(
        default="MXExperiment",
        description="The type of MXLIMS object linked to.",
    )


class CollectionSweep(core.Dataset):
    """
    MX  Crystallographic data collection sweep, may be subdivided for acquisition

     Note that the CollectionSweep specifies a single, continuous sweep range,
     with equidistant images given by image_width, and all starting motor positions
     in axis_position_start. axis_positions_end contain the end point of the sweep,
     and must have at least the value for the scan_axis; sweeps changing more than
     one motor (e.g. helical scan) can be represented by adding more values
     to axis_positions_end. The default number of images can be calculated from the
     sweep range and image_width. The actual number of images, the image numbering,
     and the order of acquisition (including interleaving) follows from the list of
     Scans. The role should be set to 'Result' for those sweeps that are deemed to
     be the desired result of the experiment; in templates you would prefer to use
     Acquisition for the Dataset that gives the acquisition parameters.
    """

    mxlims_type: Literal["CollectionSweep"]= Field(
        default="CollectionSweep",
        description="The type of MXLIMS object.",
    )
    annotation: Optional[str] = Field(
        default=None,
        description="Annotation string for sweep",
    )
    exposure_time: Optional[float] = Field(
        default=None,
        ge=0,
        description="Exposure time in seconds",
    )
    image_width: Optional[float] = Field(
        default=None,
        ge=0,
        description="Width of a single image, along scan_axis. "
        "For rotational axes in degrees, for translations in mm.",
    )
    overlap: Optional[float] = Field(
        default=None,
        description="Overlap between successivce images, in degrees. "
        "May be negtive for non-contiguous images.",
    )
    number_triggers: Optional[int] = Field(
        default=None,
        ge=0,
        description="Number of triggers. Instruction to detector "
        "- does not modify effect of other parameters.",
    )
    number_images_per_trigger: Optional[int] = Field(
        default=None,
        ge=0,
        description="Number of images per trigger. Instruction to detector "
        "- does not modify effect of other parameters.",
    )
    energy: Optional[float] = Field(
        default=None,
        ge=0,
        description="Energy of the beam in eV",
    )
    transmission: Optional[float] = Field(
        default=None,
        ge=0,
        le=100,
        description="Transmission setting in %",
    )
    resolution: Optional[float] = Field(
        default=None,
        description="Resolution that the sweep was intended to measure"
        "For offset or unusual detectors this may *not* determine the detector distance"
        "The actual detector distance can be found in axis_positions_start",
    )
    detector_roi_mode: Optional[str] = Field(
        default=None,
        description="Region-of-interest mode of detector. "
        "Should be made into an enumeration",
    )
    beam_position: Optional[Tuple[float, float]] = Field(
        default=None,
        description="x,y position of the beam on the detector in pixels",
    )
    beam_size: Optional[Tuple[float, float]] = Field(
        default=None,
        description="x,y size of the beam on the detector in mm",
    )
    beam_shape: Optional[str] = Field(
        default=None,
        description="Shape of the beam. NBNB Should be an enumeration",
        json_schema_extra={
            "examples": ["unknown", "rectangular", "ellipsoid"],
        },
    )
    detector_type: Optional[str] = Field(
        default=None,
        description="Type of detector, "
        "using enumeration of mmCIF items diffrn_detector.type "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_diffrn_detector.type.html)",
    )
    detector_binning_mode: Optional[str] = Field(
        default=None,
        description="Binning mode of detector. Should be made into an enumeration",
    )
    axis_positions_start: Dict[str, float] = Field(
        default_factory=dict,
        description="Dictionary string:float with starting position of all axes,"
        " rotations or translations, including detector distance, by name. "
        "Units are m for distances, degrees for angles"
        "NBNB do we use internal motor names (e.g. 'phi'), or std. names (e.g. 'omega')?",
    )
    axis_positions_end: Dict[str, float] = Field(
        default_factory=dict,
        description="Dictionary string:float with final position of scanned axes"
        " as for axis_positions_start,"
        "NB scans may be acquired out of order, so this determines the limits "
        "of the sweep, not the temporal start and end points",
    )
    scan_axis: str = Field(
        description="Name of main scanned axis. "
        "Other axes may be scanned in parallel.",
        json_schema_extra={
            "examples": [
                "omega",
                "kappa",
                "phi",
                "chi",
                "twoTheta",
                "sampleX",
                "sampleY",
                "sampleZ",
                "detectorX",
                "detectorY",
            ],
        },
    )
    scans: List["Scan"] = Field(
        default_factory=list,
        description="List of Snas i.e. subdivisions of CollectionSweep"
        "NB Scans need not be contiguous or in order or add up to entire sweep",
    )
    file_type: Optional[str] = Field(
        default=None,
        description="Type of file.",
        json_schema_extra={
            "examples": ["mini-cbf", "imgCIF", "FullCBF", "HDF5", "MarCCD"],
        },
    )
    prefix: Optional[str] = Field(
        default=None,
        description="Input parameter - used to build the fine name template.",
    )
    filename_template: Optional[str] = Field(
        default=None,
        description="File name template,  includes prefix, suffix, "
        "run number, and a slot where image number can be filled in.",
    )
    path: Optional[str] = Field(
        default=None,
        description="Path to directory containing image files.",
    )
    source_ref: Optional[MXExperimentRef] = Field(
        default=None,
        frozen=True,
        description="Reference to Job that created this Dataset",
    )
    # NB This rasies the problem of how to handle an optional Union
    # As we will surely get a Union here once Logistical Samples are modelled.
    logistical_sample_ref: Optional[core.LogisticalSampleRef] = Field(
        default=None,
        description="Reference to LogisticalSample that pertains this Dataset",
    )
    derived_from_ref: Optional["CollectionSweepRef"] = Field(
        default=None,
        description="Reference to Dataset from which this Dataset was derived. "
        "Used for modified Datasets without a 'source_ref' link, "
        "e.g. when removing images from a sweep before processing.",
    )
    derived_dataset_refs: List["CollectionSweepRef"] = Field(
        default_factory=list,
        description="List of references to Datasets derived from Dataset.",
    )


class CollectionSweepRef(core.MxlimsObjectRef):
    """Reference to CollectionSweep object, for use in JSON files."""

    target_type: Literal["CollectionSweep"]= Field(
        default="CollectionSweep",
        description="Type of MXLIMS object linked to",
    )


class Scan(BaseModel):
    """Subdivision of CollectionSweep.

    The Scan describes a continuously acquired set of images that forms a subset of the
    CollectionSweep of which they form part. The ordinal gives the acquisition order of
    sweeps across an entire multi-sweep experiment; this allows you to describe
    out-of-order acquisition and interleaving.
    """

    scan_position_start: float = Field(
        description="Value of scan axis for the first image, "
        "in units matching axis type",
    )
    first_image_number: int = Field(
        description="Image number to use for first image",
    )
    number_images: int = Field(
        ge=0,
        description="Number of images to acquire as part of the Scan.",
    )
    ordinal: int = Field(
        description="Ordinal defining the ordering of all scans within the "
        "experiment (not just within the scan)",
    )


class MXProcessing(core.Job):
    """MX Crystallographic processing calculation, going from images to reflection sets"""

    mxlims_type: Literal["MXProcessing"]= Field(
        default="MXProcessing",
        description="Type of MXLIMS object."
    )
    unit_cell: Optional[UnitCell] = Field(
        default=None,
        description="Expected unit cell for processing.",
    )
    space_group_name: Optional[str] = Field(
        default=None,
        description="Name of expected space group, for processing. "
        "Names may include alternative settings. "
        "Matches mmCIF item symmetry.space_group_name_H-M "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_symmetry.space_group_name_H-M.html).",
    )
    # Overriding superclass fields, for more precise typing
    sample: Optional["MXSample"] = Field(
        default=None,
        frozen=True,
        description="MXsample relevant to Job.",
    )
    # NB logistical_sample should be typed more precisely, once we have that modeled
    logistical_sample: Optional[core.LogisticalSample] = Field(
        default=None,
        frozen=True,
        description="Logistical Sample or Sample location relevant to Job."
        "Overridden by Dataset.logistical_sample; return link for Logisticalsample.jobs",
    )
    templates: List["ReflectionSet"] = Field(
        default_factory=list,
        discriminator="mxlims_type",
        description="Templates with parameters for output datasets ",
    )
    reference_data: List["ReflectionSet"] = Field(
        default_factory=list,
        discriminator="mxlims_type",
        description="Reference data sets, e.g. a reference MTZ file, ",
    )
    results: List["ReflectionSet"] = Field(
        default_factory=list,
        discriminator="mxlims_type",
        description="Datasets produced by Job (match Dataset.source_ref)",
    )
    input_data: List[CollectionSweep] = Field(
        default_factory=list,
        description="List of pre-existing Input data sets used for calculation,",
    )


class MXProcessingRef(core.MxlimsObjectRef):
    """Reference to MXProcessing object, for use in JSON files."""

    target_type: Literal["MXProcessing"]= Field(
        default="MXProcessing",
        description="Type of MXLIMS object linked to",
    )


class ReflectionStatistics(BaseModel):
    """Reflection statistics for a shell (or all) of reflections"""

    resolution_limits: Tuple[float, float] = Field(
        description="lower, higher resolution limit of shell, "
        "matches mmCIF items reflns_shell.d_res_low "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.d_res_low.html)"
        " and reflns_shell.d_res_high "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.d_res_high.html)",
    )
    number_observations: Optional[int] = Field(
        default=None,
        ge=0,
        description="total number of observations, "
        "matches mmCIF item reflns_shell.number_measured_all "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.number_measured_all.html)",
    )
    number_observations_unique: Optional[int] = Field(
        default=None,
        ge=0,
        description="total number of unique observations, "
        "matches mmCIF item reflns_shell.number_unique_all "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.number_unique_all.html)",
    )
    number_reflections_rejected: Optional[int] = Field(
        default=None,
        ge=0,
        description="Number of rejected reflections within this resolution shell, "
        "matches mmCIF item reflns_shell.pdbx_rejects.html "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_rejects.html)",
    )
    chi_squared: Optional[float] = Field(
        default=None,
        ge=0.0,
        description="Chi-squared statistic for reflection shell, "
        "matches mmCIF item reflns_shell.pdbx_chi_squared "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns_shell.pdbx_chi_squared.html)",
    )
    quality_factors: List[QualityFactor] = Field(
        default_factory=list, description="Quality factors for reflection shell, "
    )


class ReflectionSet(core.Dataset):
    """Processed reflections, possibly merged or scaled

    as might be stored within a MTZ or mmCIF reflection file
    """

    mxlims_type: Literal["ReflectionSet"]= Field(
        default="ReflectionSet",
        description="Type of MXLIMS object linked to.",
    )
    anisotropic_diffraction: bool = Field(
        default=False,
        description="Is diffraction limit analysis based on anisotropic diffraction "
        "limits? True/False ",
    )
    unit_cell: Optional[UnitCell] = Field(
        default=None,
        description="Unit cell determined",
    )
    space_group_name: Optional[str] = Field(
        default=None,
        description="Name of detected space group. "
        "Names may include alternative settings.",
    )
    operational_resolution: Optional[float] = Field(
        default=None,
        description="Operational resolution (A) matching observed_criteria.",
    )
    diffraction_limits_estimated: Optional[Tensor] = Field(
        default=None,
        description="Principal axes lengths (A) of ellipsoid "
        "describing reciprocal space region containing observable reflections, "
        "regardless whether all have actually been observed. "
        "Matches mmCIF items reflns.pdbx_aniso_diffraction_limit_{1,2,3} "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_aniso_diffraction_limit_1.html)",
    )
    wavelengths:List[float] = Field(
        default_factory=list,
        description="Wavelengths (A) at chich reflections were measured",
    )
    B_iso_Wilson_estimate: Optional[float] = Field(
        default=None,
        description="estimated (isotropic) temperature factor from slope of Wilson plot, "
        "matches mmCIF item reflns.B_iso_Wilson_estimate "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.B_iso_Wilson_estimate.html)",
    )
    aniso_B_tensor: Optional[Tensor] = Field(
        default=None,
        description="Anisotropic B tensor, matching mmCIF items "
        "reflns.pdbx_aniso_B_tensor_eigenvalue_{1,2,3} "
        "and reflns.pdbx_aniso_B_tensor_eigenvector_{1,2,3}_ortho[{1,2,3}] "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_aniso_B_tensor_eigenvalue_1.html)",
    )
    number_reflections: Optional[int] = Field(
        default=None,
        ge=0,
        description="Total number of measured reflections, matches mmCIF item "
        "reflns.pdbx_number_measured_all "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_number_measured_all.html)",
    )
    number_reflections_unique: Optional[int] = Field(
        default=None,
        ge=0,
        description="Total number of unique reflections, matches mmCIF item "
        "reflns.number_obs (https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.number_obs.html)",
    )
    h_index_range: Optional[Tuple[int, int]] = Field(
        default=None,
        description="low and high limit on Miller index h, matches mmCIF item "
        "reflns.limit_h_min "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.limit_h_min.html)"
        " and reflns.limit_h_max "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.limit_h_max.html)",
    )
    k_index_range: Optional[Tuple[int, int]] = Field(
        default=None,
        description="low and high limit on Miller index k, matches mmCIF item "
        "reflns.limit_k_min "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.limit_k_min.html)"
        " and reflns.limit_k_max "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.limit_k_max.html)",
    )
    l_index_range: Optional[Tuple[int, int]] = Field(
        default=None,
        description="low and high limit on Miller index l, matches mmCIF item "
        "reflns.limit_l_min "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.limit_l_min.html)"
        " and reflns.limit_l_max "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.limit_l_max.html)",
    )
    reflection_statistics_overall: Optional[ReflectionStatistics] = Field(
        default=None,
        description="Reflection statistics for all processed reflections",
    )
    reflection_statistics_shells: List[ReflectionStatistics] = Field(
        default_factory=list,
        description="Reflection statistics per resolution shell",
    )
    signal_type: Optional[PdbxSignalType] = Field(
        default=None,
        description="'local <I/sigmaI>', 'local wCC_half'; "
        "matches reflns.pdbx_signal_type "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_signal_type.html)."
        " Criterion for observability, as used in mmCIF refln.pdbx_signal_status "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_refln.pdbx_signal_status.html)",
    )
    signal_cutoff: Optional[float] = Field(
        default=None,
        description="Limiting value for signal calculation; "
        "matches reflns.pdbx_observed_signal_threshold "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_reflns.pdbx_observed_signal_threshold.html)."
        " Cutoff for observability, as used in mmCIF refln.pdbx_signal_status "
        "(https://mmcif.wwpdb.org/dictionaries/mmcif_pdbx_v50.dic/Items/_refln.pdbx_signal_status.html)",
    )
    resolution_cutoffs: List[QualityFactor] = Field(
        default_factory=list,
        description="Criteria used in determination of isotropic resolution cut-off "
        "(e.g. as implemented in MRFANA, https://github.com/githubgphl/MRFANA)",
    )
    binning_mode: Optional[ReflectionBinningMode] = Field(
        default=None, description="Binning mode for definition of resolution shells"
    )
    number_bins: Optional[int] = Field(
        default=None,
        gt=0,
        description="Number of bins",
    )
    reflections_per_bin: Optional[int] = Field(
        default=None,
        gt=0,
        description="Number of reflections per bin",
    )
    reflections_per_bin_per_sweep: Optional[int] = Field(
        default=None,
        gt=0,
        description="Number of reflections per bin per sweep (in multi-sweep experiment)",
    )
    resolution_rings_detected: List[Tuple[float, float]] = Field(
        default_factory=list,
        description="Resolution rings detected as originating from ice, powder "
        "diffraction etc.; given as a pair of floats (A) with decreasing value, "
        "i.e. low- and high-resolution limits",
    )
    resolution_rings_excluded: List[Tuple[float, float]] = Field(
        default_factory=list,
        description="Resolution rings excluded from calculation; "
        "given as a pair of floats (A) with decreasing value, "
        "i.e. low- and high-resolution limits)",
    )
    file_type: Optional[FileType] = Field(
        default=None,
        description="Type of file",
    )
    filename: Optional[str] = Field(
        default=None,
        description="File name.",
    )
    path: Optional[str] = Field(
        default=None,
        description="Path to directory containing reflection set file "
        "(defined by filename).",
    )
    source_ref: Optional[MXProcessingRef] = Field(
        default=None,
        frozen=True,
        description="Reference to Job that created this Dataset",
    )
    # NB This raises the problem of how to handle an optional Union
    # As we will surely get a Union here once Logistical Samples are modelled.
    logistical_sample_ref: Optional[core.LogisticalSampleRef] = Field(
        default=None,
        description="Reference to LogisticalSample"
        " that pertains specifically this Dataset",
    )
    derived_from_ref: Optional["ReflectionSetRef"] = Field(
        default=None,
        description="Reference to Dataset from which this Dataset was derived. "
        "Used for modified Datasets without a 'source_ref' link, "
        "e.g. when removing images from a sweep before processing.",
    )
    derived_dataset_refs: List["ReflectionSetRef"] = Field(
        default_factory=list,
        description="List of references to Datasets derived from Dataset.",
    )


class ReflectionSetRef(BaseModel):
    """Reference to ReflectionSet object, for use in JSON files."""

    target_type: Literal["ReflectionSet"]= Field(
        default="ReflectionSet",
        description="Type of MXLISM object linked to.",
    )


class MXSample(core.PreparedSample):
    """Prepared Sample with MX crystallography-specific additions

    NB this class is still unfinished"""

    mxlims_type: Literal["MXSample"]= Field(
        default="MXSample",
        description="Type of MXLIMS object.",
    )
    name: Optional[str] = Field(
        default=None,
        description="Short identifying name for Sample",
    )
    macromolecule: Macromolecule = Field(
        default=None,
        description="Macromolecule formingt crystal(s) in sample",
    )
    components: List[Component] = Field(
        default_factory=list,
        description="List of components in sample",
    )
    unit_cell: Optional[UnitCell] = Field(
        default=None,
        description="Unit cell expected in sample.",
    )
    space_group_name: Optional[str] = Field(
        default=None,
        description="Name of space group expected in Sample. "
        "Names may include alternative settings.",
    )
    radiation_sensitivity: Optional[float] = Field(
        default=None,
        ge=0.0,
        le=1.0,
        description="Relative radiation sensitivity of sample.",
    )
    identifiers: Dict[str, str] = Field(
        default_factory=dict,
        description="Dictionary str:str of contextName: identifier."
        "contectName will typically refer to a LIMS, database, or web site "
        "and the identifier will point to the ample within thie context",
        json_schema_extra={
            "examples": [
                {
                    "sendersId": "29174",
                    "receiversUrl": "http://lims.synchrotron.org/crystal/54321",
                },
            ],
        },
    )
    job_refs: List[Union[MXExperimentRef, MXProcessingRef]] = Field(
        default_factory=list,
        discriminator="target_type",
        description="Jobs (templates, planned, initiated or completed)"
        "for this PreparedSample",
    )
    logistical_sample_refs: List[core.LogisticalSampleRef] = Field(
        default_factory=list,
        discriminator="target_type",
        description="References to LogisticalSamples using Sample",
    )


class MXSampleRef(core.MxlimsObjectRef):
    """Reference to MXSample object, for use in JSON files."""

    target_type: Literal["MXSample"]= Field(
        default="MXSample",
        description="Type of MXLIMS object linked to.",
    )


if __name__ == "__main__":
    # Usage:
    # In target directory .../mxlims/pydantic/jsonSchema do
    # python -m mxlims.pydantic.crystallography
    import json

    for cls in (
        core.LogisticalSample,
        CollectionSweep,
        ReflectionSet,
        MXExperiment,
        MXProcessing,
        MXSample,
    ):
        tag = cls.__name__
        schema = cls.model_json_schema()
        fp = open("%s_schema.json" % tag, "w")
        json.dump(schema, fp, indent=4)

    # To generate html documentation use e.g.
    # generate-schema-doc --link-to-reused-ref LogisticalSample_schema.json ../jsonDocs
