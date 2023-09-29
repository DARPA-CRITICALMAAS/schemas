# Dorthea's change

"""
Schemas for TA3 data output from TA4
"""
from pydantic import BaseModel, Field
from typing import Optional, TypeVar

Polygon = TypeVar("Polygon")
Line = TypeVar("Line")
Point = TypeVar("Point")
WKT = TypeVar("WKT", bound=str)


class Person(BaseModel):
    name: str = Field(..., description="Name of the person")
    email: str = Field(..., description="Email address of the person")
    org: str = Field(..., description="Organization of the person")


class DateTime(BaseModel):
    """Date and time in UTM"""

    year: int = Field(..., description="Year")
    month: int = Field(..., description="Month")
    day: int = Field(..., description="Day")
    hour: int = Field(..., description="Hour")
    minute: int = Field(..., description="Minute")
    second: int = Field(..., description="Second")


class DataDescription(BaseModel):
    """Description of the values this data represents"""

    datatype: str = Field(..., description="Datatype of this value")
    min: float = Field(..., description="Minimum value of this data")
    max: float = Field(..., description="Maximum value of this data")
    description: str = Field(..., description="Description of the meaning of this data")


class ModelRun(BaseModel):
    """Information about a model run."""

    name: str = Field(..., description="Model name")
    version: str = Field(..., description="Model version")
    description: str = Field(..., description="Description of the algorithm")
    uri: str = Field(..., description="URI of the model")
    references: list[str] = Field(..., description="References for the model")
    parameters: dict[str, str] = Field(..., description="Parameters used to run the model")


class RasterData(BaseModel):
    uri: str = Field(..., description="URI of the raster")
    raster_format: str = Field(
        ...,
        description="Raster format",
        examples=["GeoTIFF", "PNG", "JPEG", "JPEG2000", "HDF5", "NetCDF", "GeoPackage"],
    )
    band: int = Field(..., description="Band number in raster")
    value_description: DataDescription = Field(..., description="Description of the raster value")


class InputData(BaseModel):
    layer_names: list[str] = Field(..., description="Names of the input layers")
    layer_uris: list[str] = Field(..., description="URIs of the input layers")
    layer_bands: list[int] = Field(..., description="Band numbers of the input layer in the URI source")
    layer_descriptions: list[DataDescription] = Field(..., description="Description of the input layer values")
    layer_importances: list[float] = Field(..., description="Importance of the input layer")


class ProspectivityModel(BaseModel):
    bounds: list[float] = Field(..., description="Bounding box of the tile scheme")
    crs: WKT = Field(
        ...,
        description="Coordinate reference system of the tile scheme",
        # default="EPSG:3857 (Web Mercator)",
    )
    resolution: float = Field(..., description="Resolution of the output prospectivity raster")

    pipelines: ModelRun = Field(..., description="Information about the model run")
    prospectivity_score: RasterData = Field(..., description="Prospectivity score raster")
    prospectivity_uncertainty: RasterData = Field(..., description="Prospectivity uncertainty raster")
    prospectivity_confidence: RasterData = Field(..., description="Confidence in the prospectivity score")
    authors: list[Person] = Field(..., description="Authors of the model run")
    contact: Person = Field(..., description="Contact person for the model run")
    datetime_generated: DateTime = Field(..., description="Date and time the model was generated")
    input_data: InputData = Field(..., description="Input data used to generate the model")
