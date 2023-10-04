# Tileset

*Tiling scheme information.*

### Properties

- **`bounds`** *(array)*: Bounding box of the tile scheme.
  - **Items** *(number)*
- **`crs`** *(string)*: Coordinate reference system of the tile scheme.
- **`tile_size`** *(integer)*: Size of the tiles in the scheme.
- **`tiles`** *(array)*: List of tiles in the scheme.
  - **Items**: Refer to *[MapTile](#MapTile)*.

## AnalyticMethod

*Metadata of analytical methods used to obtain chemical and physical data. *

### Properties

- **`analytic_method`** *(string)*: Unique short name of analytical method.
- **`analytic_method_desc`** *(string)*: Descriptions of analytical methods.
- **`digestion_method`**: Digestion methods used in analytical methods.
  - **Any of**
    - *string*
    - *null*
- **`source`**: Refer to *[AnalyticMethodBiblio](#AnalyticMethodBiblio)*.

## AnalyticMethodBiblio

*Metadata of references for analytical methods used to obtain chemical data. *

### Properties

- **`analytic_method_pub_id`**: Unique author identifiers for analytic method publications.
  - **Any of**
    - *string*
    - *null*
- **`reference_pub_id`**: Reference identifiers for analytic method publications.
  - **Any of**
    - *string*
    - *null*
- **`analytic_method`**: Analytical method abbreviations, refers to field ANALYTIC_METHOD of AnalyticalMethod table.
  - **Any of**
    - *string*
    - *null*
- **`media`**: Analyzed media types for analytic method publications.
  - **Any of**
    - *string*
    - *null*
- **`pub_author`**: Authors of analytical method publications.
  - **Any of**
    - *string*
    - *null*
- **`pub_year`**: Year of analytic method publication. Min: 1947, Max: 2017, Units: year.
  - **Any of**
    - *string*
    - *null*
- **`pub_citation`**: Bibliographic citation for analytic method publication; may refer to chapter or section of publication.
  - **Any of**
    - *string*
    - *null*
- **`pub_url`**: URL of analytical method publication, if available.
  - **Any of**
    - *string*
    - *null*

## CoordinatesQualifier

*Metadata of qualifier codes for the precision of geographic coordinates.*

### Properties

- **`coordinates_qual`** *(integer)*: Qualifier code regarding precision of coordinates gained using GIS. Value 1-5.
- **`coordinates_qual_desc`** *(string)*: Description of coordinate qualifier.
- **`estimated_accuracy`**: Estimated positional accuracy of geospatial coordinates resolved by project.
  - **Any of**
    - *string*
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
- **`source`**: Source map of the point.
  - **All of**
    - : Refer to *[Map](#Map)*.
- **`geometry`**: Geometry of this feature, expressed as Lat Long in geographic coordinates.
- **`geology`**: Associated geologic data of the sample.
  - **All of**
    - : Refer to *[SampleData](#SampleData)*.
- **`mineral_best_value`**: 'Best Value' element chemical data.
  - **All of**
    - : Refer to *[Mineral_BestValueData](#Mineral_BestValueData)*.
- **`whole_rock_majors_best_value`**: Table of 'best value' chemical 'whole rock' major element data for rock, sediment, soil and organic samples.
  - **All of**
    - : Refer to *[WholeRockMajors_BestValueData](#WholeRockMajors_BestValueData)*.
- **`whole_rock_others_best_value`**: Table of 'best value' chemical 'whole rock' data of other various elements, compounds and physical measurements for rock, sediment, soil and organic samples.
  - **All of**
    - : Refer to *[WholeRockOthers_BestValueData](#WholeRockOthers_BestValueData)*.

## MapTile

*A tile representing geologic map information covering a small area.*

### Properties

- **`x`** *(integer)*: X coordinate of the tile.
- **`y`** *(integer)*: Y coordinate of the tile.
- **`z`** *(integer)*: Z coordinate of the tile.
- **`points`** *(array)*: Points in the tile.
  - **Items**: Refer to *[MapPoint](#MapPoint)*.

## Mineral_BestValueData

*Table of 'best value' chemical data for rock, sediment, soil and organic samples.
Values listed as optional due to some elements being measured in ppm and others as a percent, and not all elements
having measurements.*

### Properties

- **`cmibs_id`** *(integer)*: Unique identifier assigned to each sample entered in the CMIBS geochemical database; foreign key from Geology table.
- **`mineral_ppm`**: Parts per million of target mineral for best model.
  - **Any of**
    - *number*
    - *null*
- **`mineral_pct`**: Best value of target mineral in weight percent.
  - **Any of**
    - *number*
    - *null*
- **`mineral_am`**: Refer to *[AnalyticMethod](#AnalyticMethod)*.
- **`mineral_ppm_all`**: Parts per million of target mineral for all models.
  - **Any of**
    - *number*
    - *null*
- **`mineral_pct_all`**: All values of target mineral in weight percent.
  - **Any of**
    - *number*
    - *null*

## SampleAnalyticData

*Metadata of descriptive and analytical attributes for rock, sediment, soil and organic samples.
Many fields may be optional.*

### Properties

- **`field_id`**: Field identifiers assigned by the sample collector of samples submitted for analysis.
  - **Any of**
    - *string*
    - *null*
- **`lab_id`**: Laboratory batch identifiers assigned by the Sample Control Officers of the analytical laboratories that received the samples as batches.
  - **Any of**
    - *string*
    - *null*
- **`job_id`**: Unique identifiers assigned to submitted samples by the Sample Control Officer of the analytical laboratory that received the samples.
  - **Any of**
    - *string*
    - *null*
- **`submitter`**: Names of the individuals who submitted samples in batches to the laboratories for analysis.
  - **Any of**
    - *string*
    - *null*
- **`project_name`**: Project names, at times derived from project account numbers, of work groups funded for the collection and analysis of submitted samples.
  - **Any of**
    - *string*
    - *null*
- **`date_submitted`**: Date sample was submitted to Sample Control for initial database processing prior to sample prep and analysis; or date sample and its data were added to the database from non-USGS sources; in the format mm/dd/yyyy.
  - **Any of**
    - *string*
    - *null*
- **`method_collected`**: Sample collection method: single grab, composite, or channel.
  - **Any of**
    - *string*
    - *null*
- **`previous_job_id`**: Original NGDB batch numbers (JOB_ID) of USGS resubmitted samples that have been given new batch numbers upon resubmittal for further analysis.
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

## SampleData

*Metadata of spatial, geologic and descriptive attributes for rock, sediment, soil and organic samples.*

### Properties

- **`cmibs_id`** *(integer)*: Unique identifier assigned to each sample entered in the CMIBS geochemical database.
- **`analytics`**: Data related to the analytic methods for obtaining and processing the sample.
  - **All of**
    - : Refer to *[SampleAnalyticData](#SampleAnalyticData)*.
- **`location`**: Data related ot the location of the sample.
  - **All of**
    - : Refer to *[SampleLocationData](#SampleLocationData)*.
- **`geologic`**: Data related to the specific geology of the sample.
  - **All of**
    - : Refer to *[SampleGeologicData](#SampleGeologicData)*.

## SampleGeologicData

*Metadata of geologic attributes for rock, sediment, soil and organic samples. Many fields may be optional.*

### Properties

- **`sample_source`**: Physical settings or environments from which the samples were collected.
  - **Any of**
    - *string*
    - *null*
- **`primary_class`**: Primary classifications of sample media.
  - **Any of**
    - *string*
    - *null*
- **`secondary_class`**: Secondary classifications or subclasses of sample media.
  - **Any of**
    - *string*
    - *null*
- **`specific_name`**: Specific names for sample media.
  - **Any of**
    - *string*
    - *null*
- **`sample_comment`**: Attributes used to modify PRIMARY_CLASS, SECONDARY_CLASS, or SPECIFIC_NAME.
  - **Any of**
    - *string*
    - *null*
- **`addl_attr`**: Additional attributes used to modify PRIMARY_CLASS, SECONDARY_CLASS, or SPECIFIC_NAME.
  - **Any of**
    - *string*
    - *null*
- **`geologic_age`**: Ages or ranges of ages from the Geological Time Scale for the collected samples.
  - **Any of**
    - *string*
    - *null*
- **`stratigraphy`**: Names of the stratigraphic units from which samples were collected.
  - **Any of**
    - *string*
    - *null*
- **`strat_grp`**: Summary field of formations, groups or supergroups for entries in STRATIGRAPHY.
  - **Any of**
    - *string*
    - *null*
- **`start_sort`**: Summary field for entries in STRATIGRAPHY.
  - **Any of**
    - *string*
    - *null*
- **`regional_geology`**: Regional geologic settings of stratigraphic units.
  - **Any of**
    - *string*
    - *null*
- **`tectonic_setting`**: Tectonic settings for deposition of stratigraphic units.
  - **Any of**
    - *string*
    - *null*
- **`source_terrain`**: Tectonic terrains as sources of deposition for stratigraphic units.
  - **Any of**
    - *string*
    - *null*
- **`metallogeny`**: Metallogenic associations of stratigraphic units.
  - **Any of**
    - *string*
    - *null*
- **`mineralizaton`**: Indications of mineralization or mineralization types as provided by sample submitters.
  - **Any of**
    - *string*
    - *null*
- **`alteration`**: Indications of the presence or types of alteration noted in samples by submitters.
  - **Any of**
    - *string*
    - *null*

## SampleLocationData

*Metadata of spatial attributes for rock, sediment, soil and organic samples. Many fields may be optional.*

### Properties

- **`country`**: Countries or marine bodies of water from where samples were collected.
  - **Any of**
    - *string*
    - *null*
- **`state_province`**: Countries or marine bodies of water from where samples were collected.
  - **Any of**
    - *string*
    - *null*
- **`quad`**: Names of 1:250,000-scale quadrangles (1-degree x 2-degree or 1-degree by 3-degree) in which samples were collected.
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
  - **All of**
    - : Refer to *[CoordinatesQualifier](#CoordinatesQualifier)*.
- **`coordinates_comment`**: Comments regarding precision of geospatial coordinates.
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

## WholeRockMajors_BestValueData

*Table of 'best value' chemical 'whole rock' major element data for rock, sediment, soil and organic samples. *

### Properties

- **`cmibs_id`** *(integer)*: Unique identifier assigned to each sample entered in the CMIBS geochemical database; foreign key from Geology table.
- **`wr_qual`** *(integer)*: Qualifier for whole rock analysis, from 1 to 6, where 1 is the most precise analytical method package with the best sample digestion, and 6 is the least.
- **`wr_def`** *(string)*: Definition of qualifier for whole rock analysis.
- **`compoundmajor_pct`**: Best value in weight percent of whole rock majority.
  - **Any of**
    - *number*
    - *null*
- **`compoundmajor_am`**: Refer to *[AnalyticMethod](#AnalyticMethod)*.
- **`compoundmajor_pct_all`**: All values in weight percent of whole rock majority.
  - **Any of**
    - *number*
    - *null*

## WholeRockOthers_BestValueData

*Table of 'best value' chemical 'whole rock' data of other various elements, compounds and physical measurements
for rock, sediment, soil and organic samples*

### Properties

- **`cmibs_id`** *(integer)*: Unique identifier assigned to each sample entered in the CMIBS geochemical database; foreign key from Geology table.
- **`loi_pct`** *(number)*: Loss on ignition as 'best value', in weight percent. Negative values indicate concentrations less than the lower limit of determination for the analytical method. The absolute value of the negative number is the lower limit of determination. A null or empty cell means not analyzed. LOI first at 600 to 650 degrees centegrade, LOI second at 900 to 950 degrees centegrade.
- **`loi_pct_all`**: Loss on ignition, at 600 to 650 or 900 to 950 degrees centigrade, all values, in weight percent, and their analytical methods, from best method to least, as concatenations.
  - **Any of**
    - *number*
    - *null*
- **`compound_pct`**: Other compound, as 'best value', in weight percent. Negative values indicate concentrations less than the lower limit of determination for the analytical method. The absolute value of the negative number is the lower limit of determination. A null (or empty cell) means not analyzed.
  - **Any of**
    - *number*
    - *null*
- **`compound_pct_am`**: Analytical methods used for 'best values' of other compound.
  - **All of**
    - : Refer to *[AnalyticMethod](#AnalyticMethod)*.
- **`compound_pct_all`**: Other compound, all values, in weight percent, and their analytical methods, from best method to least, as concatenations.
  - **Any of**
    - *number*
    - *null*
- **`dop_si`**: Degree of pyritization, as a calculation FePyr(FePyr + FeHCl), as 'best value', in standard units. Negative values indicate concentrations less than the lower limit of determination for the analytical method. The absolute value of the negative number is the lower limit of determination. A null (or empty cell) means not analyzed for the species.
  - **Any of**
    - *number*
    - *null*
- **`dop_am`**: Degree of pyritization, analytical method used for 'best value'; see ANALYTIC_METHOD field of AnalyticMethod table for method description.
  - **All of**
    - : Refer to *[AnalyticMethod](#AnalyticMethod)*.
- **`dop_si_all`**: Degree of pyritization, all values, in weight percent, and their analytical methods, from best method to least, as a concatenation.
  - **Any of**
    - *number*
    - *null*
- **`varDensity_gcc`**: Variable 'Bulk' or 'Powder' density, as 'best value', in grams per cubic centimeter. A null (or empty cell) means not analyzed for the species.
  - **Any of**
    - *number*
    - *null*
- **`varDensity_am`**: Variable 'Bulk' or 'Powder' density, analytical method used for 'best value'.
  - **All of**
    - : Refer to *[AnalyticMethod](#AnalyticMethod)*.
- **`varDensity_gcc_all`**: Variable 'Bulk' or 'Powder' density, all values, in grams per cubic centimeter, and their analytical methods, from best method to least, as a concatenation.
  - **Any of**
    - *number*
    - *null*
- **`satind_si`**: Saturation index, as 'best value', in standard units. A null (or empty cell) means not analyzed for the species.
  - **Any of**
    - *number*
    - *null*
- **`satind_am`**: Saturation index, analytical method used for 'best value.'.
  - **All of**
    - : Refer to *[AnalyticMethod](#AnalyticMethod)*.
- **`satind_si_all`**: Saturation index, all values, in standard units, and their analytical methods, from best method to least, as a concatenation.
  - **Any of**
    - *number*
    - *null*
- **`tmax_degC`**: Temperature at which the maximum release of hydrocarbons occurs during pyrolysis, as 'best value', in degrees Centigrade. A null (or empty cell) means not analyzed for the species.
  - **Any of**
    - *number*
    - *null*
- **`tmax_am`**: Temperature at which the maximum release of hydrocarbons occurs during pyrolysis, analytical methods used for 'best values.'.
  - **All of**
    - : Refer to *[AnalyticMethod](#AnalyticMethod)*.
- **`tmax_degC_all`**: Temperature at which the maximum release of hydrocarbons occurs during pyrolysis, all values, in weight percent, and their analytical methods, from best method to least, as concatenations.
  - **Any of**
    - *number*
    - *null*
- **`sVar_mgg`**: S1. Free hydrocarbons in the sample,  S2.Hydrocarbons generated through thermal cracking of nonvolatile organic matter, or  S3. Carbon dioxide produced during pyrolysis of kerogen, as 'best value', in milligrams of S1-2. hydrocarbon or S3. carbon dioxide per gram of rock. Negative values indicate concentrations less than the lower limit of determination for the analytical method. The absolute value of the negative number is the lower limit of determination. A null (or empty cell) means not analyzed for the species.
  - **Any of**
    - *number*
    - *null*
- **`sVar_am`**: Analytical method useds for 'best values.'.
  - **All of**
    - : Refer to *[AnalyticMethod](#AnalyticMethod)*.
- **`sVar_mgg_all`**: All values for S1, S2, S3, in weight percent, and their analytical methods, from best method to least,as concatenations.
  - **Any of**
    - *number*
    - *null*
- **`var_ratio`**: Hydrogen index (hi), or oxygen index (oi), or production index (pi), as 'best value', in milligrams of hi: hydrocarbons [100 x S2] (hi), oi: carbon dioxide [100 x S3],pi: [S1] hydrocarbons milligrams of [S1 + S2] hydrocarbons, per gram of total organic carbon. A null (or empty cell) means not analyzed for the species.
  - **Any of**
    - *number*
    - *null*
- **`var_am`**: Analytical methods used for 'best values.'.
  - **All of**
    - : Refer to *[AnalyticMethod](#AnalyticMethod)*.
- **`var_ratio_all`**: Hydrogen index (in weight percent), oxygen index (in parts per million), or production index (in weight percent), all values, in weight percent, and their analytical methods, from best method to least, as concatenations.
  - **Any of**
    - *number*
    - *null*

