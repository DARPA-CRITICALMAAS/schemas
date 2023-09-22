# Mineral Inventory

*Mineral inventory data*

### Properties

- **`id`** *(integer)*
- **`mine`**: Refer to *[MineralSite](#MineralSite)*.
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

## MineralSite

### Properties

- **`id`** *(string)*
- **`name`** *(string)*
- **`location`** *(Geometry)*
- **`crs`** *(string)*
- **`country`** *(string)*
- **`location_source`** *(string)*
- **`state_or_province`**
    - **Any of**
        - *string*
        - *null*
- **`same_as`**
    - **Any of**
        - *dict*
        - *null*


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
