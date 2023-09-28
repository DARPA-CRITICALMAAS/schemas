"""
Schemas for TA3 data input from TA4
"""
from pydantic import BaseModel, Field
from typing import Optional, TypeVar


Point = TypeVar("Point")
WKT = TypeVar("WKT", bound=str)


class Map(BaseModel):
    """Schema for map information."""

    ref_url: str = Field(..., description="Source URL of the map")
    ref_name: str = Field(..., description="Short name of the map")
    ref_title: str = Field(..., description="Title of the map")
    ref_authors: list[str] = Field(..., description="Authors")
    ref_source: str = Field(
        ...,
        description="Publication/data release containing the map",
        examples=["U.S. Geological Survey Data Series 424"],
    )
    ref_year: int = Field(..., description="Publication year", examples=["2009"])


class GeologySampleAnalyticData(BaseModel):
    # need to mark lots of these as optional
    field_id: Optional[str] = Field(..., description='Field identifiers assigned by the sample collector of '
                                           'samples submitted for analysis.')
    lab_id: Optional[str] = Field(..., description='Laboratory batch identifiers assigned by the Sample Control Officers of the '
                                         'analytical laboratories that received the samples as batches. ')
    job_id: Optional[str] = Field(..., description='Unique identifiers assigned to submitted samples by the Sample Control Officer'
                                         ' of the analytical laboratory that received the samples')
    submitter: Optional[str] = Field(..., description=' Names of the individuals who submitted samples in batches to the '
                                            'laboratories for analysis')
    project_name: Optional[str] = Field(..., description='Project names, at times derived from project account numbers, of work '
                                               'groups funded for the collection and analysis of submitted samples')
    date_submitted: Optional[str] = Field(..., description='Date sample was submitted to Sample Control for initial database '
                                                      'processing prior to sample prep and analysis; or date sample and'
                                                      ' its data were added to the database from non-USGS sources. '
                                                      'in the format mm/dd/yyyy')
    method_collected: Optional[str] = Field(..., description='Sample collection method: single grab, composite, or channel.')
    previous_job_id: Optional[str] = Field(..., description='Original NGDB batch numbers (JOB_ID) of USGS resubmitted samples '
                                                  'that have been given new batch numbers upon resubmittal for further analysis. ')
    previous_lab_id: Optional[str] = Field(..., description='Original NGDB LAB_IDs of USGS resubmitted samples that have been'
                                                  ' given new lab numbers upon resubmittal for further analysis.')
    publ_id: Optional[str] = Field(..., description='Identifiers for publications that are sources of data, or where data is cited.')
    data_source: Optional[str] = Field(..., description='Identifiers for other sources of data; databases, publications, individuals.')


class GeologySampleLocationData(BaseModel):
    # need to mark lots of these as optional
    country: Optional[str] = Field(..., description='Countries or marine bodies of water from where samples were collected')
    state_province: Optional[str] = Field(..., description='Countries or marine bodies of water from where samples were collected.')
    quad: Optional[str] = Field(..., description=' Names of 1:250,000-scale quadrangles '
                                       '(1-degree x 2-degree or 1-degree by 3-degree) in which samples were collected.')
    latitude: float = Field(..., description='Latitude coordinate of sample site, reported in decimal degrees; '
                                             'see metadata for further datum and spheroid information.')
    longitude: float = Field(..., description='Longitude coordinate of sample site, reported in decimal degrees; '
                                              'there are sites on both sides of the International Date Line; '
                                              'see metadata for further datum and spheroid information')
    spheroid: Optional[str] = Field(..., description='Reference spheroids or ellipsoids, when recorded, for the latitude and '
                                           'longitude coordinates of the sample sites.')
    datum: Optional[str] = Field(..., description='Reference datums, when recorded, for the latitude and longitude coordinates'
                                        ' of the sample sites.')
    coordinates_qual: Optional[int] = Field(..., description='Qualifier code regarding precision of coordinates gained using GIS.'
                                                   ' Not all samples have the code if they weren’t determined by GIS '
                                                   'analysis')
    coordinates_comment: Optional[str] = Field(..., description=' Comments regarding precision of geospatial coordinates.')
    locate_desc: Optional[str] = Field(..., description='Geographic information relating to the locations of the sample sites.')
    depth: Optional[int] = Field(..., description='Depths from the surface at which samples were collected; units are specified'
                                        ' by the submitter and included with the values.')


class GeologyGeologicData(BaseModel):
    # need to mark lots of these as optional
    sample_source: Optional[str] = Field(..., description='Physical settings or environments from which the samples were collected. ')
    primary_class: Optional[str] = Field(..., description='Primary classifications of sample media. ')
    secondary_class: Optional[str] = Field(..., description='Secondary classifications or subclasses of sample media. ')
    specific_name: Optional[str] = Field(..., description='Specific names for sample media. ')
    sample_comment: Optional[str] = Field(..., description='Attributes used to modify PRIMARY_CLASS, SECONDARY_CLASS, or SPECIFIC_NAME. ')
    addl_attr: Optional[str] = Field(..., description='Additional attributes used to modify PRIMARY_CLASS, SECONDARY_CLASS, or SPECIFIC_NAME.')
    geologic_age: Optional[str] = Field(..., description='Ages or ranges of ages from the Geological Time Scale for the collected samples. ')
    stratigraphy: Optional[str] = Field(..., description='Names of the stratigraphic units from which samples were collected. ')
    strat_grp: Optional[str] = Field(..., description='Summary field of formations, groups or supergroups for entries in STRATIGRAPHY. ')
    start_sort: Optional[str] = Field(..., description='Summary field for entries in STRATIGRAPHY. ')
    regional_geology: Optional[str] = Field(..., description='Regional geologic settings of stratigraphic units. ')
    tectonic_setting: Optional[str] = Field(..., description='Tectonic settings for deposition of stratigraphic units. ')
    source_terrain: Optional[str] = Field(..., description='Tectonic terrains as sources of deposition for stratigraphic units. ')
    metallogeny: Optional[str] = Field(..., description='Metallogenic associations of stratigraphic units. ')
    mineralizaton: Optional[str] = Field(..., description='Indications of mineralization or mineralization types as provided by sample submitters. ')
    alteration: Optional[str] = Field(..., description='Indications of the presence or types of alteration noted in samples by submitters. ')


class GeologySampleData(BaseModel):
    """metadata related to the geology of the sample from Geology.txt file"""
    analytics: Optional[GeologySampleAnalyticData] = Field(..., description='data related to the analytic methods for obtaining' \
                                                                 'and processing the sample')
    location: Optional[GeologySampleLocationData] = Field(..., description='data related ot the location of the sample')
    geologic: Optional[GeologyGeologicData] = Field(..., description='data related to the specific geology of the sample')


class MineralBestValueData(BaseModel):
    """Data from BestValue_Element.txt file
    values listed as optional due to some elements being measured in ppm and others as a percent, and not all elements
    having measurements"""
    cmibs_id: int = Field(...,  description='Unique identifier assigned to each sample entered in the CMIBS geochemical '
                                            'database; foreign key from Geology table')
    element_ppm: Optional[float] = Field(..., description='elemental best value in ppm')
    element_pct: Optional[float] = Field(..., description='elemental best value in pct')
    element_am: Optional[str] = Field(..., description='analytical method used for "best value", abbreviation; '
                                                         'see ANALYTIC_METHOD field of AnalyticMethod table for method description')
    element_ppm_all: Optional[float] = Field(..., description='elemental all values in ppm')
    element_pct_all: Optional[float] = Field(..., description='elemental all values in pct')


class WholeRockBestValueMajorsData(BaseModel):
    """Data from BestValue_WholeRock_Majors.txt file"""
    cmibs_id: int = Field(..., description='Unique identifier assigned to each sample entered in the CMIBS geochemical '
                                           'database; foreign key from Geology table')
    wr_qual: int = Field(..., description='Qualifier for whole rock analysis, from 1 to 6, where 1 is the most precise '
                                          'analytical method package with the best sample digestion, and 6 is the least')
    compound_pct: Optional[float] = Field(..., description='compound best value in weight percent')
    compound_am: Optional[str] = Field(..., description='analytical method used for "best value", abbreviation; '
                                                         'see ANALYTIC_METHOD field of AnalyticMethod table for method description')
    element_pct_all: Optional[float] = Field(..., description='compound all values in weight pct')


class WholeRockBestValueOthersData(BaseModel):
    """Data from BestValue_WholeRock_Others.txt file"""
    # NOT COMPLETE
    cmibs_id: int = Field(..., description='Unique identifier assigned to each sample entered in the CMIBS geochemical '
                                           'database; foreign key from Geology table')
    loi_pct: float = Field(..., description='Loss on ignition, at 900 to 950 degrees centigrade, as "best value", '
                                             'in weight percent. Negative values indicate concentrations less than the '
                                             'lower limit of determination for the analytical method. The absolute value'
                                             ' of the negative number is the lower limit of determination. '
                                             'A null (or empty cell) means not analyzed. (Source: Metadata author)')
    loi_am: float = Field(..., description='Loss on ignition, at 900 to 950 degrees centigrade, analytical method used'
                                           ' for "best value"; see ANALYTIC_METHOD field of AnalyticMethod table for '
                                           'method description')
    NOT_FINISHED: str = Field(..., description='still lots of columns to go through')


class MapPoint(BaseModel):
    id: int = Field(..., description="Internal ID of the point. CMIBS Sample ID")
    geometry: Point = Field(..., description="Geometry of this feature, expressed as Lat Long in geographic coordinates")
    geology: GeologySampleData = Field(..., description="Associated geologic data of the sample")
    mineral_best_value: MineralBestValueData = Field(..., description="'Best Value' element chemical data")
    whole_rock_best_value_majors: WholeRockBestValueMajorsData = Field(..., description="'Best Value' whole rock chemical data")
    whole_rock_best_value_others: WholeRockBestValueOthersData = Field(...,
                                                                description="'Best Value' whole rock chemical data")

    source: Map = Field(..., description="Source map of the point")


class MapTile(BaseModel):
    """A tile representing geologic map information covering a small area."""

    x: int = Field(..., description="X coordinate of the tile")
    y: int = Field(..., description="Y coordinate of the tile")
    z: int = Field(..., description="Z coordinate of the tile")
    points: list[MapPoint] = Field(..., description="Points in the tile")


class Tileset(BaseModel):
    """Tiling scheme information."""

    bounds: list[float] = Field(..., description="Bounding box of the tile scheme")
    crs: WKT = Field(
        ...,
        description="Coordinate reference system of the tile scheme",
        # default="EPSG:3857 (Web Mercator)",
    )
    tile_size: int = Field(..., description="Size of the tiles in the scheme")
    tiles: list[MapTile] = Field(..., description="List of tiles in the scheme")
