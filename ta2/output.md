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
- **`commodities`** *(array)*
  - **Items**: Refer to *[Commodity](#Commodity)*.
- **`location`**
  - **Any of**
    - 
    - *null*
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

## GradeTonnageModel

### Properties

- **`ore_quantity`** *(number)*: Ore quantity in metric tons.
- **`materials`** *(array)*
  - **Items**: Refer to *[CommodityWithConcentration](#CommodityWithConcentration)*.
- **`level`**: Type of resource.
  - **All of**
    - : Refer to *[ResourceDevelopmentLevel](#ResourceDevelopmentLevel)*.

## MineralSystem

### Properties

- **`deposit_type`** *(string)*
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

## Commodity

*A mineral or elemental commodity, with information about its importance in a deposit.*

### Properties

- **`species`**: Species of interest (mineral, element, or other commodity).
  - **Any of**
    - : Refer to *[MineralSpecies](#MineralSpecies)*.
    - *string*

  Examples:
  ```json
  "quartz"
  ```

  ```json
  "gold"
  ```

  ```json
  "silver"
  ```

  ```json
  "copper"
  ```

  ```json
  "lead"
  ```

  ```json
  "zinc"
  ```

  ```json
  "aggregate"
  ```

- **`is_ore`** *(boolean)*: Is this an ore or gangue mineral in this deposit?
- **`importance`**: Importance of this mineral in this deposit.
  - **All of**
    - : Refer to *[Importance](#Importance)*.

## CommodityWithConcentration

### Properties

- **`material`**: Species of interest (mineral or element).
  - **All of**
    - : Refer to *[Commodity](#Commodity)*.
- **`concentration`** *(number)*: Concentration of species in ppm.
- **`unit`**: Unit of concentration.
  - **All of**
    - : Refer to *[ConcentrationUnit](#ConcentrationUnit)*.

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

## MineralSpecies

*A mineral or elemental species of interest*

### Properties

- **`name`** *(string)*
- **`mindat_id`**
  - **Any of**
    - *string*
    - *null*
- **`formula`**
  - **Any of**
    - *string*
    - *null*
- **`metallic`** *(boolean)*: Is this a metallic mineral/element?

## Reference

### Properties

- **`doc`**: Refer to *[Document](#Document)*.
- **`text`** *(array)*
  - **Items** *(string)*
- **`coords`**
  - **Any of**
    - *array*
      - **Items** *(integer)*
    - *null*

