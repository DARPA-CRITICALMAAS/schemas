import erdantic as erd
from datetime import datetime
from enum import Enum, auto
from typing import List, Optional

from typing import TypeVar
from pydantic import BaseModel, Field

Point = TypeVar("Point")
Polygon = TypeVar("Polygon")
Geometry = TypeVar("Geometry")

class MineralSite(BaseModel):
    id: str
    name: str
    location: Geometry = Field(
        description="Type: Polygon or Point, value indicates the geolocation of the site"
    )
    crs: str = Field(
        description="The Coordinate Reference System (CRS) of the location"
    )
    country: str = Field( description = "Country that the mine site resides in")
    location_source: str = Field(description = "Source dataset that the location info is retrieved from. e.g., MRDS")
    state_or_province: Optional[str] = Field(description = "State or province that the mine site resides in")

    same_as: Optional[dict] = Field(
        description="Dictionary that stores the IDs point to other databases",
        examples={'MRDS':'dep_id:[10289747,10022920]', 'USMIN': 'ftr_id:[Mf00576,Mo00569]'},
    )

class ResourceReserveCategory(Enum):
    INFERRED = "inferred"
    INDICATED = "indicated"
    MEASURED = "measured"
    PROBABLE = "probable"
    PROVEN = "proven"
    ORIGINAL_RESOURCE = "original resource"
    EXTRACTED = "extracted"
    CUMULATIVE_EXTRACTED = "cumulative extracted"

class Country(BaseModel):
    id: str
    name: str = Field(
        description="Name of the country"
    )

class State(BaseModel):
    id: str
    name: str

class County(BaseModel):
    id: str
    name: str


class Ore(BaseModel):
    oreUnit: str
    oreValue: float



class DepositType(BaseModel):
    id: str
    name: str = Field( description = "Name of the deposit type")


class Document(BaseModel):
    id: str
    title: str = Field( description = "Title of the document")



class Reference(BaseModel):
    id: str
    document: Document
    date: datetime
    page: int
    line: int



class Commodity(BaseModel):
    id: str
    name: str



class Grade(BaseModel):
    gradeUnit: str
    gradeValue: float


class Metal(BaseModel):
    id: str
    name: str

class MineralInventory(BaseModel):
    id: str
    mine: MineralSite
    depositType: DepositType
    commodity: Commodity
    category: ResourceReserveCategory
    ore: Ore
    grade: Grade
    containedMetal: float
    reference: Reference


diagram2 = erd.create(MineralInventory)

diagram2.draw("final-output.png")