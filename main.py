from scraper import fetch_and_screenshot
from ai_writer import ai_spin_content, ai_review_content
from human_loop import human_edit
from chromadb_manager import save_to_chromadb
from rl_search import rl_search_query

def main():
    print("main started")
    print("📥 Fetching and processing content...")
    text = fetch_and_screenshot()

    print("🤖 AI Writer: Spinning content...")
    spun = ai_spin_content(text)

    print("🔎 AI Reviewer: Reviewing content...")
    reviewed = ai_review_content(spun)

    print("👤 Human: Making final edits...")
    final = human_edit(reviewed)

    print("💾 Final version saved in ChromaDB.")
    save_to_chromadb(final)

    print("🎯 RL search: Retrieved content summary:")
    print(rl_search_query("Gates of Morning"))

if __name__ == "__main__":
    main()