from chromadb_manager import load_latest_version

def rl_search_query(query):
    doc = load_latest_version()
    content = doc['documents'][0]
    if query.lower() in content.lower():
        return f"✅ Match found for '{query}' in content."
    return "❌ No match found."