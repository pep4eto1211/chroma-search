# Chroma Search

A small command-line tool that indexes a CSV column in ChromaDB and searches
its values using semantic similarity.

## Setup

Requires Python 3.14 or newer and [uv](https://docs.astral.sh/uv/).

```sh
uv sync
```

## Usage

```sh
uv run python main.py <csv-file> <column-name> <search-term> [--results N]
```

For example, given a CSV file with a `description` header:

```sh
uv run python main.py products.csv description "comfortable running shoes" --results 5
```

The CSV must have a header row. The `--results` option (or `-r`) defaults to
10. Use `--help` to see all options.

Each run creates an in-memory collection, indexes the specified column, and
prints the raw ChromaDB query results. The index is not persisted between
runs. ChromaDB may download its default embedding model on first use.