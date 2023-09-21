# ProspectivityModel

### Properties

- **`bounds`** *(array)*: Bounding box of the tile scheme.
  - **Items** *(number)*
- **`crs`** *(string)*: Coordinate reference system of the tile scheme.
- **`resolution`** *(number)*: Resolution of the output prospectivity raster.
- **`pipelines`** *(array)*
  - **Items**: Refer to *[ModelRun](#ModelRun)*.
- **`prospectivity_score`**: Prospectivity score raster.
  - **All of**
    - : Refer to *[ProspectivityScore](#ProspectivityScore)*.
- **`prospectivity_uncertainty`**: Prospectivity uncertainty raster.
  - **All of**
    - : Refer to *[ProspectivityUncertainty](#ProspectivityUncertainty)*.

## ConfidenceEstimation

*Confidence information for a map extraction*

### Properties

- **`model`**: Refer to *[ExtractionIdentifier](#ExtractionIdentifier)*.
- **`scale`**: Refer to *[ConfidenceScale](#ConfidenceScale)*.
- **`confidence`** *(number)*: Certainty.
- **`extra_data`** *(object)*: Additional data.

## ConfidenceScale

*Confidence measure for a map extraction*

### Properties

- **`name`** *(string)*: Name of the confidence scale.
- **`description`** *(string)*: Description of the confidence scale.
- **`min_value`** *(number)*: Minimum value.
- **`max_value`** *(number)*: Maximum value.

## ExtractionIdentifier

*Link to extracted model*

### Properties

- **`model`** *(string)*: Model name.
- **`id`** *(integer)*: ID of the extracted feature.
- **`field`** *(string)*: Field name of the model.

## ModelRun

*Information about a model run.*

### Properties

- **`pipeline_name`** *(string)*: Model name.
- **`version`** *(string)*: Model version.
- **`timestamp`** *(string)*: Time of model run.
- **`batch_id`**: Batch ID.
  - **Any of**
    - *string*
    - *null*
- **`image_size`** *(array)*: Pixel size of the map image.
  - **Items** *(integer)*
- **`confidence`** *(array)*
  - **Items**: Refer to *[ConfidenceEstimation](#ConfidenceEstimation)*.

## ProspectivityScore

### Properties

- **`uri`** *(string)*: URI of the output prospectivity score raster.

## ProspectivityUncertainty

### Properties

- **`uri`** *(string)*: URI of the output prospectivity uncertainty raster.

