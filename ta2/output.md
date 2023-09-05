# MineralResourceSite

*A mineral resource site from MRDS.*

### Properties

- **`deposit_id`** *(integer)*
- **`mrds_id`**
  - **Any of**
    - *string*
    - *null*
- **`url`** *(string)*
- **`area_name`**
  - **Any of**
    - *string*
    - *null*
- **`minerals`** *(array)*
  - **Items** *(string)*
- **`location`**
- **`commodities`**: Refer to *[Commodities](#Commodities)*.
- **`history`**: Refer to *[History](#History)*.
- **`reporter`**
  - **Any of**
    - *string*
    - *null*
- **`ref`**
  - **Any of**
    - *string*
    - *null*
- **`score`**: Refer to *[Score](#Score)*.

## Commodities

### Properties

- **`primary`** *(array)*
  - **Items** *(string)*
- **`secondary`** *(array)*
  - **Items** *(string)*
- **`accessory`** *(array)*
  - **Items** *(string)*
- **`metallic`** *(boolean)*
- **`nonmetallic`** *(boolean)*

## History

### Properties

- **`discovery_year`**
  - **Any of**
    - *integer*
    - *null*
- **`production_years`**
  - **Any of**
    - *string*
    - *null*
- **`development_status`**
  - **Any of**
    - *string*
    - *null*
- **`operation_type`**
  - **Any of**
    - *string*
    - *null*

