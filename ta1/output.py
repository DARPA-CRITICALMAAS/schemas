from pydantic import BaseModel, Field
from typing import Optional, TypeVar
from enum import Enum

Polygon = TypeVar("Polygon")
Line = TypeVar("Line")
Point = TypeVar("Point")
WKT = TypeVar("WKT", bound=str)

PixelBoundingPolygon = TypeVar("PixelBoundingPolygon")


class GeologicUnit(BaseModel):
    """
    Information about a geologic unit synthesized from map legend extractions.
    """
    name: str = Field(..., description="Geologic unit name extracted from legend")
    description: str = Field(
        ..., description="Map unit description"
    )
    comments: Optional[str] = Field(..., description="Map unit comments")

    age_text: str = Field(
        ..., description="Text representation of age extracted from legend"
    )
    t_interval: Optional[str | int] = Field(
        ..., description="Youngest interval", examples=["Holocene", "Cretaceous"]
    )
    b_interval: Optional[str | int] = Field(
        ..., description="Oldest interval", examples=["Mesozoic", "Neoproterozoic"]
    )
    t_age: Optional[int] = Field(..., description="Minimum age (in Ma)")
    b_age: Optional[int] = Field(..., description="Maximum age (in Ma)")
    lithology: list[str] = Field(
        ..., description="Structured lithology information extracted from legend."
    )


class PolygonTypeName(Enum):
    geologic_unit = "geologic unit"
    tailings = "tailings"
    outcrop = "outcrop"
    water = "body of water"
    other = "other"
    unknown = "unknown"

class PolygonType(BaseModel):
    """Information about a polygon extracted from the map legend."""

    id: int = Field(..., description="Internal ID")
    name: PolygonTypeName = Field(..., description="Type of feature")

    color: str = Field(..., description="Color extracted from map/legend")
    pattern: Optional[str] = Field(..., description="Pattern extracted from map/legend")
    abbreviation: Optional[str] = Field(
        ..., description="Abbreviation extracted from map/legend"
    )
    description: Optional[str] = Field(
        ..., description="Description text extracted from legend"
    )
    category: Optional[str] = Field(..., description="Name of containing legend block")
    map_unit: Optional[GeologicUnit] = Field(..., description="Map unit information")



class PolygonFeature(BaseModel):
    """Polygon containing map unit information."""

    id: int = Field(..., description="Internal ID")

    geometry: Polygon = Field(..., description="Polygon geometry")
    type: PolygonType = Field(..., description="Polygon type information")

class LineTypeName(Enum):
    anticline = "anticline"
    antiform = "antiform"
    normal_fault = "normal fault"
    reverse_fault = "reverse fault"
    thrust_fault = "thrust fault"
    left_lateral_strike_slip_fault = "left-lateral strike-slip fault"
    right_lateral_strike_slip_fault = "right-lateral strike-slip fault"
    strike_slip_fault = "strike-slip fault"
    fault = "fault"
    lineament = "lineament"
    scarp = "scarp"
    syncline = "syncline"
    synform = "synform"
    bed = "bed"
    crater = "crater"
    caldera = "caldera"
    dike = "dike"
    escarpment = "escarpment"
    fold = "fold"
    other = "other"
    unknown = "unknown"

class LinePolarity(Enum):
    """
    Positive: ticks are to right of line/directed towards endpoint
    Negative: ticks are to left of line/directed away from endpoint"""
    positive = 1
    negative = -1
    undirected = 0

class LineType(BaseModel):
    """Line type information."""

    id: int = Field(..., description="Internal ID")

    name: LineTypeName = Field(
        ...,
        description="Name of this line type",
        examples=["contact", "normal fault", "thrust fault"],
    )
    description: Optional[str] = Field(..., description="Description")
    dash_pattern: Optional[str] = Field(..., description="Dash pattern description")
    symbol: Optional[str] = Field(..., description="Symbol description")


class LineFeature(BaseModel):
    """Line containing map unit information."""

    id: int = Field(..., description="Internal ID")

    geometry: Line = Field(..., description="Line geometry")
    name: Optional[str] = Field(
        ..., description="Name of this map feature", examples=["San Andreas Fault"]
    )

    type: LineType = Field(..., description="Line type")
    direction: LinePolarity = Field(
        ..., description="Line polarity", examples=[1, -1]
    )


class PointTypeName(Enum):
    bedding = "bedding"
    foliation = "foliation"
    lineation = "lineation"
    joint = "joint"
    fault = "fault"
    fracture = "fracture"
    fold_axis = "fold axis"
    sample_location = "sample location"
    outcrop = "outcrop"
    mine_site = "mine site"
    contact = "contact"
    cleavage = "cleavage"
    other = "other"
    unknown = "unknown"

class PointType(BaseModel):
    """Point type information."""

    id: int = Field(..., description="Internal ID")
    name: PointTypeName = Field(
        ...,
        description="Name of this point type",
        examples=["outcrop", "borehole", "geochron", "strike/dip"],
    )
    description: Optional[str] = Field(..., description="Description")


class PointFeature(BaseModel):
    """Point for map measurement"""

    id: int = Field(..., description="Internal ID")
    type: PointType = Field(..., description="Point type")
    geometry: Point = Field(..., description="Point geometry")
    dip_direction: Optional[float] = Field(..., description="Dip direction")
    dip: Optional[float] = Field(..., description="Dip")


class MapFeatureExtractions(BaseModel):
    """Extractions from a map used to estimate features"""

    polygons: list[PolygonFeature] = Field(..., description="Map polygons")
    lines: list[LineFeature] = Field(..., description="Map lines")
    points: list[PointFeature] = Field(..., description="Map points")


class ExtractionIdentifier(BaseModel):
    """Link to extracted model"""

    model: str = Field(
        ...,
        description="Model name",
        example=[
            "PolygonFeature",
            "LineFeature",
            "PointFeature",
            "MapUnit",
            "LineType",
            "PointType",
        ],
    )
    id: int = Field(..., description="ID of the extracted feature")
    field: str = Field(..., description="Field name of the model")


class ConfidenceScale(BaseModel):
    """Confidence measure for a map extraction"""

    name: str = Field(..., description="Name of the confidence scale")
    description: str = Field(..., description="Description of the confidence scale")
    min_value: float = Field(..., description="Minimum value")
    max_value: float = Field(..., description="Maximum value")


class ConfidenceEstimation(BaseModel):
    """Confidence information for a map extraction"""

    model: ExtractionIdentifier
    scale: ConfidenceScale
    confidence: float = Field(..., description="Certainty")
    extra_data: dict = Field(..., description="Additional data")


class PageExtraction(BaseModel):
    """Extractions from a page used to estimate features"""

    name: str = Field(
        ..., description="Name of the page extraction object", example=["Legend"]
    )
    ocr_text: str = Field(..., description="OCR text of the page extraction")
    color_estimation: Optional[str]
    bounds: PixelBoundingPolygon = Field(
        ..., description="Bounds of the page extraction, in pixel coordinates"
    )
    model: Optional[ExtractionIdentifier]

class System(BaseModel):
    """Information about a system (inference engine, HMI, and/or human)"""
    id: int = Field(..., description="Internal ID")
    system_name: str = Field(..., description="System name")
    version: str = Field(..., description="System version")

class GroundControlPoint(BaseModel):
    """Ground control point"""

    id: int = Field(..., description="Internal ID")
    map_geom: Point = Field(..., description="Point geometry")
    px_geom: Point = Field(..., description="Point geometry")
    system: System
    human_entered: bool = Field(..., description="Human entered")
    confidence: ConfidenceEstimation

class ProjectionMeta(BaseModel):
    """Information about the map projection. Projection information should also be applied
    to the map image and output vector data (if using GeoPackage output format)."""

    system: System
    timestamp: str = Field(..., description="Time of model run")
    gcps: list[GroundControlPoint] = Field(..., description="Ground control points")
    projection: WKT = Field(..., description="Map projection information")


class ModelRun(BaseModel):
    """Information about a model run."""

    pipeline_name: str = Field(..., description="Model name")
    version: str = Field(..., description="Model version")
    timestamp: str = Field(..., description="Time of model run")
    batch_id: Optional[str] = Field(..., description="Batch ID")
    confidence: list[ConfidenceEstimation]
    boxes: list[PageExtraction]


class CrossSection(BaseModel):
    """Information about a geological cross section (lines of section + images).

    NOTE: This would be nice to have but isn't required (especially for the initial target).
    """

    id: int = Field(..., description="Internal ID")
    label: str = Field(..., description="Cross section label")
    line_of_section: Line = Field(..., description="Geographic line of section")
    image: PixelBoundingPolygon = Field(..., description="Bounding pixel coordinates of the cross section")


class Map(BaseModel):
    """Basic information about the extracted map."""

    name: str = Field(..., description="Map name")
    source_url: str = Field(
        ..., description="URL of the map source (e.g., NGMDB information page)"
    )
    # A centralized map image store would simplify the work of debugging and re-running models.
    image_url: str = Field(
        ...,
        description="URL of the map image, as a web-accessible, cloud-optimized GeoTIFF",
    )
    image_size: list[int] = Field(..., description="Pixel size of the map image")

    authors: str = Field(..., description="Map authors")
    publisher: str = Field(..., description="Map publisher")
    year: int = Field(..., description="Map publication year")
    organization: str = Field(..., description="Map organization")
    scale: str = Field(..., description="Map scale")
    bounds: Polygon = Field(..., description="Map geographic bounds")

    features: MapFeatureExtractions
    cross_sections: Optional[list[CrossSection]]

    pipelines: list[ModelRun]
    projection_info: list[ProjectionMeta]
