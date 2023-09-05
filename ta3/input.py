"""
Schemas for TA3 data input from TA4
"""
from pydantic import BaseModel, Field
from typing import Optional, TypeVar

Polygon = TypeVar("Polygon")
Line = TypeVar("Line")
Point = TypeVar("Point")
WKT = TypeVar("WKT", bound=str)


class BoundaryAge(BaseModel):
    """Bounding age of a map unit"""

    age: int = Field(..., description="Age in Ma, if known")
    interval: str = Field(
        ..., description="Age interval name", examples=["Holocene", "Cretaceous"]
    )
    interval_id: int = Field(
        ..., description="Age interval ID, from Macrostrat", examples=[1, 2]
    )


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


class MapPolygon(BaseModel):
    """Macrostrat proposal for geologic mapping output schema.
    This is fairly similar to the existing output of Macrostrat's tile-based
    geological map services, with several changes:

    - Allowance for more specific/harmonized lithological information
    - Normalization for clarity
    """

    id: int = Field(..., description="Internal ID of the map unit")
    geometry: Polygon = Field(..., description="Geometry of this feature")
    age: str = Field(..., description="Geologic age of the map unit, from source map")
    t_age: BoundaryAge = Field(..., description="Upper age of the map unit")
    b_age: BoundaryAge = Field(..., description="Lower age of the map unit")
    legend_id: int = Field(..., description="ID of the map legend block")
    lithology: list[str] = Field(..., description="Lithology descriptions")
    description: str = Field(..., description="Description of the map unit")
    comments: str = Field(..., description="Comments")
    name: str = Field(..., description="Name of the map unit")
    color: Optional[str] = Field(
        ..., description="Color of the map unit, on the original map"
    )
    pattern: Optional[str] = Field(
        ..., description="FGDC pattern of the map unit, if any"
    )
    source: Map = Field(..., description="Source map of the map unit")


class MapLine(BaseModel):
    id: int = Field(..., description="Internal ID of the line")
    geometry: Line = Field(..., description="Geometry of this feature")
    description: str = Field(..., description="Description of the line")
    name: Optional[str] = Field(..., description="Name of the line")
    type: str = Field(..., description="Type of the line")
    name: Optional[str] = Field(
        ..., description="Name of the line", examples=["San Andreas Fault"]
    )
    direction: int = Field(..., description="Direction of the line", examples=[1, -1])
    source: Map = Field(..., description="Source map of the line")


class MapPoint(BaseModel):
    id: int = Field(..., description="Internal ID of the point")
    geometry: Point = Field(..., description="Geometry of this feature")
    type: str = Field(
        ..., description="Type of the point", examples=["borehole", "bedding"]
    )
    name: Optional[str] = Field(..., description="Name of the point")
    dip: Optional[float] = Field(..., description="Dip of the point")
    dip_direction: Optional[float] = Field(..., description="Strike of the point")
    description: str = Field(..., description="Description of the point")
    source: Map = Field(..., description="Source map of the point")


class MapTile(BaseModel):
    """A tile representing geologic map information covering a small area."""

    x: int = Field(..., description="X coordinate of the tile")
    y: int = Field(..., description="Y coordinate of the tile")
    z: int = Field(..., description="Z coordinate of the tile")
    units: list[MapPolygon] = Field(..., description="Map units in the tile")
    lines: list[MapLine] = Field(..., description="Lines in the tile")
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
