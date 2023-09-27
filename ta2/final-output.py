import erdantic as erd
from datetime import datetime
from enum import Enum, auto
from typing import List, Optional

from typing import TypeVar
from pydantic import BaseModel, Field

Point = TypeVar("Point")
Polygon = TypeVar("Polygon")
Geometry = TypeVar("Geometry")


class ResourceReserveCategory(Enum):
    INFERRED = "inferred"
    INDICATED = "indicated"
    MEASURED = "measured"
    PROBABLE = "probable"
    PROVEN = "proven"
    ORIGINAL_RESOURCE = "original resource"
    EXTRACTED = "extracted"
    CUMULATIVE_EXTRACTED = "cumulative extracted"


class Ore(BaseModel):
    oreUnit: str = Field( description="The unit in which ore quantity is measured, eg, metric tonnes")
    oreValue: float = Field( description="The value of ore quantity")



class DepositType(BaseModel):
    id: str
    name: str = Field( description="Name of the deposit type")


class Document(BaseModel):
    id: str
    title: str = Field( description="Title of the document")
    doi: Optional[str] = Field(description="doi of the document")
    uri: Optional[str] = Field(description="URI of the document, if it does not have a doi")
    authors: list[str] = Field(description="list of the authors of the document")
    journal: Optional[str] = Field(description="journal document belongs to")
    year: int = Field(description="Published year of the document")
    month: int = Field(description="Published month of the document")
    volume: Optional[int] = Field(description="Volume of the document")
    issue: Optional[int] = Field(description="Issue number of the document")
    description: str = Field(description="Description of the document")



class Reference(BaseModel):
    id: str
    document: Document
    page: int
    coords: list[int] = Field(description="coordinates of the document where reference is found")


class Commodity(BaseModel):
    id: str
    name: str

class Grade(BaseModel):
    gradeUnit: str = Field( description="The unit in which grade is measured, eg, percent")
    gradeValue: float = Field( description="The value of grade")

class MineralInventory(BaseModel):
    id: str
    depositType: DepositType = Field( description="The deposit type of an inventory item")
    commodity: Commodity = Field( description="The commodity of an inventory item")
    category: ResourceReserveCategory = Field( description="The category of an inventory item")
    ore: Ore = Field( description="The ore of an inventory item")
    grade: Grade = Field( description="The grade of an inventory item")
    containedMetal: float = Field( description="The quantity of a contained metal in an inventory item")
    reference: Reference = Field( description="The reference of an inventory item")
    date: datetime = Field(description="When in the point of time mineral inventory valid")

class LocationInfo(BaseModel):
    location: Geometry = Field(
        description="Type: Polygon or Point, value indicates the geolocation of the site"
    )
    location_source: str = Field(description="Source dataset that the location info is retrieved from. e.g., MRDS")
    crs: str = Field(description='The Coordinate Reference System (CRS) of the location')
    country: str = Field( description="Country that the mine site resides in")
    state_or_province: Optional[str] = Field(description="State or province that the mine site resides in")



class MineralSite(BaseModel):
    id: str
    name: str = Field(description="Name of the mine, e.g., Tungsten Jim")
    mineral_inventory: MineralInventory
    location_info: LocationInfo

    same_as: Optional[dict] = Field(
        description='Dictionary that stores the IDs point to other databases: '
                    'e.g.: {"MRDS" : [{"dep_id" : "10289747","mrds_id" : "W018008",  '
                    '  "altername_or_previous_names": "Thompson Creek Tungsten Mine, Tungsten Jim Mine"    },'
                    '    {"dep_id": "10022920",    "mrds_id":"FS00436",    "record_type":"Site"}  ],'
                    '  "USMIN" : [  {"ftr_id":"Mf00576",  "site_id":"ID00055",  "ftr_name":"Tungsten Jim"},'
                    '  {"ftr_id":"Mo00569",  "site_id":"ID00055"  }  ]}'
    )
    
diagram2 = erd.create(MineralSite)

diagram2.draw("final-output.png")