# ProspectivityModel

### Properties

- **`bounds`** *(array)*: Bounding box of the tile scheme.
  - **Items** *(number)*
- **`crs`** *(string)*: Coordinate reference system of the tile scheme.
- **`resolution`** *(number)*: Resolution of the output prospectivity raster.
- **`pipelines`**: Information about the model run.
  - **All of**
    - : Refer to *[ModelRun](#ModelRun)*.
- **`prospectivity_score`**: Prospectivity score raster.
  - **All of**
    - : Refer to *[RasterData](#RasterData)*.
- **`prospectivity_uncertainty`**: Prospectivity uncertainty raster.
  - **All of**
    - : Refer to *[RasterData](#RasterData)*.
- **`prospectivity_confidence`**: Confidence in the prospectivity score.
  - **All of**
    - : Refer to *[RasterData](#RasterData)*.
- **`authors`** *(array)*: Authors of the model run.
  - **Items**: Refer to *[Person](#Person)*.
- **`contact`**: Contact person for the model run.
  - **All of**
    - : Refer to *[Person](#Person)*.
- **`datetime_generated`**: Date and time the model was generated.
  - **All of**
    - : Refer to *[DateTime](#DateTime)*.
- **`input_data`**: Input data used to generate the model.
  - **All of**
    - : Refer to *[InputData](#InputData)*.

## DataDescription

*Description of the values this data represents*

### Properties

- **`datatype`** *(string)*: Datatype of this value.
- **`min`** *(number)*: Minimum value of this data.
- **`max`** *(number)*: Maximum value of this data.
- **`description`** *(string)*: Description of the meaning of this data.

## DateTime

*Date and time in UTM*

### Properties

- **`year`** *(integer)*: Year.
- **`month`** *(integer)*: Month.
- **`day`** *(integer)*: Day.
- **`hour`** *(integer)*: Hour.
- **`minute`** *(integer)*: Minute.
- **`second`** *(integer)*: Second.

## InputData

### Properties

- **`layer_names`** *(array)*: Names of the input layers.
  - **Items** *(string)*
- **`layer_uris`** *(array)*: URIs of the input layers.
  - **Items** *(string)*
- **`layer_bands`** *(array)*: Band numbers of the input layer in the URI source.
  - **Items** *(integer)*
- **`layer_descriptions`** *(array)*: Description of the input layer values.
  - **Items**: Refer to *[DataDescription](#DataDescription)*.
- **`layer_importances`** *(array)*: Importance of the input layer.
  - **Items** *(number)*

## ModelRun

*Information about a model run.*

### Properties

- **`name`** *(string)*: Model name.
- **`version`** *(string)*: Model version.
- **`description`** *(string)*: Description of the algorithm.
- **`uri`** *(string)*: URI of the model.
- **`references`** *(array)*: References for the model.
  - **Items** *(string)*
- **`parameters`** *(object)*: Parameters used to run the model. Can contain additional properties.
  - **Additional Properties** *(string)*

## Person

### Properties

- **`name`** *(string)*: Name of the person.
- **`email`** *(string)*: Email address of the person.
- **`org`** *(string)*: Organization of the person.

## RasterData

### Properties

- **`uri`** *(string)*: URI of the raster.
- **`raster_format`** *(string)*: Raster format.

  Examples:
  ```json
  "GeoTIFF"
  ```

  ```json
  "PNG"
  ```

  ```json
  "JPEG"
  ```

  ```json
  "JPEG2000"
  ```

  ```json
  "HDF5"
  ```

  ```json
  "NetCDF"
  ```

  ```json
  "GeoPackage"
  ```

- **`band`** *(integer)*: Band number in raster.
- **`value_description`**: Description of the raster value.
  - **All of**
    - : Refer to *[DataDescription](#DataDescription)*.

