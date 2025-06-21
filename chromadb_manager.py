import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("book_versions")

def save_to_chromadb(content):
    collection.add(
        documents=[content],
        ids=["chapter_1_final"]
    )

def load_latest_version():
    return collection.get(ids=["chapter_1_final"])