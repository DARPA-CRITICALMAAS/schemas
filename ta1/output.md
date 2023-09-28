# Map

*Basic information about the extracted map.*

### Properties

- **`name`** *(string)*: Map name.
- **`source_url`** *(string)*: URL of the map source (e.g., NGMDB information page).
- **`image_url`** *(string)*: URL of the map image, as a web-accessible, cloud-optimized GeoTIFF.
- **`image_size`** *(array)*: Pixel size of the map image.
  - **Items** *(integer)*
- **`authors`** *(string)*: Map authors.
- **`publisher`** *(string)*: Map publisher.
- **`year`** *(integer)*: Map publication year.
- **`organization`** *(string)*: Map organization.
- **`scale`** *(string)*: Map scale.
- **`bounds`**: Map geographic bounds.
- **`features`**: Refer to *[MapFeatureExtractions](#MapFeatureExtractions)*.
- **`cross_sections`**
  - **Any of**
    - *array*
      - **Items**: Refer to *[CrossSection](#CrossSection)*.
    - *null*
- **`pipelines`** *(array)*
  - **Items**: Refer to *[ModelRun](#ModelRun)*.
- **`projection_info`** *(array)*
  - **Items**: Refer to *[ProjectionMeta](#ProjectionMeta)*.

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

## CrossSection

*Information about a geological cross section (lines of section + images).

NOTE: This would be nice to have but isn't required (especially for the initial target).*

### Properties

- **`id`** *(integer)*: Internal ID.
- **`label`** *(string)*: Cross section label.
- **`line_of_section`**: Geographic line of section.
- **`image`**: Bounding pixel coordinates of the cross section.

## ExtractionIdentifier

*Link to extracted model*

### Properties

- **`model`** *(string)*: Model name.
- **`id`** *(integer)*: ID of the extracted feature.
- **`field`** *(string)*: Field name of the model.

## GeologicUnit

*Information about a geologic unit synthesized from map legend extractions.*

### Properties

- **`name`** *(string)*: Geologic unit name extracted from legend.
- **`description`** *(string)*: Map unit description.
- **`comments`**: Map unit comments.
  - **Any of**
    - *string*
    - *null*
- **`age_text`** *(string)*: Text representation of age extracted from legend.
- **`t_interval`**: Youngest interval.
  - **Any of**
    - *string*
    - *integer*
    - *null*

  Examples:
  ```json
  "Holocene"
  ```

  ```json
  "Cretaceous"
  ```

- **`b_interval`**: Oldest interval.
  - **Any of**
    - *string*
    - *integer*
    - *null*

  Examples:
  ```json
  "Mesozoic"
  ```

  ```json
  "Neoproterozoic"
  ```

- **`t_age`**: Minimum age (in Ma).
  - **Any of**
    - *integer*
    - *null*
- **`b_age`**: Maximum age (in Ma).
  - **Any of**
    - *integer*
    - *null*
- **`lithology`** *(array)*: Structured lithology information extracted from legend.
  - **Items** *(string)*

## GroundControlPoint

*Ground control point*

### Properties

- **`id`** *(integer)*: Internal ID.
- **`map_geom`**: Point geometry.
- **`px_geom`**: Point geometry.
- **`system`**: Refer to *[System](#System)*.
- **`human_entered`** *(boolean)*: Human entered.
- **`confidence`**: Refer to *[ConfidenceEstimation](#ConfidenceEstimation)*.

## LineFeature

*Line containing map unit information.*

### Properties

- **`id`** *(integer)*: Internal ID.
- **`geometry`**: Line geometry.
- **`name`**: Name of this map feature.
  - **Any of**
    - *string*
    - *null*

  Examples:
  ```json
  "San Andreas Fault"
  ```

- **`type`**: Line type.
  - **All of**
    - : Refer to *[LineType](#LineType)*.
- **`direction`**: Line polarity.
  - **All of**
    - : Refer to *[LinePolarity](#LinePolarity)*.

  Examples:
  ```json
  1
  ```

  ```json
  -1
  ```


## LineType

*Line type information.*

### Properties

- **`id`** *(integer)*: Internal ID.
- **`name`**: Name of this line type.
  - **All of**
    - : Refer to *[LineTypeName](#LineTypeName)*.

  Examples:
  ```json
  "contact"
  ```

  ```json
  "normal fault"
  ```

  ```json
  "thrust fault"
  ```

- **`description`**: Description.
  - **Any of**
    - *string*
    - *null*
- **`dash_pattern`**: Dash pattern description.
  - **Any of**
    - *string*
    - *null*
- **`symbol`**: Symbol description.
  - **Any of**
    - *string*
    - *null*

## MapFeatureExtractions

*Extractions from a map used to estimate features*

### Properties

- **`polygons`** *(array)*: Map polygons.
  - **Items**: Refer to *[PolygonFeature](#PolygonFeature)*.
- **`lines`** *(array)*: Map lines.
  - **Items**: Refer to *[LineFeature](#LineFeature)*.
- **`points`** *(array)*: Map points.
  - **Items**: Refer to *[PointFeature](#PointFeature)*.

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
- **`confidence`** *(array)*
  - **Items**: Refer to *[ConfidenceEstimation](#ConfidenceEstimation)*.
- **`boxes`** *(array)*
  - **Items**: Refer to *[PageExtraction](#PageExtraction)*.

## PageExtraction

*Extractions from a page used to estimate features*

### Properties

- **`name`** *(string)*: Name of the page extraction object.
- **`ocr_text`** *(string)*: OCR text of the page extraction.
- **`color_estimation`**
  - **Any of**
    - *string*
    - *null*
- **`bounds`**: Bounds of the page extraction, in pixel coordinates.
- **`model`**
  - **Any of**
    - : Refer to *[ExtractionIdentifier](#ExtractionIdentifier)*.
    - *null*

## PointFeature

*Point for map measurement*

### Properties

- **`id`** *(integer)*: Internal ID.
- **`type`**: Point type.
  - **All of**
    - : Refer to *[PointType](#PointType)*.
- **`geometry`**: Point geometry.
- **`dip_direction`**: Dip direction.
  - **Any of**
    - *number*
    - *null*
- **`dip`**: Dip.
  - **Any of**
    - *number*
    - *null*

## PointType

*Point type information.*

### Properties

- **`id`** *(integer)*: Internal ID.
- **`name`**: Name of this point type.
  - **All of**
    - : Refer to *[PointTypeName](#PointTypeName)*.

  Examples:
  ```json
  "outcrop"
  ```

  ```json
  "borehole"
  ```

  ```json
  "geochron"
  ```

  ```json
  "strike/dip"
  ```

- **`description`**: Description.
  - **Any of**
    - *string*
    - *null*

## PolygonFeature

*Polygon containing map unit information.*

### Properties

- **`id`** *(integer)*: Internal ID.
- **`geometry`**: Polygon geometry.
- **`type`**: Polygon type information.
  - **All of**
    - : Refer to *[PolygonType](#PolygonType)*.

## PolygonType

*Information about a polygon extracted from the map legend.*

### Properties

- **`id`** *(integer)*: Internal ID.
- **`name`**: Type of feature.
  - **All of**
    - : Refer to *[PolygonTypeName](#PolygonTypeName)*.
- **`color`** *(string)*: Color extracted from map/legend.
- **`pattern`**: Pattern extracted from map/legend.
  - **Any of**
    - *string*
    - *null*
- **`abbreviation`**: Abbreviation extracted from map/legend.
  - **Any of**
    - *string*
    - *null*
- **`description`**: Description text extracted from legend.
  - **Any of**
    - *string*
    - *null*
- **`category`**: Name of containing legend block.
  - **Any of**
    - *string*
    - *null*
- **`map_unit`**: Map unit information.
  - **Any of**
    - : Refer to *[GeologicUnit](#GeologicUnit)*.
    - *null*

## ProjectionMeta

*Information about the map projection. Projection information should also be applied
to the map image and output vector data (if using GeoPackage output format).*

### Properties

- **`system`**: Refer to *[System](#System)*.
- **`timestamp`** *(string)*: Time of model run.
- **`gcps`** *(array)*: Ground control points.
  - **Items**: Refer to *[GroundControlPoint](#GroundControlPoint)*.
- **`projection`** *(string)*: Map projection information.

## System

*Information about a system (inference engine, HMI, and/or human)*

### Properties

- **`id`** *(integer)*: Internal ID.
- **`system_name`** *(string)*: System name.
- **`version`** *(string)*: System version.

