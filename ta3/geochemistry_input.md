# Tileset

*Tiling scheme information.*

### Properties

- **`bounds`** *(array)*: Bounding box of the tile scheme.
  - **Items** *(number)*
- **`crs`** *(string)*: Coordinate reference system of the tile scheme.
- **`tile_size`** *(integer)*: Size of the tiles in the scheme.
- **`tiles`** *(array)*: List of tiles in the scheme.
  - **Items**: Refer to *[MapTile](#MapTile)*.

## GeologyGeologicData

### Properties

- **`sample_source`**: Physical settings or environments from which the samples were collected. .
  - **Any of**
    - *string*
    - *null*
- **`primary_class`**: Primary classifications of sample media. .
  - **Any of**
    - *string*
    - *null*
- **`secondary_class`**: Secondary classifications or subclasses of sample media. .
  - **Any of**
    - *string*
    - *null*
- **`specific_name`**: Specific names for sample media. .
  - **Any of**
    - *string*
    - *null*
- **`sample_comment`**: Attributes used to modify PRIMARY_CLASS, SECONDARY_CLASS, or SPECIFIC_NAME. .
  - **Any of**
    - *string*
    - *null*
- **`addl_attr`**: Additional attributes used to modify PRIMARY_CLASS, SECONDARY_CLASS, or SPECIFIC_NAME.
  - **Any of**
    - *string*
    - *null*
- **`geologic_age`**: Ages or ranges of ages from the Geological Time Scale for the collected samples. .
  - **Any of**
    - *string*
    - *null*
- **`stratigraphy`**: Names of the stratigraphic units from which samples were collected. .
  - **Any of**
    - *string*
    - *null*
- **`strat_grp`**: Summary field of formations, groups or supergroups for entries in STRATIGRAPHY. .
  - **Any of**
    - *string*
    - *null*
- **`start_sort`**: Summary field for entries in STRATIGRAPHY. .
  - **Any of**
    - *string*
    - *null*
- **`regional_geology`**: Regional geologic settings of stratigraphic units. .
  - **Any of**
    - *string*
    - *null*
- **`tectonic_setting`**: Tectonic settings for deposition of stratigraphic units. .
  - **Any of**
    - *string*
    - *null*
- **`source_terrain`**: Tectonic terrains as sources of deposition for stratigraphic units. .
  - **Any of**
    - *string*
    - *null*
- **`metallogeny`**: Metallogenic associations of stratigraphic units. .
  - **Any of**
    - *string*
    - *null*
- **`mineralizaton`**: Indications of mineralization or mineralization types as provided by sample submitters. .
  - **Any of**
    - *string*
    - *null*
- **`alteration`**: Indications of the presence or types of alteration noted in samples by submitters. .
  - **Any of**
    - *string*
    - *null*

## GeologySampleAnalyticData

### Properties

- **`field_id`**: Field identifiers assigned by the sample collector of samples submitted for analysis.
  - **Any of**
    - *string*
    - *null*
- **`lab_id`**: Laboratory batch identifiers assigned by the Sample Control Officers of the analytical laboratories that received the samples as batches. .
  - **Any of**
    - *string*
    - *null*
- **`job_id`**: Unique identifiers assigned to submitted samples by the Sample Control Officer of the analytical laboratory that received the samples.
  - **Any of**
    - *string*
    - *null*
- **`submitter`**:  Names of the individuals who submitted samples in batches to the laboratories for analysis.
  - **Any of**
    - *string*
    - *null*
- **`project_name`**: Project names, at times derived from project account numbers, of work groups funded for the collection and analysis of submitted samples.
  - **Any of**
    - *string*
    - *null*
- **`date_submitted`**: Date sample was submitted to Sample Control for initial database processing prior to sample prep and analysis; or date sample and its data were added to the database from non-USGS sources. in the format mm/dd/yyyy.
  - **Any of**
    - *string*
    - *null*
- **`method_collected`**: Sample collection method: single grab, composite, or channel.
  - **Any of**
    - *string*
    - *null*
- **`previous_job_id`**: Original NGDB batch numbers (JOB_ID) of USGS resubmitted samples that have been given new batch numbers upon resubmittal for further analysis. .
  - **Any of**
    - *string*
    - *null*
- **`previous_lab_id`**: Original NGDB LAB_IDs of USGS resubmitted samples that have been given new lab numbers upon resubmittal for further analysis.
  - **Any of**
    - *string*
    - *null*
- **`publ_id`**: Identifiers for publications that are sources of data, or where data is cited.
  - **Any of**
    - *string*
    - *null*
- **`data_source`**: Identifiers for other sources of data; databases, publications, individuals.
  - **Any of**
    - *string*
    - *null*

## GeologySampleData

*metadata related to the geology of the sample from Geology.txt file*

### Properties

- **`analytics`**: data related to the analytic methods for obtainingand processing the sample.
  - **Any of**
    - : Refer to *[GeologySampleAnalyticData](#GeologySampleAnalyticData)*.
    - *null*
- **`location`**: data related ot the location of the sample.
  - **Any of**
    - : Refer to *[GeologySampleLocationData](#GeologySampleLocationData)*.
    - *null*
- **`geologic`**: data related to the specific geology of the sample.
  - **Any of**
    - : Refer to *[GeologyGeologicData](#GeologyGeologicData)*.
    - *null*

## GeologySampleLocationData

### Properties

- **`country`**: Countries or marine bodies of water from where samples were collected.
  - **Any of**
    - *string*
    - *null*
- **`state_province`**: Countries or marine bodies of water from where samples were collected.
  - **Any of**
    - *string*
    - *null*
- **`quad`**:  Names of 1:250,000-scale quadrangles (1-degree x 2-degree or 1-degree by 3-degree) in which samples were collected.
  - **Any of**
    - *string*
    - *null*
- **`latitude`** *(number)*: Latitude coordinate of sample site, reported in decimal degrees; see metadata for further datum and spheroid information.
- **`longitude`** *(number)*: Longitude coordinate of sample site, reported in decimal degrees; there are sites on both sides of the International Date Line; see metadata for further datum and spheroid information.
- **`spheroid`**: Reference spheroids or ellipsoids, when recorded, for the latitude and longitude coordinates of the sample sites.
  - **Any of**
    - *string*
    - *null*
- **`datum`**: Reference datums, when recorded, for the latitude and longitude coordinates of the sample sites.
  - **Any of**
    - *string*
    - *null*
- **`coordinates_qual`**: Qualifier code regarding precision of coordinates gained using GIS. Not all samples have the code if they weren’t determined by GIS analysis.
  - **Any of**
    - *integer*
    - *null*
- **`coordinates_comment`**:  Comments regarding precision of geospatial coordinates.
  - **Any of**
    - *string*
    - *null*
- **`locate_desc`**: Geographic information relating to the locations of the sample sites.
  - **Any of**
    - *string*
    - *null*
- **`depth`**: Depths from the surface at which samples were collected; units are specified by the submitter and included with the values.
  - **Any of**
    - *integer*
    - *null*

## Map

*Schema for map information.*

### Properties

- **`ref_url`** *(string)*: Source URL of the map.
- **`ref_name`** *(string)*: Short name of the map.
- **`ref_title`** *(string)*: Title of the map.
- **`ref_authors`** *(array)*: Authors.
  - **Items** *(string)*
- **`ref_source`** *(string)*: Publication/data release containing the map.

  Examples:
  ```json
  "U.S. Geological Survey Data Series 424"
  ```

- **`ref_year`** *(integer)*: Publication year.

  Examples:
  ```json
  "2009"
  ```


## MapPoint

### Properties

- **`id`** *(integer)*: Internal ID of the point. CMIBS Sample ID.
- **`geometry`**: Geometry of this feature, expressed as Lat Long in geographic coordinates.
- **`geology`**: Associated geologic data of the sample.
  - **All of**
    - : Refer to *[GeologySampleData](#GeologySampleData)*.
- **`mineral_best_value`**: 'Best Value' element chemical data.
  - **All of**
    - : Refer to *[MineralBestValueData](#MineralBestValueData)*.
- **`whole_rock_best_value_majors`**: 'Best Value' whole rock chemical data.
  - **All of**
    - : Refer to *[WholeRockBestValueMajorsData](#WholeRockBestValueMajorsData)*.
- **`whole_rock_best_value_others`**: 'Best Value' whole rock chemical data.
  - **All of**
    - : Refer to *[WholeRockBestValueOthersData](#WholeRockBestValueOthersData)*.
- **`source`**: Source map of the point.
  - **All of**
    - : Refer to *[Map](#Map)*.

## MapTile

*A tile representing geologic map information covering a small area.*

### Properties

- **`x`** *(integer)*: X coordinate of the tile.
- **`y`** *(integer)*: Y coordinate of the tile.
- **`z`** *(integer)*: Z coordinate of the tile.
- **`points`** *(array)*: Points in the tile.
  - **Items**: Refer to *[MapPoint](#MapPoint)*.

## MineralBestValueData

*Data from BestValue_Element.txt file
values listed as optional due to some elements being measured in ppm and others as a percent, and not all elements
having measurements*

### Properties

- **`cmibs_id`** *(integer)*: Unique identifier assigned to each sample entered in the CMIBS geochemical database; foreign key from Geology table.
- **`element_ppm`**: elemental best value in ppm.
  - **Any of**
    - *number*
    - *null*
- **`element_pct`**: elemental best value in pct.
  - **Any of**
    - *number*
    - *null*
- **`element_am`**: analytical method used for "best value", abbreviation; see ANALYTIC_METHOD field of AnalyticMethod table for method description.
  - **Any of**
    - *string*
    - *null*
- **`element_ppm_all`**: elemental all values in ppm.
  - **Any of**
    - *number*
    - *null*
- **`element_pct_all`**: elemental all values in pct.
  - **Any of**
    - *number*
    - *null*

## WholeRockBestValueMajorsData

*Data from BestValue_WholeRock_Majors.txt file*

### Properties

- **`cmibs_id`** *(integer)*: Unique identifier assigned to each sample entered in the CMIBS geochemical database; foreign key from Geology table.
- **`wr_qual`** *(integer)*: Qualifier for whole rock analysis, from 1 to 6, where 1 is the most precise analytical method package with the best sample digestion, and 6 is the least.
- **`compound_pct`**: compound best value in weight percent.
  - **Any of**
    - *number*
    - *null*
- **`compound_am`**: analytical method used for "best value", abbreviation; see ANALYTIC_METHOD field of AnalyticMethod table for method description.
  - **Any of**
    - *string*
    - *null*
- **`element_pct_all`**: compound all values in weight pct.
  - **Any of**
    - *number*
    - *null*

## WholeRockBestValueOthersData

*Data from BestValue_WholeRock_Others.txt file*

### Properties

- **`cmibs_id`** *(integer)*: Unique identifier assigned to each sample entered in the CMIBS geochemical database; foreign key from Geology table.
- **`loi_pct`** *(number)*: Loss on ignition, at 900 to 950 degrees centigrade, as "best value", in weight percent. Negative values indicate concentrations less than the lower limit of determination for the analytical method. The absolute value of the negative number is the lower limit of determination. A null (or empty cell) means not analyzed. (Source: Metadata author).
- **`loi_am`** *(number)*: Loss on ignition, at 900 to 950 degrees centigrade, analytical method used for "best value"; see ANALYTIC_METHOD field of AnalyticMethod table for method description.
- **`NOT_FINISHED`** *(string)*: still lots of columns to go through.

