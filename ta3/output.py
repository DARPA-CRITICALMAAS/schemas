"""
Schemas for TA3 data output from TA4
"""
from pydantic import BaseModel, Field
from typing import Optional, TypeVar

Polygon = TypeVar("Polygon")
Line = TypeVar("Line")
Point = TypeVar("Point")
WKT = TypeVar("WKT", bound=str)


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

class ModelRun(BaseModel):
    """Information about a model run."""

    pipeline_name: str = Field(..., description="Model name")
    version: str = Field(..., description="Model version")
    timestamp: str = Field(..., description="Time of model run")
    batch_id: Optional[str] = Field(..., description="Batch ID")
    image_size: list[int] = Field(..., description="Pixel size of the map image")
    confidence: list[ConfidenceEstimation]

class ProspectivityScore(BaseModel):
    uri: str = Field(..., description="URI of the output prospectivity score raster")

class ProspectivityUncertainty(BaseModel):
    uri: str = Field(..., description="URI of the output prospectivity uncertainty raster")

class ProspectivityModel(BaseModel):
    bounds: list[float] = Field(..., description="Bounding box of the tile scheme")
    crs: WKT = Field(
        ...,
        description="Coordinate reference system of the tile scheme",
        # default="EPSG:3857 (Web Mercator)",
    )
    resolution: float = Field(..., description="Resolution of the output prospectivity raster")

    pipelines: list[ModelRun]
    prospectivity_score: ProspectivityScore = Field(..., description="Prospectivity score raster")
    prospectivity_uncertainty: ProspectivityUncertainty = Field(..., description="Prospectivity uncertainty raster")
    feature_importance: list[dict] = Field(..., description="Feature importance")
