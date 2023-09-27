# MineralSite

### Properties

- **`id`** *(string)*
- **`name`** *(string)*
- **`mineral_inventory`**: Refer to *[MineralInventory](#MineralInventory)*.
- **`location_info`**: Refer to *[LocationInfo](#LocationInfo)*.
- **`same_as`**
    - **Any of**
        - *dict*
        - *null*

## LocationInfo

### Properties

- **`location`** *(Geometry)*
- **`crs`** *(string)*
- **`country`** *(string)*
- **`location_source`** *(string)*
- **`state_or_province`**
    - **Any of**
        - *string*
        - *null*

## MineralInventory

*Mineral inventory data*

### Properties

- **`id`** *(integer)*
- **`depositType`**: Refer to *[DepositType](#DepositType)*.
- **`commodity`**: Refer to *[Commodity](#Commodity)*.
- **`category`**: Refer to *[ResourceReserveCategory](#ResourceReserveCategory)*.
- **`ore`**: Refer to *[Ore](#Ore)*.
- **`grade`**: Refer to *[Grade](#Grade)*.
- **`containedMetal`** *(float)*.
- **`reference`**: Refer to *[Reference](#Reference)*.
- **`date`** *(date)*.

## ResourceReserveCategory

### enum
- **`inferred`**
- **`indicated`**
- **`measured`**
- **`probable`**
- **`proven`**
- **`original resource`**
- **`extracted`**
- **`cumulative extracted`**


## Commodity

### Properties

- **`id`** *(string)*
- **`name`** *(string)*

## DepositType

### Properties

- **`id`** *(string)*
- **`name`** *(string)*

## Ore

### Properties

- **`oreUnit`** *(string)*
- **`oreValue`** *(float)*


## Grade

### Properties

- **`gradeUnit`** *(string)*
- **`gradeValue`** *(float)*

## Document

### Properties

- **`id`** *(string)*
- **`doi`** 
    - **Any of**
        - *string*
        - *null*
- **`uri`** 
  - **Any of**
    - *string*
    - *null*
- **`authors`** *(array)*
    - **Items** *(string)*
- **`journal`**
    - **Any of**
        - *string*
        - *null*
- **`year`** *(string)*
- **`month`** *(string)*
- **`volume`**
    - **Any of**
        - *integer*
        - *null*
- **`issue`**
    - **Any of**
        - *integer*
        - *null*
- **`description`** *(string)*


## Reference

### Properties

- **`id`** *(string)*
- **`page`** *(integer)*
- **`bounding_box`**: Refer to *[BoundingBox](#BoundingBox)*.
- **`document`**: Refer to *[Document](#Document)*.

## BoundingBox

### Properties

- **`x_min`** *(float)*
- **`x_max`** *(float)*
- **`y_min`** *(float)*
- **`y_max`** *(float)*.
