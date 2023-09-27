# Map

*Basic information about the extracted map.*

### Properties

- **`name`** *(string)*: Map name.
- **`source_url`** *(string)*: URL of the map source (e.g., NGMDB information page).
- **`image_url`** *(string)*: URL of the map image, as a web-accessible, cloud-optimized GeoTIFF.
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
- **`projection_info`**: Refer to *[ProjectionMeta](#ProjectionMeta)*.

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
- **`image`**: Image of the cross section.

## ExtractionIdentifier

*Link to extracted model*

### Properties

- **`model`** *(string)*: Model name.
- **`id`** *(integer)*: ID of the extracted feature.
- **`field`** *(string)*: Field name of the model.

## GroundControlPoint

*Ground control point*

### Properties

- **`id`** *(integer)*: Internal ID.
- **`map_geom`**: Point geometry.
- **`px_geom`**: Point geometry.

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
- **`direction`**: Line direction.
  - **Any of**
    - *integer*
    - *null*

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
- **`type`** *(string)*: Name of this line type.

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

## MapUnit

### Properties

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
- **`id`** *(integer)*: Internal ID.
- **`name`** *(string)*: Geologic unit name extracted from legend.
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
- **`lithology`** *(array)*: Lithology information extracted from legend.
  - **Items** *(string)*
- **`comments`**: Comments extracted from legend.
  - **Any of**
    - *string*
    - *null*
- **`category`**: Name of containing legend block.
  - **Any of**
    - *string*
    - *null*

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
- **`type`** *(string)*: Name of this point type.

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
- **`map_unit`**: Map unit information.
  - **All of**
    - : Refer to *[MapUnit](#MapUnit)*.

## ProjectionMeta

*Information about the map projection. Projection information should also be applied
to the map image and output vector data (if using GeoPackage output format).*

### Properties

- **`gcps`** *(array)*: Ground control points.
  - **Items**: Refer to *[GroundControlPoint](#GroundControlPoint)*.
- **`projection`** *(string)*: Map projection information.

