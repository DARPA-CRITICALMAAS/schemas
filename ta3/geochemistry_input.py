"""
Schemas for TA3 data input from TA4
"""
from pydantic import BaseModel, Field
from typing import Optional, TypeVar


Point = TypeVar("Point")
WKT = TypeVar("WKT", bound=str)


class Map(BaseModel):
    """Schema for map information."""

    ref_url: str = Field(..., description="Source URL of the map.")
    ref_name: str = Field(..., description="Short name of the map.")
    ref_title: str = Field(..., description="Title of the map.")
    ref_authors: list[str] = Field(..., description="Authors")
    ref_source: str = Field(
        ...,
        description="Publication/data release containing the map",
        examples=["U.S. Geological Survey Data Series 424"],
    )
    ref_year: int = Field(..., description="Publication year", examples=["2009"])

class CoordinatesQualifier(BaseModel):
    """Metadata of qualifier codes for the precision of geographic coordinates."""

    coordinates_qual: int = Field(..., description="Qualifier code regarding precision of coordinates "
                                                             "gained using GIS. Value 1-5.")
    coordinates_qual_desc: str = Field(..., description="Description of coordinate qualifier.")
    estimated_accuracy: Optional[str] = Field(..., description="Estimated positional accuracy of geospatial coordinates "
                                                               "resolved by project.")
class SampleLocationData(BaseModel):
    """Metadata of spatial attributes for rock, sediment, soil and organic samples. Many fields may be optional."""

    country: Optional[str] = Field(..., description="Countries or marine bodies of water from where samples were "
                                                    "collected.")
    state_province: Optional[str] = Field(..., description="Countries or marine bodies of water from where samples "
                                                           "were collected.")
    quad: Optional[str] = Field(..., description="Names of 1:250,000-scale quadrangles (1-degree x 2-degree or 1-degree "
                                                 "by 3-degree) in which samples were collected.")
    latitude: float = Field(..., description="Latitude coordinate of sample site, reported in decimal degrees; "
                                             "see metadata for further datum and spheroid information.")
    longitude: float = Field(..., description="Longitude coordinate of sample site, reported in decimal degrees; "
                                              "there are sites on both sides of the International Date Line; "
                                              "see metadata for further datum and spheroid information.")
    spheroid: Optional[str] = Field(..., description="Reference spheroids or ellipsoids, when recorded, for the latitude"
                                                     " and longitude coordinates of the sample sites.")
    datum: Optional[str] = Field(..., description="Reference datums, when recorded, for the latitude and longitude "
                                                  "coordinates of the sample sites.")
    coordinates_qual: CoordinatesQualifier = Field(..., description="Qualifier code regarding precision of coordinates gained "
                                                             "using GIS. Not all samples have the code if they weren’t "
                                                             "determined by GIS analysis.")
    coordinates_comment: Optional[str] = Field(..., description="Comments regarding precision of geospatial coordinates.")
    locate_desc: Optional[str] = Field(..., description="Geographic information relating to the locations of the "
                                                        "sample sites.")
    depth: Optional[int] = Field(..., description="Depths from the surface at which samples were collected; units are "
                                                  "specified by the submitter and included with the values.")

class SampleAnalyticData(BaseModel):
    """Metadata of descriptive and analytical attributes for rock, sediment, soil and organic samples.
    Many fields may be optional."""

    field_id: Optional[str] = Field(..., description="Field identifiers assigned by the sample collector of samples "
                                                     "submitted for analysis.")
    lab_id: Optional[str] = Field(..., description="Laboratory batch identifiers assigned by the Sample Control "
                                                   "Officers of the analytical laboratories that received "
                                                   "the samples as batches.")
    job_id: Optional[str] = Field(..., description="Unique identifiers assigned to submitted samples by the Sample "
                                                   "Control Officer of the analytical laboratory that received "
                                                   "the samples.")
    submitter: Optional[str] = Field(..., description="Names of the individuals who submitted samples in batches to the "
                                                      "laboratories for analysis.")
    project_name: Optional[str] = Field(..., description="Project names, at times derived from project account numbers, "
                                                         "of work groups funded for the collection and analysis of "
                                                         "submitted samples.")
    date_submitted: Optional[str] = Field(..., description="Date sample was submitted to Sample Control for initial "
                                                           "database processing prior to sample prep and analysis; "
                                                           "or date sample and its data were added to the database "
                                                           "from non-USGS sources; in the format mm/dd/yyyy.")
    method_collected: Optional[str] = Field(..., description="Sample collection method: single grab, composite, "
                                                             "or channel.")
    previous_job_id: Optional[str] = Field(..., description="Original NGDB batch numbers (JOB_ID) of USGS resubmitted "
                                                            "samples that have been given new batch numbers upon "
                                                            "resubmittal for further analysis.")
    previous_lab_id: Optional[str] = Field(..., description="Original NGDB LAB_IDs of USGS resubmitted samples that "
                                                            "have been given new lab numbers upon resubmittal for "
                                                            "further analysis.")
    publ_id: Optional[str] = Field(..., description="Identifiers for publications that are sources of data, "
                                                    "or where data is cited.")
    data_source: Optional[str] = Field(..., description="Identifiers for other sources of data; databases, "
                                                        "publications, individuals.")
class SampleGeologicData(BaseModel):
    """Metadata of geologic attributes for rock, sediment, soil and organic samples. Many fields may be optional."""

    sample_source: Optional[str] = Field(..., description="Physical settings or environments from which the samples "
                                                          "were collected.")
    primary_class: Optional[str] = Field(..., description="Primary classifications of sample media.")
    secondary_class: Optional[str] = Field(..., description="Secondary classifications or subclasses of sample media.")
    specific_name: Optional[str] = Field(..., description="Specific names for sample media.")
    sample_comment: Optional[str] = Field(..., description="Attributes used to modify PRIMARY_CLASS, SECONDARY_CLASS, "
                                                           "or SPECIFIC_NAME.")
    addl_attr: Optional[str] = Field(..., description="Additional attributes used to modify PRIMARY_CLASS, "
                                                      "SECONDARY_CLASS, or SPECIFIC_NAME.")
    geologic_age: Optional[str] = Field(..., description="Ages or ranges of ages from the Geological Time Scale for "
                                                         "the collected samples.")
    stratigraphy: Optional[str] = Field(..., description="Names of the stratigraphic units from which samples "
                                                         "were collected.")
    strat_grp: Optional[str] = Field(..., description="Summary field of formations, groups or supergroups for entries "
                                                      "in STRATIGRAPHY.")
    start_sort: Optional[str] = Field(..., description="Summary field for entries in STRATIGRAPHY.")
    regional_geology: Optional[str] = Field(..., description="Regional geologic settings of stratigraphic units.")
    tectonic_setting: Optional[str] = Field(..., description="Tectonic settings for deposition of stratigraphic units.")
    source_terrain: Optional[str] = Field(..., description="Tectonic terrains as sources of deposition for "
                                                           "stratigraphic units.")
    metallogeny: Optional[str] = Field(..., description="Metallogenic associations of stratigraphic units.")
    mineralizaton: Optional[str] = Field(..., description="Indications of mineralization or mineralization types "
                                                          "as provided by sample submitters.")
    alteration: Optional[str] = Field(..., description="Indications of the presence or types of alteration noted "
                                                       "in samples by submitters.")

class SampleData(BaseModel):
    """Metadata of spatial, geologic and descriptive attributes for rock, sediment, soil and organic samples."""
    cmibs_id: int = Field(..., description="Unique identifier assigned to each sample entered in the "
                                           "CMIBS geochemical database.")
    analytics: SampleAnalyticData = Field(..., description="Data related to the analytic methods for obtaining "
                                                                     "and processing the sample.")
    location: SampleLocationData = Field(..., description="Data related ot the location of the sample.")
    geologic: SampleGeologicData = Field(..., description="Data related to the specific geology of the sample.")

class AnalyticMethodBiblio(BaseModel):
    """Metadata of references for analytical methods used to obtain chemical data. """

    analytic_method_pub_id: Optional[str] = Field(...,description="Unique author identifiers for analytic method publications.")
    reference_pub_id: Optional[str] = Field(..., description="Reference identifiers for analytic method publications.")
    analytic_method: Optional[str] = Field(..., description="Analytical method abbreviations, refers to field "
                                                             "ANALYTIC_METHOD of AnalyticalMethod table.")
    media: Optional[str] = Field(..., description="Analyzed media types for analytic method publications.")
    pub_author: Optional[str] = Field(..., description="Authors of analytical method publications.")
    pub_year: Optional[str] = Field(..., description="Year of analytic method publication. "
                                                     "Min: 1947, Max: 2017, Units: year")
    pub_citation: Optional[str] = Field(..., description="Bibliographic citation for analytic method publication; "
                                                         "may refer to chapter or section of publication.")
    pub_url: Optional[str] = Field(..., description="URL of analytical method publication, if available.")
class AnalyticMethod(BaseModel):
    """Metadata of analytical methods used to obtain chemical and physical data. """

    analytic_method: str = Field(...,description="Unique short name of analytical method.")
    analytic_method_desc: str = Field(..., description="Descriptions of analytical methods.")
    digestion_method: Optional[str] = Field(..., description="Digestion methods used in analytical methods.")
    source: AnalyticMethodBiblio


class WholeRockOthers_BestValueData(BaseModel):
    """Table of 'best value' chemical 'whole rock' data of other various elements, compounds and physical measurements
    for rock, sediment, soil and organic samples"""
    cmibs_id: int = Field(..., description="Unique identifier assigned to each sample entered in the CMIBS geochemical "
                                           "database; foreign key from Geology table.")
    #Loss on ignition: LOI, LOI1st, LOI2nd - vary by degrees
    loi_pct: float = Field(..., description="Loss on ignition as 'best value', in weight percent. Negative values "
                                               "indicate concentrations less than the lower limit of determination for "
                                               "the analytical method. The absolute value of the negative number is the "
                                               "lower limit of determination. A null or empty cell means not analyzed. "
                                               "LOI first at 600 to 650 degrees centegrade, LOI second at 900 to 950 "
                                               "degrees centegrade.")
    loi_pct_all: Optional[float] = Field(..., description="Loss on ignition, at 600 to 650 or 900 to 950 "
                                                             "degrees centigrade, all values, in weight percent, and "
                                                             "their analytical methods, from best method to least, "
                                                             "as concatenations.")

    #Other compounds: ash, C (carbon), CT02 (), CCO3 (), CaCO3 (), Cgraph (graphitic carbon), Corg (organic carbon),
    # CO2 (carbon dioxide), S (sulfur), SO3 (sulfite), SO4 (sulfate), Sorg (organic sulfur), Spyr (pyritic sulfur),
    # sulfide, FeHR (highly reactive iron), FePyr (pyritic iron), FeHC1 (acid soluble iron),
    # Pinorg (inorganic phosphorus), Porg (organic phrosphorus), N (nitrogen), Norg (organic nitrogen), H (hydrogen),
    # H2O (total water), H20b (water bound), H20m (moisture or nonessential water), Cl (cloride), F (Flouride)
    #acidinsol (Acid-insoluble residue), TOM (total organic matter)
    compound_pct: Optional[float] = Field(..., description="Other compound, as 'best value', in weight percent. "
                                                                "Negative values indicate concentrations less than the "
                                                                "lower limit of determination for the analytical method. "
                                                                "The absolute value of the negative number is the lower "
                                                                "limit of determination. A null (or empty cell) means "
                                                                "not analyzed.")
    compound_pct_am: AnalyticMethod = Field(..., description="Analytical methods used for 'best values' of other "
                                                                  "compound.")
    compound_pct_all: Optional[float] = Field(..., description="Other compound, all values, in weight percent, and "
                                                                    "their analytical methods, from best method to "
                                                                    "least, as concatenations.")
    dop_si: Optional[float] = Field(..., description="Degree of pyritization, as a calculation FePyr(FePyr + FeHCl), "
                                                     "as 'best value', in standard units. Negative values indicate "
                                                     "concentrations less than the lower limit of determination for "
                                                     "the analytical method. The absolute value of the negative number "
                                                     "is the lower limit of determination. A null (or empty cell) means "
                                                     "not analyzed for the species.")
    dop_am: AnalyticMethod = Field(..., description="Degree of pyritization, analytical method used for 'best value'; "
                                                    "see ANALYTIC_METHOD field of AnalyticMethod table for method "
                                                    "description.")
    dop_si_all: Optional[float] = Field(..., description="Degree of pyritization, all values, in weight percent, and "
                                                         "their analytical methods, from best method to least, as a "
                                                         "concatenation.")
    varDensity_gcc: Optional[float] = Field(..., description="Variable 'Bulk' or 'Powder' density, as 'best value', in "
                                                             "grams per cubic centimeter. A null (or empty cell) means "
                                                             "not analyzed for the species.")
    varDensity_am: AnalyticMethod = Field(..., description="Variable 'Bulk' or 'Powder' density, analytical method used "
                                                      "for 'best value'.")
    varDensity_gcc_all: Optional[float] = Field(..., description="Variable 'Bulk' or 'Powder' density, all values, in grams "
                                                             "per cubic centimeter, and their analytical methods, from "
                                                             "best method to least, as a concatenation.")
    satind_si: Optional[float] = Field(..., description="Saturation index, as 'best value', in standard units. A null "
                                                        "(or empty cell) means not analyzed for the species.")
    satind_am: AnalyticMethod = Field(..., description="Saturation index, analytical method used for 'best value.'")
    satind_si_all: Optional[float] = Field(...,
                                           description="Saturation index, all values, in standard units, and their "
                                                       "analytical methods, from best method to least, as a "
                                                       "concatenation.")
    tmax_degC: Optional[float] = Field(..., description="Temperature at which the maximum release of hydrocarbons occurs "
                                                        "during pyrolysis, as 'best value', in degrees Centigrade. A "
                                                        "null (or empty cell) means not analyzed for the species.")
    tmax_am: AnalyticMethod = Field(..., description= "Temperature at which the maximum release of hydrocarbons occurs "
                                                     "during pyrolysis, analytical methods used for 'best values.'")
    tmax_degC_all: Optional[float] = Field(..., description="Temperature at which the maximum release of hydrocarbons "
                                                            "occurs during pyrolysis, all values, in weight percent, and "
                                                            "their analytical methods, from best method to least, "
                                                            "as concatenations.")
    sVar_mgg: Optional[float] = Field(..., description="S1. Free hydrocarbons in the sample,  S2.Hydrocarbons generated "
                                                       "through thermal cracking of nonvolatile organic matter, or  "
                                                       "S3. Carbon dioxide produced during pyrolysis of kerogen, "
                                                       "as 'best value', in milligrams of S1-2. hydrocarbon or "
                                                       "S3. carbon dioxide per gram of rock. "
                                                       "Negative values indicate concentrations less than the lower "
                                                       "limit of determination for the analytical method. The absolute "
                                                       "value of the negative number is the lower limit of "
                                                       "determination. A null (or empty cell) means not analyzed for "
                                                       "the species.")
    sVar_am: AnalyticMethod = Field(..., description="Analytical method useds for 'best values.'")
    sVar_mgg_all: Optional[float] = Field(..., description="All values for S1, S2, S3, in weight percent, and their "
                                                           "analytical methods, from best method to least,"
                                                           "as concatenations.")
    var_ratio: Optional[float] = Field(..., description="Hydrogen index (hi), or oxygen index (oi), "
                                                        "or production index (pi), as 'best value', in milligrams of "
                                                        "hi: hydrocarbons [100 x S2] (hi), oi: carbon dioxide [100 x S3],"
                                                        "pi: [S1] hydrocarbons milligrams of [S1 + S2] hydrocarbons, "
                                                        "per gram of total organic carbon. A null (or empty cell) means "
                                                        "not analyzed for the species.")
    var_am: AnalyticMethod = Field(..., description="Analytical methods used for 'best values.'")
    var_ratio_all: Optional[float] = Field(..., description="Hydrogen index (in weight percent), "
                                                            "oxygen index (in parts per million), "
                                                            "or production index (in weight percent), "
                                                            "all values, in weight percent, and their analytical methods, "
                                                            "from best method to least, as concatenations.")
class WholeRockMajors_BestValueData(BaseModel):
    """Table of 'best value' chemical 'whole rock' major element data for rock, sediment, soil and organic samples. """
    cmibs_id: int = Field(..., description="Unique identifier assigned to each sample entered in the CMIBS geochemical "
                                           "database; foreign key from Geology table.")
    wr_qual: int = Field(..., description="Qualifier for whole rock analysis, from 1 to 6, where 1 is the most precise "
                                          "analytical method package with the best sample digestion, and 6 is the least.")
    wr_def: str = Field(..., description="Definition of qualifier for whole rock analysis.")
    compoundmajor_pct: Optional[float] = Field(..., description="Best value in weight percent of whole rock majority.")
    compoundmajor_am: AnalyticMethod
    compoundmajor_pct_all: Optional[float] = Field(..., description="All values in weight percent of whole rock majority.")

class Mineral_BestValueData(BaseModel):
    """Table of 'best value' chemical data for rock, sediment, soil and organic samples.
    Values listed as optional due to some elements being measured in ppm and others as a percent, and not all elements
    having measurements."""

    cmibs_id: int = Field(...,  description="Unique identifier assigned to each sample entered in the CMIBS geochemical "
                                            "database; foreign key from Geology table.")
    mineral_ppm: Optional[float] = Field(..., description="Parts per million of target mineral for best model.")
    mineral_pct: Optional[float] = Field(..., description="Best value of target mineral in weight percent.")
    mineral_am: AnalyticMethod
    mineral_ppm_all: Optional[float] = Field(..., description="Parts per million of target mineral for all models.")
    mineral_pct_all: Optional[float] = Field(..., description="All values of target mineral in weight percent.")


class MapPoint(BaseModel):
    id: int = Field(..., description="Internal ID of the point. CMIBS Sample ID.")
    source: Map = Field(..., description="Source map of the point.")
    geometry: Point = Field(...,description="Geometry of this feature, expressed as Lat Long in geographic coordinates.")
    geology: SampleData = Field(..., description="Associated geologic data of the sample.")
    mineral_best_value: Mineral_BestValueData = Field(...,
                                                      description="'Best Value' element chemical data.")
    whole_rock_majors_best_value: WholeRockMajors_BestValueData = Field(..., description="Table of 'best value' chemical "
                                                                                         "'whole rock' major element "
                                                                                         "data for rock, sediment, soil "
                                                                                         "and organic samples.")
    whole_rock_others_best_value: WholeRockOthers_BestValueData = Field(...,description="Table of 'best value' chemical "
                                                                                        "'whole rock' data of other "
                                                                                        "various elements, compounds and "
                                                                                        "physical measurements for rock, "
                                                                                        "sediment, soil and organic "
                                                                                        "samples.")

class MapTile(BaseModel):
    """A tile representing geologic map information covering a small area."""

    x: int = Field(..., description="X coordinate of the tile.")
    y: int = Field(..., description="Y coordinate of the tile.")
    z: int = Field(..., description="Z coordinate of the tile.")
    points: list[MapPoint] = Field(..., description="Points in the tile.")


class Tileset(BaseModel):
    """Tiling scheme information."""

    bounds: list[float] = Field(..., description="Bounding box of the tile scheme.")
    crs: WKT = Field(
        ...,
        description="Coordinate reference system of the tile scheme.",
        # default="EPSG:3857 (Web Mercator)",
    )
    tile_size: int = Field(..., description="Size of the tiles in the scheme.")
    tiles: list[MapTile] = Field(..., description="List of tiles in the scheme.")
