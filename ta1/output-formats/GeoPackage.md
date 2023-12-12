## Proposal for TA1 GeoPackage output

_Proposed on 2023-12-06 by Daven Quinn, Macrostrat_

TA1 and TA4 performers should prefer the GeoPackage format for map data output. GeoPackage is an open [standard](http://www.geopackage.org/spec/) maintained by the Open Geospatial Consortium (OGC).
The format has several advantages over both Shapefiles and GeoJSON. GeoPackage

- Is based on SQLite so is widely readable and extensible
- Has decent compression
- Can contain multiple layers (all TA1 schema elements) in a single file
- Allows explicit representation of projection, unlike GeoJSON (maps can be represented/used in their native or pixel-based forms)
- Allows foreign keys and other constraints
- Can contain non-geographic data/metadata in arbitrary SQL tables
- Has a defined standards for how to include raster data, if that is desired by TA1 teams alongside the core spec

See [one of my favorite GIS websites](http://switchfromshapefile.org/) for more context on the GIS format wars. 

GeoPackage is a little harder to write than GeoJSON, but not overly so with modern libraries.

As a proof-of-concept, I just created a [GeoPackage writer](https://github.com/UW-Macrostrat/macrostrat/pull/6/files) for Macrostrat map datasets. This is still very minimal and does not yet follow the TA1 schema or contain much metadata. However, it does show the Python libraries (`geopandas` , which wraps `pandas`, `fiona` and `sqlalchemy`) that can be used to write GeoPackage content. Other libraries outside of Python, such as the `ogr2ogr` command-line tool, can also be used.

Over time, we could iterate this or similar code to implement the TA1 schema spec faithfully, including SQL niceties such as foreign key constraints and the normalized table design implied by the schema code. This could possibly also be done as a shared library referencing the TA1 schemas to ensure that we can all read/write map data files, or test dataset compliance.