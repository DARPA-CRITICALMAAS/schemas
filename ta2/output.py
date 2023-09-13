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


class Importance(Enum):
    Primary = "Primary"
    Secondary = "Secondary"
    Accessory = "Accessory"


class OccurrenceType(Enum):
    Prospect = "Prospect"
    Occurrence = "Occurrence"
    Deposit = "Deposit"


class MineralSpecies(BaseModel):
    """A mineral or elemental species of interest"""

    name: str
    mindat_id: str | None
    formula: str | None
    metallic: bool = Field(description="Is this a metallic mineral/element?")


class Commodity(BaseModel):
    """A mineral or elemental commodity, with information about its importance in a deposit."""

    species: MineralSpecies | str = Field(
        description="Species of interest (mineral, element, or other commodity)",
        examples=["quartz", "gold", "silver", "copper", "lead", "zinc", "aggregate"],
    )
    is_ore: bool = Field(
        description="Is this an ore or gangue mineral in this deposit?"
    )
    importance: Importance = Field(
        description="Importance of this mineral in this deposit"
    )


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


class MineralDepositModel(BaseModel):
    deposit_type: str
    GeoEnv_age_range: list[str] | None
    GeoEnv_rock_types: list[str] | None
    GeoEnv_textures: list[str] | None
    GeoEnv_dep_env: list[str] | None
    GeoEnv_tectonic_settings: list[str] | None
    DepDesc_ore_controls: list[str] | None
    DepDesc_alteration: list[str] | None
    DepDesc_mineralogy: list[str] | None
    DepDesc_geo_signature: list[str] | None
    DepDesc_texture_structure: list[str] | None


class ResourceDevelopmentLevel(Enum):
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


class CommodityWithConcentration(BaseModel):
    material: Commodity = Field(description="Species of interest (mineral or element)")
    concentration: float = Field(description="Concentration of species in ppm")
    unit: ConcentrationUnit = Field(description="Unit of concentration")


class GradeTonnageModel(BaseModel):
    ore_quantity: float = Field(description="Ore quantity in metric tons")
    materials: list[CommodityWithConcentration]
    level: ResourceDevelopmentLevel = Field(description="Type of resource")


class MineralOccurrence(BaseModel):
    """A mineral resource site, based on MRDS."""

    id: int
    mrds_id: str | None
    mrds_url: str | None
    type: OccurrenceType
    area_name: str | None
    commodities: list[Commodity]
    location: Optional[Point | Polygon]
    history: History | None
    reporter: str | None
    score: Score
    sources: list[Document]
    geologic_unit: GeologicUnit
    # Note: we could associate grade/tonnage information with deposits if it is desireable
    # production_info: list[GradeTonnageModel] | None


# Schemas can conform to other ones by inheriting from them or by declaring conformance
# with the `conforms_to` attribute. This is useful for schemas that are not directly loaded
# into the database, but are used to validate other schemas.

class Reference(BaseModel):
    doc: Document
    text: list[str]
    coords: list[int] | None

class MappableCriteria(BaseModel):
    info: str
    potential_dataset: str | None
    supporting_references: list[Reference]

class Criteria(BaseModel):
    theoretical: str
    mappable: list[MappableCriteria]

class MineralSystem(BaseModel):
    deposit_type: str
    trigger: list[Criteria]
    source: list[Criteria]
    conduit: list[Criteria]
    driver: list[Criteria]
    throttle: list[Criteria]
    trap: list[Criteria]
    dispersion: list[Criteria]
    exhumation: list[Criteria]
    direct_detection: list[Criteria]
