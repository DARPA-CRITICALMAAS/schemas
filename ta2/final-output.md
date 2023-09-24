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
- **`title`** *(string)*


## Reference

### Properties

- **`id`** *(string)*
- **`date`** *(date)*
- **`page`** *(integer)*
- **`line`** *(integer)*
- **`document`**: Refer to *[Document](#Document)*.
