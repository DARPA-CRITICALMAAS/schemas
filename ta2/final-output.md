# MineralSite

### Properties

- **`id`** *(string)*
- **`name`** *(string)*: Name of the mine, e.g., Tungsten Jim.
- **`mineral_inventory`**: Refer to *[MineralInventory](#MineralInventory)*.
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

- **`gradeUnit`** *(string)*: The unit in which grade is measured, eg, percent.
- **`gradeValue`** *(number)*: The value of grade.

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

## MineralInventory

### Properties

- **`id`** *(string)*
- **`depositType`**: The deposit type of an inventory item.
  - **All of**
    - : Refer to *[DepositType](#DepositType)*.
- **`commodity`**: The commodity of an inventory item.
  - **All of**
    - : Refer to *[Commodity](#Commodity)*.
- **`category`**: The category of an inventory item.
  - **All of**
    - : Refer to *[ResourceReserveCategory](#ResourceReserveCategory)*.
- **`ore`**: The ore of an inventory item.
  - **All of**
    - : Refer to *[Ore](#Ore)*.
- **`grade`**: The grade of an inventory item.
  - **All of**
    - : Refer to *[Grade](#Grade)*.
- **`containedMetal`** *(number)*: The quantity of a contained metal in an inventory item.
- **`reference`**: The reference of an inventory item.
  - **All of**
    - : Refer to *[Reference](#Reference)*.
- **`date`** *(string, format: date-time)*: When in the point of time mineral inventory valid.

## Ore

### Properties

- **`oreUnit`** *(string)*: The unit in which ore quantity is measured, eg, metric tonnes.
- **`oreValue`** *(number)*: The value of ore quantity.

## Reference

### Properties

- **`id`** *(string)*
- **`document`**: Refer to *[Document](#Document)*.
- **`page`** *(integer)*
- **`bounding_box`**: coordinates of the document where reference is found.
  - **All of**
    - : Refer to *[BoundingBox](#BoundingBox)*.

