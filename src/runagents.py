#!/usr/bin/env python3
from crew import crew

if __name__ == "__main__":
    print("🚀 Spouštím CrewAI na velkém projektu...")
    result = crew.kickoff()
    print("✅ Výsledek:")
    print(result)
