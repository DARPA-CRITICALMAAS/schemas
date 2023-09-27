all:
	poetry run python scripts/generate-schema.py ta1/output.py Map
	poetry run python scripts/generate-schema.py ta2/output.py MineralOccurrence GradeTonnageModel MineralSystem
	poetry run python scripts/generate-schema.py ta3/input.py Tileset
	poetry run python scripts/generate-schema.py ta3/output.py ProspectivityModel
