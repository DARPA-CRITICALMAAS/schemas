"""
Schemas for TA3 data output from TA4
"""
from pydantic import BaseModel, Field
from typing import Optional, TypeVar

Polygon = TypeVar("Polygon")
Line = TypeVar("Line")
Point = TypeVar("Point")
WKT = TypeVar("WKT", bound=str)


class AnalyticModel(BaseModel):
    """Link to bestval_mineral"""

    id: int = Field(..., description="ID of the extracted feature")
    analytic_method: str = Field(...,description="Unique short name of analytical method")
    analytic_method_desc: str = Field(..., description="Descriptions of analytical methods")
    digestion_method: str = Field(..., description="Digestion methods used in analytical methods")

class Geology(BaseModel):
    """Sample collection information"""

    CMIBS_ID: int = Field(..., description="Unique identifier assigned to each sample entered in the CMIBS geochemical database")
    field_ID: str = Field(..., description="Field identifiers assigned by the sample collector of samples submitted for analysis")
    lab_ID: str = Field(..., description="Laboratory batch identifiers assigned by the Sample Control Officers of the analytical laboratories that received the samples as batches")
    job_ID: str = Field(..., description="Unique identifiers assigned to submitted samples by the Sample Control Officer of the analytical laboratory that received the samples")
    submitter: str = Field(..., description="Names of the individuals who submitted samples in batches to the laboratories for analysis")
    project_name: str = Field(..., description="Project names, at times derived from project account numbers, of work groups funded for the collection and analysis of submitted samples")
    #date_submitted: datetime = Field(..., description="MM/DD/YYYY Date sample was submitted to Sample Control for initial database processing prior to sample prep and analysis; "
                                                      #"or date sample and its data were added to the database from non-USGS sources")

class BestVal_Mineral(BaseModel):
    """Values of mineral concentrations"""

    CMIBS_ID: int = Field(...,description="Unique identifier assigned to each sample entered in the CMIBS geochemical database")
    mineral_ppm: float = Field(..., description="Parts per million of target mineral for best model")
    mineral_ppm_all: float = Field(..., description="Parts per million of target mineral for all models")
    mineral_pct: float = Field(..., description="Best value of target mineral in weight percent")
    mineral_pct_all: float = Field(..., description="All values of target mineral in weight percent")
    mineral_AM: AnalyticModel

class BestVal_RockMaj(BaseModel):
    """Table of "best value" chemical "whole rock" major element data for rock, sediment, soil and organic samples"""

    CMIBS_ID: int = Field(..., description="Unique identifier assigned to each sample entered in the CMIBS geochemical database")
    wr_qual: int = Field(..., description="Qualifier for whole rock analysis, from 1 to 6, where 1 is the most precise "
                                          "analytical method package with the best sample digestion, and 6 is the least")
    wr_def: str = Field(..., description="Definition of qualifier for whole rock analysis")
    mineral_pct: float = Field(..., description="Best value in weight percent of whole rock majority")
    mineral_pct_all: float = Field(..., description="All values in weight percent of whole rock majority")
    mineral_pct_AM:AnalyticModel

class CMIBS_samples(BaseModel):
    CMIBS_ID: int = Field(...,
                          description="Unique identifier assigned to each sample entered in the CMIBS geochemical database")
    geometry: Point =  Field(...,
                          description="MapPoint layer")
    crs: WKT = Field(
        ...,
        description="Coordinate reference system of the tile scheme",
        # default="EPSG:3857 (Web Mercator)",
        )
    sampel_mineraldata: BestVal_Mineral
    sample_rockmajority: BestVal_RockMaj
    sample_geologydata: Geology

