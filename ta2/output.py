"""
Schemas for TA2 data output to TA3

This is a work in progress, borrowed from UW–Macrostrat's work to generate schemas
for MRDS data output:
https://dev.macrostrat.org/map/weaver
https://github.com/digitalcrust/weaver/blob/main/example-pipelines/mrds/02-get-data.py
"""
from enum import Enum
from typing import TypeVar, Optional
from pydantic import BaseModel, Field

Point = TypeVar("Point")
Polygon = TypeVar("Polygon")


class Score(Enum):
    """A score for the quality/completeness of a data source."""

    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"


class OccurrenceType(Enum):
    Prospect = "Prospect"
    Occurrence = "Occurrence"
    Deposit = "Deposit"


class Commodities(BaseModel):
    primary: list[str]
    secondary: list[str]
    accessory: list[str]
    metallic: bool
    nonmetallic: bool


class History(BaseModel):
    discovery_year: int | None
    production_years: str | None
    development_status: str | None
    operation_type: str | None


class Document(BaseModel):
    doi: str | None
    title: str | None
    authors: list[str]
    journal: str | None
    year: int | None
    volume: int | None
    issue: int | None
    description: str | None


class GeologicUnit(BaseModel):
    age: str
    name: str
    description: str
    lithology: list[str]
    environments: list[str]
    comments: str


class MineralOccurrence(BaseModel):
    """A mineral resource site, based on MRDS."""

    id: int
    mrds_id: str | None
    mrds_url: str | None
    type: OccurrenceType
    area_name: str | None
    ore_minerals: list[str]
    gangue_minerals: list[str]
    location: Optional[Point | Polygon]
    commodities: Commodities
    history: History | None
    reporter: str | None
    score: Score
    sources: list[Document]
    geologic_unit: GeologicUnit


# Schemas can conform to other ones by inheriting from them or by declaring conformance
# with the `conforms_to` attribute. This is useful for schemas that are not directly loaded
# into the database, but are used to validate other schemas.


class MineralDepositModel(BaseModel):
    ...  # TODO


class MineralResourceClassification(Enum):
    Inferred = "Inferred resources"
    Measured = "Measured resources"
    Proven = "Proven reserves"
    ProvenAndDeveloped = "Proven and developed resources"
    Production = "Cumulative production"


class ConcentrationUnit(Enum):
    ppm = "ppm"
    percentwt = "%wt"
    percentmol = "%mol"
    percent = "%"


class GradeInformation(BaseModel):
    species: str = Field(description="Species of interest (mineral or element)")
    concentration: float = Field(description="Concentration of species in ppm")
    unit: ConcentrationUnit = Field(description="Unit of concentration")


class GradeTonnageModel(BaseModel):
    ore_quantity: float = Field(description="Ore quantity in metric tons")
    grades: list[GradeInformation]
    type: MineralResourceClassification = Field(description="Type of resource")
