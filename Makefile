all:
	poetry run python scripts/generate-schema.py ta1/output.py Map
	poetry run python scripts/generate-schema.py ta2/output.py MineralOccurrence MineralDepositModel GradeTonnageModel MineralSystem
	poetry run python scripts/generate-schema.py ta3/input.py Tileset
