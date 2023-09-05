"""
Schemas for TA2 data output to TA3

This is a work in progress, borrowed from UW–Macrostrat's work to generate schemas
for MRDS data output:
https://dev.macrostrat.org/map/weaver
https://github.com/digitalcrust/weaver/blob/main/example-pipelines/mrds/02-get-data.py
"""
from enum import Enum
from typing import TypeVar
from pydantic import BaseModel, Field

Point = TypeVar("Point")


class Score(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"


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


class MineralResourceSite(BaseModel):
    """A mineral resource site from MRDS."""

    deposit_id: int
    mrds_id: str | None
    url: str
    area_name: str | None
    minerals: list[str]
    location: Point
    commodities: Commodities
    history: History
    reporter: str | None
    ref: str | None
    score: Score


# Schemas can conform to other ones by inheriting from them or by declaring conformance
# with the `conforms_to` attribute. This is useful for schemas that are not directly loaded
# into the database, but are used to validate other schemas.


class MineralDepositModel(BaseModel):
    ...  # TODO


class GradeAndTonnageModel(BaseModel):
    ...  # TODO
