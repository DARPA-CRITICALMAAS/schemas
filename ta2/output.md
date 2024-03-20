# MineralSite

### Properties

- **`source_id`** *(string)*: Source dataset that the site info is retrieved from. e.g., MRDS.
- **`record_id`** *(string)*: Unique ID of the record that the info is retrieved from e.g., 10022920.
- **`name`**: Name of the mine, e.g., Tungsten Jim.
  - **Any of**
    - *string*
    - *null*
- **`mineral_inventory`** *(array)*
  - **Items**: Refer to *[MineralInventory](#MineralInventory)*.
- **`location_info`**: Refer to *[LocationInfo](#LocationInfo)*.
- **`geology_info`**
  - **Any of**
    - : Refer to *[GeologyInfo](#GeologyInfo)*.
    - *null*
- **`deposit_type_candidate`** *(array)*
  - **Items**: Refer to *[DepositTypeCandidate](#DepositTypeCandidate)*.

## BoundingBox

### Properties

- **`x_min`** *(number)*
- **`x_max`** *(number)*
- **`y_min`** *(number)*
- **`y_max`** *(number)*

## Commodity

### Properties

- **`name`** *(string)*

## DepositType

### Properties

- **`name`** *(string)*: Deposit type name.
- **`environment`** *(string)*: Deposit type environment.
- **`group`** *(string)*: Deposit type group.

## DepositTypeCandidate

### Properties

- **`observed_name`** *(string)*: Source dataset that the site info is retrieved from. e.g., MRDS.
- **`normalized_uri`**: The deposit type of an inventory item.
  - **All of**
    - : Refer to *[DepositType](#DepositType)*.
- **`confidence`** *(number)*: Score deposit type of an inventory item.
- **`source`** *(string)*: Source of the classification (automated model version / SME / etc...).

## Document

### Properties

- **`title`**: Title of the document.
  - **Any of**
    - *string*
    - *null*
- **`doi`**: doi of the document.
  - **Any of**
    - *string*
    - *null*
- **`uri`**: URI of the document, if it does not have a doi.
  - **Any of**
    - *string*
    - *null*
- **`authors`**: list of the authors of the document.
  - **Any of**
    - *array*
      - **Items** *(string)*
    - *null*
- **`journal`**: journal document belongs to.
  - **Any of**
    - *string*
    - *null*
- **`year`**: Published year of the document.
  - **Any of**
    - *integer*
    - *null*
- **`month`**: Published month of the document.
  - **Any of**
    - *integer*
    - *null*
- **`volume`**: Volume of the document.
  - **Any of**
    - *integer*
    - *null*
- **`issue`**: Issue number of the document.
  - **Any of**
    - *integer*
    - *null*
- **`description`**: Description of the document.
  - **Any of**
    - *string*
    - *null*

## EvidenceLayer

### Properties

- **`name`** *(string)*
- **`relevance_score`** *(number)*

## GeologyInfo

### Properties

- **`age`**: Age of the geologic unit or event.
  - **Any of**
    - *string*
    - *null*
- **`unit_name`**: Name of the geologic unit.
  - **Any of**
    - *string*
    - *null*
- **`description`**
  - **Any of**
    - *string*
    - *null*
- **`lithology`**
  - **Any of**
    - *array*
      - **Items** *(string)*
    - *null*
- **`process`**
  - **Any of**
    - *array*
      - **Items** *(string)*
    - *null*
- **`environment`**
  - **Any of**
    - *array*
      - **Items** *(string)*
    - *null*
- **`comments`**
  - **Any of**
    - *string*
    - *null*

## Grade

### Properties

- **`grade_unit`** *(string)*: The unit in which grade is measured, eg, percent.
- **`grade_value`** *(number)*: The value of grade.

## LocationInfo

### Properties

- **`location`**: Type: Polygon or Point, value indicates the geolocation of the site.
- **`crs`** *(string)*: The Coordinate Reference System (CRS) of the location.
- **`country`**: Country that the mine site resides in.
  - **Any of**
    - *string*
    - *null*
- **`state_or_province`**: State or province that the mine site resides in.
  - **Any of**
    - *string*
    - *null*

## MappableCriteria

### Properties

- **`criteria`** *(string)*
- **`theoretical`**
  - **Any of**
    - *string*
    - *null*
- **`potential_dataset`**
  - **Any of**
    - *array*
      - **Items**: Refer to *[EvidenceLayer](#EvidenceLayer)*.
    - *null*
- **`supporting_references`** *(array)*
  - **Items**: Refer to *[Reference](#Reference)*.

## MineralInventory

### Properties

- **`commodity`**: The commodity of an inventory item.
  - **All of**
    - : Refer to *[Commodity](#Commodity)*.
- **`observed_commodity`**: The observed commodity in the source data (textual format).
  - **Any of**
    - *string*
    - *null*
- **`category`**: The category of an inventory item.
  - **Any of**
    - : Refer to *[ResourceReserveCategory](#ResourceReserveCategory)*.
    - *null*
- **`ore`**: The ore of an inventory item.
  - **Any of**
    - : Refer to *[Ore](#Ore)*.
    - *null*
- **`grade`**: The grade of an inventory item.
  - **Any of**
    - : Refer to *[Grade](#Grade)*.
    - *null*
- **`cutoff_grade`**: The cutoff grade of the observed inventory item.
  - **Any of**
    - : Refer to *[Grade](#Grade)*.
    - *null*
- **`contained_metal`**: The quantity of a contained metal in an inventory item.
  - **Any of**
    - *number*
    - *null*
- **`reference`**: The reference of an inventory item.
  - **All of**
    - : Refer to *[Reference](#Reference)*.
- **`date`**: When in the point of time mineral inventory valid.
  - **Any of**
    - *string, format: date-time*
    - *null*
- **`zone`**: zone of mineral site where inventory item was discovered.
  - **Any of**
    - *string*
    - *null*

## MineralSystem

### Properties

- **`deposit_type`** *(array)*
  - **Items**: Refer to *[DepositType](#DepositType)*.
- **`source`** *(array)*
  - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
- **`pathway`** *(array)*
  - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
- **`trap`**
  - **Any of**
    - *array*
      - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
    - *null*
- **`preservation`**
  - **Any of**
    - *array*
      - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
    - *null*
- **`energy`**
  - **Any of**
    - *array*
      - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
    - *null*
- **`outflow`**
  - **Any of**
    - *array*
      - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
    - *null*

## Ore

### Properties

- **`ore_unit`** *(string)*: The unit in which ore quantity is measured, eg, metric tonnes.
- **`ore_value`** *(number)*: The value of ore quantity.

## PageInfo

### Properties

- **`page`** *(integer)*
- **`bounding_box`**: Coordinates of the document where reference is found.
  - **Any of**
    - : Refer to *[BoundingBox](#BoundingBox)*.
    - *null*

## Reference

### Properties

- **`document`**: Refer to *[Document](#Document)*.
- **`page_info`** *(array)*: List of pages and their respective bounding boxes where the reference is found.
  - **Items**: Refer to *[PageInfo](#PageInfo)*.

