"""
Script to generate JSON schemas and markdown documentation from pydantic models.
Usage: python scripts/generate-schema.py <schema_file.py> <RootModel>

"""
from json import dumps
from jsonschema2md import Parser
import erdantic as erd
from pydantic import BaseModel
from pathlib import Path
from importlib import import_module
import sys

# Define PYTHONPATH

schema_file = sys.argv[1]
root_model = sys.argv[2]

# Get the output directory
fn = Path(schema_file)
output_dir = fn.parent
name = fn.stem

sys.path.append(str(output_dir))


# print(Path.cwd())
# Convert filename to module name
# Import the schema file
# mod_name = schema_file.replace("/", ".").replace(".py", "")
# print(mod_name)
mod = import_module(name=fn.stem)

# Find the root model
RootModel = getattr(mod, root_model)
assert issubclass(RootModel, BaseModel)

graph = erd.create(RootModel)

# Draw the entity-relation diagram
erd_file = output_dir / (name + ".png")
graph.draw(out=erd_file)

schema = RootModel.model_json_schema()

json_file = output_dir / (name + ".json")
with json_file.open("w") as f:
    f.write(dumps(schema, indent=2))

parser = Parser(
    examples_as_yaml=False,
)

md_lines = []

sub_models = [d.model for d in graph.models if d.model is not RootModel]
models = [RootModel] + sub_models

for d in models:
    schema = d.model_json_schema()
    lines = parser.parse_schema(schema)
    md_lines.extend(lines)
    md_lines.append("\n")

text = "".join(md_lines).replace("#/$defs/", "").replace("#$defs/", "#")
# Move headers down a level
text = text.replace("\n#", "\n##")

doc_file = output_dir / (name + ".md")
with doc_file.open("w") as f:
    f.write(text)
