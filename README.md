# Agentic-Content-Transformation-System
AI agentic workflow by Muskan Singh (BTech CSE-AIML) for scraping, transforming, reviewing, and retrieving content using LLM logic, human feedback simulation, and ChromaDB version control.

	Agentic Content Transformation System
An AI-powered pipeline designed for automated content transformation and intelligent retrieval. Built during my internship at  Softnerve Technology , this system integrates LLMs, agentic workflows, human-in-the-loop simulation, and ChromaDB for versioning and intelligent search.
	Features
•	Web Scraping & Screenshots : Extracts chapters from public sources using Playwright
•	AI-Driven Content Generation : Uses LLMs (like Gemini or GPT) to rewrite and refine content
•	Human-in-the-Loop Simulation : Enables iterative AI-human reviews before finalizing    output
•	ChromaDB Versioning : Saves and indexes all content versions for reliable search
•	RL-Style Retrieval : Implements a reward-based search algorithm to fetch the best-matching version
	Tech Stack
   Tool                   Purpose                          
    Python             Main development language        
    Playwright         Web scraping and screenshots     
    LLMs               AI writing & reviewing           
    ChromaDB           Versioning and search indexing   
    RL Algorithm       Intelligent content retrieval    

	Project Structure
├── main.py                  # Workflow pipeline
├── scraper.py              # Extracts chapter content
├── ai_writer.py            # AI writing agent
├── human_loop.py           # Review simulation loop
├── chromadb_manager.py     # Save/search versions
├── rl_search.py            # Reward-based matching
├── requirements.txt
├── chapter_1.png           # Sample screenshot
└── README.md
	How to Run
1.  Install dependencies :
   bash
   pip install -r requirements.txt
   playwright install
2.  Run the project :
   bash
   python main.py
 Make sure you have Python and Playwright installed correctly. Chromium will auto-install on first run.

	Output
  Content from the URL is scraped and processed
  Final version is saved in ChromaDB
  You can run RL search to fetch the most relevant version
Developed By-
Muskan Singh 
BTech CSE-AIML
[GitHub](https://github.com/happiness-singh09)
