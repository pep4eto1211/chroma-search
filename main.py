import csv
from typing import Annotated

import chromadb
import typer
from rich import print

app = typer.Typer(add_completion=False)

def init_collection():
    print("Initializing ChromaDB")
    chroma_client = chromadb.Client()
    return chroma_client.create_collection(name="column")

@app.command()
def main(file_name: Annotated[str, typer.Argument(help="Path to the CSV file")],
        column: Annotated[str, typer.Argument(help="Column to index and search")],
        search_term: Annotated[str, typer.Argument(help="Term to search in the indexed column")],
        num_results: Annotated[int, typer.Option("--results", "-r", help="Number of results returned by search")] = 10):
    collection = init_collection()
    
    print(f"Indexing file column {column}")
    with open(file_name) as f:
        reader = csv.DictReader(f)
        for idx, row in enumerate(reader):
            collection.add(
                ids = [str(idx)],
                documents = [
                    row[column]
                ]
            )

    print(f"Searching for {search_term}")
    results = collection.query(
        query_texts=[search_term],
        n_results=num_results
    )
    print(results)

if __name__ == "__main__":
    app()