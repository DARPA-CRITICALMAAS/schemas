# MineralOccurrence

*A mineral resource site, based on MRDS.*

### Properties

- **`id`** *(integer)*
- **`mrds_id`**
  - **Any of**
    - *string*
    - *null*
- **`mrds_url`**
  - **Any of**
    - *string*
    - *null*
- **`type`**: Refer to *[OccurrenceType](#OccurrenceType)*.
- **`area_name`**
  - **Any of**
    - *string*
    - *null*
- **`minerals`** *(array)*
  - **Items** *(string)*
- **`location`**
  - **Any of**
    - 
    - *null*
- **`commodities`**: Refer to *[Commodities](#Commodities)*.
- **`history`**
  - **Any of**
    - : Refer to *[History](#History)*.
    - *null*
- **`reporter`**
  - **Any of**
    - *string*
    - *null*
- **`score`**: Refer to *[Score](#Score)*.
- **`sources`** *(array)*
  - **Items**: Refer to *[Document](#Document)*.
- **`geologic_unit`**: Refer to *[GeologicUnit](#GeologicUnit)*.

## MineralDepositModel

### Properties


## GradeTonnageModel

### Properties

- **`ore_quantity`** *(number)*: Ore quantity in metric tons.
- **`grades`** *(array)*
  - **Items**: Refer to *[GradeInformation](#GradeInformation)*.
- **`type`**: Type of resource.
  - **All of**
    - : Refer to *[MineralResourceClassification](#MineralResourceClassification)*.

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

## Document

### Properties

- **`doi`**
  - **Any of**
    - *string*
    - *null*
- **`title`**
  - **Any of**
    - *string*
    - *null*
- **`authors`** *(array)*
  - **Items** *(string)*
- **`journal`**
  - **Any of**
    - *string*
    - *null*
- **`year`**
  - **Any of**
    - *integer*
    - *null*
- **`volume`**
  - **Any of**
    - *integer*
    - *null*
- **`issue`**
  - **Any of**
    - *integer*
    - *null*
- **`description`**
  - **Any of**
    - *string*
    - *null*

## GeologicUnit

### Properties

- **`age`** *(string)*
- **`name`** *(string)*
- **`description`** *(string)*
- **`lithology`** *(array)*
  - **Items** *(string)*
- **`environments`** *(array)*
  - **Items** *(string)*
- **`comments`** *(string)*

## GradeInformation

### Properties

- **`species`** *(string)*: Species of interest (mineral or element).
- **`concentration`** *(number)*: Concentration of species in ppm.
- **`unit`**: Unit of concentration.
  - **All of**
    - : Refer to *[ConcentrationUnit](#ConcentrationUnit)*.

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

