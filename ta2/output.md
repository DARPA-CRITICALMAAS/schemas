# MineralSite

### Properties

- **`id`** *(string)*
- **`name`** *(string)*: Name of the mine, e.g., Tungsten Jim.
- **`mineral_inventory`** *(array)*
  - **Items**: Refer to *[MineralInventory](#MineralInventory)*.
- **`location_info`**: Refer to *[LocationInfo](#LocationInfo)*.
- **`geology_info`**: Refer to *[GeologyInfo](#GeologyInfo)*.
- **`same_as`**: Dictionary that stores the IDs point to other databases: e.g.: {"MRDS" : [{"dep_id" : "10289747","mrds_id" : "W018008",    "altername_or_previous_names": "Thompson Creek Tungsten Mine, Tungsten Jim Mine"    },    {"dep_id": "10022920",    "mrds_id":"FS00436",    "record_type":"Site"}  ],  "USMIN" : [  {"ftr_id":"Mf00576",  "site_id":"ID00055",  "ftr_name":"Tungsten Jim"},  {"ftr_id":"Mo00569",  "site_id":"ID00055"  }  ]}.
  - **Any of**
    - *object*
    - *null*

## BoundingBox

### Properties

- **`x_min`** *(number)*
- **`x_max`** *(number)*
- **`y_min`** *(number)*
- **`y_max`** *(number)*

## Commodity

### Properties

- **`id`** *(string)*
- **`name`** *(string)*

## DepositType

### Properties

- **`id`** *(string)*
- **`name`** *(string)*: Name of the deposit type.

## Document

### Properties

- **`id`** *(string)*
- **`title`** *(string)*: Title of the document.
- **`doi`**: doi of the document.
  - **Any of**
    - *string*
    - *null*
- **`uri`**: URI of the document, if it does not have a doi.
  - **Any of**
    - *string*
    - *null*
- **`authors`** *(array)*: list of the authors of the document.
  - **Items** *(string)*
- **`journal`**: journal document belongs to.
  - **Any of**
    - *string*
    - *null*
- **`year`** *(integer)*: Published year of the document.
- **`month`** *(integer)*: Published month of the document.
- **`volume`**: Volume of the document.
  - **Any of**
    - *integer*
    - *null*
- **`issue`**: Issue number of the document.
  - **Any of**
    - *integer*
    - *null*
- **`description`** *(string)*: Description of the document.

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
- **`location_source`** *(string)*: Source dataset that the location info is retrieved from. e.g., MRDS.
- **`crs`** *(string)*: The Coordinate Reference System (CRS) of the location.
- **`country`** *(string)*: Country that the mine site resides in.
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
    - *string*
    - *null*
- **`supporting_references`** *(array)*
  - **Items**: Refer to *[Reference](#Reference)*.

## MineralInventory

### Properties

- **`id`** *(string)*
- **`deposit_type`**: The deposit type of an inventory item.
  - **Any of**
    - : Refer to *[DepositType](#DepositType)*.
    - *null*
- **`commodity`**: The commodity of an inventory item.
  - **All of**
    - : Refer to *[Commodity](#Commodity)*.
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
- **`containedMetal`**: The quantity of a contained metal in an inventory item.
  - **Any of**
    - *number*
    - *null*
- **`reference`**: The reference of an inventory item.
  - **Any of**
    - : Refer to *[Reference](#Reference)*.
    - *null*
- **`date`**: When in the point of time mineral inventory valid.
  - **Any of**
    - *string, format: date-time*
    - *null*

## MineralSystem

### Properties

- **`deposit_type`**: Refer to *[DepositType](#DepositType)*.
- **`trigger`** *(array)*
  - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
- **`source_fluid`** *(array)*
  - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
- **`source_ligand`** *(array)*
  - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
- **`source_metal`** *(array)*
  - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
- **`source_other`** *(array)*
  - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
- **`conduit`** *(array)*
  - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
- **`driver`** *(array)*
  - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
- **`throttle`** *(array)*
  - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
- **`trap`** *(array)*
  - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
- **`dispersion`** *(array)*
  - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
- **`exhumation`** *(array)*
  - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.
- **`direct_detection`** *(array)*
  - **Items**: Refer to *[MappableCriteria](#MappableCriteria)*.

## Ore

### Properties

- **`ore_unit`** *(string)*: The unit in which ore quantity is measured, eg, metric tonnes.
- **`ore_value`** *(number)*: The value of ore quantity.

## Reference

### Properties

- **`id`** *(string)*
- **`document`**: Refer to *[Document](#Document)*.
- **`page`** *(integer)*
- **`bounding_box`** *(array)*: coordinates of the document where reference is found.
  - **Items**: Refer to *[BoundingBox](#BoundingBox)*.

