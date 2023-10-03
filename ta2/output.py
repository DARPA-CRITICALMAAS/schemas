import erdantic as erd
from datetime import datetime
from enum import Enum
from typing import List, Optional, TypeVar

from pydantic import BaseModel, Field

from json import dumps
from jsonschema2md import Parser

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

class GeologyInfo(BaseModel):
    age: Optional[str] = Field(description = "Age of the geologic unit or event")
    unit_name: Optional[str] = Field(description = "Name of the geologic unit")
    description: Optional[str]
    lithology: Optional[list[str]]
    process: Optional[list[str]]
    environment: Optional[list[str]]
    comments: Optional[str]

class Ore(BaseModel):
    oreUnit: str = Field( description="The unit in which ore quantity is measured, eg, metric tonnes")
    oreValue: float = Field( description="The value of ore quantity")



class DepositType(BaseModel):
    id: str
    name: str = Field( description="Name of the deposit type")

class BoundingBox(BaseModel):
    x_min: float
    x_max: float
    y_min: float
    y_max: float
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
    bounding_box: list[BoundingBox] = Field(description="coordinates of the document where reference is found")

class MappableCriteria(BaseModel):
    criteria: str
    theoretical: Optional[str]
    potential_dataset: Optional[str]
    supporting_references: list[Reference]

class MineralSystem(BaseModel):
    deposit_type: str
    trigger: list[MappableCriteria]
    source_fluid: list[MappableCriteria]
    source_ligand: list[MappableCriteria]
    source_metal: list[MappableCriteria]
    source_other: list[MappableCriteria]
    conduit: list[MappableCriteria]
    driver: list[MappableCriteria]
    throttle: list[MappableCriteria]
    trap: list[MappableCriteria]
    dispersion: list[MappableCriteria]
    exhumation: list[MappableCriteria]
    direct_detection: list[MappableCriteria]

class Commodity(BaseModel):
    id: str
    name: str

class Grade(BaseModel):
    gradeUnit: str = Field( description="The unit in which grade is measured, eg, percent")
    gradeValue: float = Field( description="The value of grade")

class MineralInventory(BaseModel):
    id: str
    depositType: Optional[DepositType] = Field( description="The deposit type of an inventory item")
    commodity: Commodity = Field( description="The commodity of an inventory item")
    category: Optional[ResourceReserveCategory] = Field( description="The category of an inventory item")
    ore: Optional[Ore] = Field( description="The ore of an inventory item")
    grade: Optional[Grade] = Field( description="The grade of an inventory item")
    containedMetal: Optional[float] = Field( description="The quantity of a contained metal in an inventory item")
    reference: Optional[Reference] = Field( description="The reference of an inventory item")
    date: Optional[datetime] = Field(description="When in the point of time mineral inventory valid")



class LocationInfo(BaseModel):
    location: Geometry = Field(
        description="Type: Polygon or Point, value indicates the geolocation of the site"
    )
    location_source: str = Field(description = "Source dataset that the location info is retrieved from. e.g., MRDS")
    crs: str = Field(description = 'The Coordinate Reference System (CRS) of the location')
    country: str = Field( description = "Country that the mine site resides in")
    state_or_province: Optional[str] = Field(description = "State or province that the mine site resides in")

class GeologyInfo(BaseModel):
    age: Optional[str] = Field(description = "Age of the geologic unit or event")
    unit_name: Optional[str] = Field(description = "Name of the geologic unit")
    description: Optional[str]
    lithology: Optional[list[str]]
    process: Optional[list[str]]
    environment: Optional[list[str]]
    comments: Optional[str]



class MineralSite(BaseModel):
    id: str
    name: str = Field(description = "Name of the mine, e.g., Tungsten Jim")
    mineral_inventory: list[MineralInventory]
    location_info: LocationInfo
    geology_info: GeologyInfo

    same_as: Optional[dict] = Field(
        description='Dictionary that stores the IDs point to other databases: e.g.: {"MRDS" : [{"dep_id" : "10289747","mrds_id" : "W018008",    "altername_or_previous_names": "Thompson Creek Tungsten Mine, Tungsten Jim Mine"    },    {"dep_id": "10022920",    "mrds_id":"FS00436",    "record_type":"Site"}  ],  "USMIN" : [  {"ftr_id":"Mf00576",  "site_id":"ID00055",  "ftr_name":"Tungsten Jim"},  {"ftr_id":"Mo00569",  "site_id":"ID00055"  }  ]}'
    )


# Schemas can conform to other ones by inheriting from them or by declaring conformance
# with the `conforms_to` attribute. This is useful for schemas that are not directly loaded
# into the database, but are used to validate other schemas.



graph = erd.create(MineralSystem, MineralSite)

name = "output"
# Easy one-liner
graph.draw(out=name + ".png")

schema = MineralSite.model_json_schema()

schema_mineral_system = MineralSystem.model_json_schema()


with open(name + ".json", "w") as f:
    f.write(dumps([schema, schema_mineral_system], indent=2))

parser = Parser(
    examples_as_yaml=False,
)

md_lines = []

sub_models = [d.model for d in graph.models if d.model is not MineralSite]

models = [MineralSite] + sub_models

for d in models:
    schema = d.model_json_schema()
    lines = parser.parse_schema(schema)
    md_lines.extend(lines)
    md_lines.append("\n")

text = "".join(md_lines).replace("#/$defs/", "").replace("#$defs/", "#")
# Move headers down a level
text = text.replace("\n#", "\n##")

with open(name + ".md", "w") as f:
    f.write(text)

    same_as: Optional[dict] = Field(
        description='Dictionary that stores the IDs point to other databases: e.g.: {"MRDS" : [{"dep_id" : "10289747","mrds_id" : "W018008",    "altername_or_previous_names": "Thompson Creek Tungsten Mine, Tungsten Jim Mine"    },    {"dep_id": "10022920",    "mrds_id":"FS00436",    "record_type":"Site"}  ],  "USMIN" : [  {"ftr_id":"Mf00576",  "site_id":"ID00055",  "ftr_name":"Tungsten Jim"},  {"ftr_id":"Mo00569",  "site_id":"ID00055"  }  ]}'
    )
