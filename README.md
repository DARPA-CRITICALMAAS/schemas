## Schemas and APIs
A place to describe schemas for data and APIs for services for the project.

We propose to use [JSON Schemas](http://json-schema.org/specification.html) to describe data - specifically the [2020-12 version](http://json-schema.org/specification-links.html#2020-12).

The benfits of this approach are because the JSON format:
- Describes your existing data format(s).
- Provides clear human- and machine- readable documentation.
- Validates data which is useful for:
- Automated testing.
- Ensures quality of client submitted data.

There is a great guide for JSON Schemas [here](http://json-schema.org/learn/getting-started-step-by-step.html).

## Index

- [TA1 schemas](ta1/README.md)
- [TA2 schemas](ta2/README.md)
- [TA3 schemas](ta3/README.md)

## Building the schemas

The JSON schemas in this library are compiled using [`pydantic`](https://docs.pydantic.dev/latest/)
model builder in Python, which provides a terse API for JSON schema construction.
This also allows an entity-relationship diagram to be generated.

- Install Python 3 (tested on `3.10`) and Poetry
- Run `poetry install` to install dependencies
- Run `make` to build the schemas and documentation

## Todo

- The script only builds one 'root model' per file, but this can be changed
- Add remaining schemas (especially for TA2 and TA3)
- Add basic schemas for feedback data (validation and correction modalities)
- Better, more comprehensive documentation
- Information about file formats and other data-handling infrastructure
- Work with TA1-3 to solidify and adjust schemas