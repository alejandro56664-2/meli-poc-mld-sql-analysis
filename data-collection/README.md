# Data Collection

This component connects to SourceGraph via GraphQL client a retrieve all SQL queries from the MLD Insurtech Team and create a dataset for after analysis.

## Run locally

requirements:

- Python 3.+
- [Poetry](https://python-poetry.org/docs/#installation)

Please create a SourceGraph token and update or create an '.env' file in root folder, like this:

```sh
SOURCEGRAPH_TOKEN=XXXXX
```

Activate virtual environment

```sh
poetry shell
```

execute the next command to run the app:

```shell
python3 data_collection/main.py
```
