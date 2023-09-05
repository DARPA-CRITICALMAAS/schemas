# Tileset

*Tiling scheme information.*

### Properties

- **`bounds`** *(array)*: Bounding box of the tile scheme.
  - **Items** *(number)*
- **`crs`** *(string)*: Coordinate reference system of the tile scheme.
- **`tile_size`** *(integer)*: Size of the tiles in the scheme.
- **`tiles`** *(array)*: List of tiles in the scheme.
  - **Items**: Refer to *[MapTile](#MapTile)*.

## BoundaryAge

*Bounding age of a map unit*

### Properties

- **`age`** *(integer)*: Age in Ma, if known.
- **`interval`** *(string)*: Age interval name.

  Examples:
  ```json
  "Holocene"
  ```

  ```json
  "Cretaceous"
  ```

- **`interval_id`** *(integer)*: Age interval ID, from Macrostrat.

  Examples:
  ```json
  1
  ```

  ```json
  2
  ```


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


## MapLine

### Properties

- **`id`** *(integer)*: Internal ID of the line.
- **`geometry`**: Geometry of this feature.
- **`description`** *(string)*: Description of the line.
- **`name`**: Name of the line.
  - **Any of**
    - *string*
    - *null*

  Examples:
  ```json
  "San Andreas Fault"
  ```

- **`type`** *(string)*: Type of the line.
- **`direction`** *(integer)*: Direction of the line.

  Examples:
  ```json
  1
  ```

  ```json
  -1
  ```

- **`source`**: Source map of the line.
  - **All of**
    - : Refer to *[Map](#Map)*.

## MapPoint

### Properties

- **`id`** *(integer)*: Internal ID of the point.
- **`geometry`**: Geometry of this feature.
- **`type`** *(string)*: Type of the point.

  Examples:
  ```json
  "borehole"
  ```

  ```json
  "bedding"
  ```

- **`name`**: Name of the point.
  - **Any of**
    - *string*
    - *null*
- **`dip`**: Dip of the point.
  - **Any of**
    - *number*
    - *null*
- **`dip_direction`**: Strike of the point.
  - **Any of**
    - *number*
    - *null*
- **`description`** *(string)*: Description of the point.
- **`source`**: Source map of the point.
  - **All of**
    - : Refer to *[Map](#Map)*.

## MapPolygon

*Macrostrat proposal for geologic mapping output schema.
This is fairly similar to the existing output of Macrostrat's tile-based
geological map services, with several changes:

- Allowance for more specific/harmonized lithological information
- Normalization for clarity*

### Properties

- **`id`** *(integer)*: Internal ID of the map unit.
- **`geometry`**: Geometry of this feature.
- **`age`** *(string)*: Geologic age of the map unit, from source map.
- **`t_age`**: Upper age of the map unit.
  - **All of**
    - : Refer to *[BoundaryAge](#BoundaryAge)*.
- **`b_age`**: Lower age of the map unit.
  - **All of**
    - : Refer to *[BoundaryAge](#BoundaryAge)*.
- **`legend_id`** *(integer)*: ID of the map legend block.
- **`lithology`** *(array)*: Lithology descriptions.
  - **Items** *(string)*
- **`description`** *(string)*: Description of the map unit.
- **`comments`** *(string)*: Comments.
- **`name`** *(string)*: Name of the map unit.
- **`color`**: Color of the map unit, on the original map.
  - **Any of**
    - *string*
    - *null*
- **`pattern`**: FGDC pattern of the map unit, if any.
  - **Any of**
    - *string*
    - *null*
- **`source`**: Source map of the map unit.
  - **All of**
    - : Refer to *[Map](#Map)*.

## MapTile

*A tile representing geologic map information covering a small area.*

### Properties

- **`x`** *(integer)*: X coordinate of the tile.
- **`y`** *(integer)*: Y coordinate of the tile.
- **`z`** *(integer)*: Z coordinate of the tile.
- **`units`** *(array)*: Map units in the tile.
  - **Items**: Refer to *[MapPolygon](#MapPolygon)*.
- **`lines`** *(array)*: Lines in the tile.
  - **Items**: Refer to *[MapLine](#MapLine)*.
- **`points`** *(array)*: Points in the tile.
  - **Items**: Refer to *[MapPoint](#MapPoint)*.

