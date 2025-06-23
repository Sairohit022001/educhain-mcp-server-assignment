import requests
import json
import os

BASE_URL = "http://127.0.0.1:8000"
OUTPUT_FILE = "Sample_Responses.txt"

def write_to_file(content):
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(content + "\n\n")

def clear_output_file():
    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)
    print(f"Cleared existing {OUTPUT_FILE}")

def main():
    clear_output_file()
    write_to_file("--- EduChain MCP Server Sample Commands and Responses ---\n")
    write_to_file(f"Server Base URL: {BASE_URL}\n")

    print(f"Generating sample responses to '{OUTPUT_FILE}'...")

    # Test Case 1: Generate 5 multiple-choice questions on Python loops.
    command_mcq = "Generate 5 multiple-choice questions on Python loops."
    write_to_file(f"User Command: \"{command_mcq}\"")
    print(f"\nProcessing: {command_mcq}")
    try:
        response = requests.post(f"{BASE_URL}/tools/generate_mcqs", json={"topic": "Python loops", "num_questions": 5})
        response.raise_for_status() 
        mcq_response = response.json()
        write_to_file(f"Server Endpoint: POST {BASE_URL}/tools/generate_mcqs")
        write_to_file(f"Request Payload: {json.dumps({'topic': 'Python loops', 'num_questions': 5}, indent=2)}")
        write_to_file(f"Server Response (MCQs):\n{json.dumps(mcq_response, indent=2)}")
        print("MCQ generation successful.")
    except requests.exceptions.RequestException as e:
        write_to_file(f"Error processing MCQ command: {e}")
        print(f"Error processing MCQ command: {e}")
    except json.JSONDecodeError as e:
        write_to_file(f"Error decoding JSON response for MCQ command: {e}")
        print(f"Error decoding JSON response for MCQ command: {e}")
    write_to_file("-" * 80)

    # Test Case 2: Provide a lesson plan for teaching algebra.
    command_lesson_plan = "Provide a lesson plan for teaching algebra."
    write_to_file(f"User Command: \"{command_lesson_plan}\"")
    print(f"\nProcessing: {command_lesson_plan}")
    try:
        response = requests.get(f"{BASE_URL}/resources/lesson_plan?subject=algebra")
        response.raise_for_status()
        lesson_plan_response = response.json()
        write_to_file(f"Server Endpoint: GET {BASE_URL}/resources/lesson_plan?subject=algebra")
        write_to_file(f"Server Response (Lesson Plan):\n{json.dumps(lesson_plan_response, indent=2)}")
        print("Lesson plan generation successful.")
    except requests.exceptions.RequestException as e:
        write_to_file(f"Error processing Lesson Plan command: {e}")
        print(f"Error processing Lesson Plan command: {e}")
    except json.JSONDecodeError as e:
        write_to_file(f"Error decoding JSON response for Lesson Plan command: {e}")
        print(f"Error decoding JSON response for Lesson Plan command: {e}")
    write_to_file("-" * 80)

    # Test Case 3 (Bonus): Generate 3 flashcards on Calculus concepts.
    command_flashcards = "Generate 3 flashcards on Calculus concepts."
    write_to_file(f"User Command: \"{command_flashcards}\"")
    print(f"\nProcessing: {command_flashcards}")
    try:
        response = requests.post(f"{BASE_URL}/tools/generate_flashcards", json={"topic": "Calculus concepts", "num_cards": 3})
        response.raise_for_status()
        flashcards_response = response.json()
        write_to_file(f"Server Endpoint: POST {BASE_URL}/tools/generate_flashcards")
        write_to_file(f"Request Payload: {json.dumps({'topic': 'Calculus concepts', 'num_cards': 3}, indent=2)}")
        write_to_file(f"Server Response (Flashcards):\n{json.dumps(flashcards_response, indent=2)}")
        print("Flashcard generation successful.")
    except requests.exceptions.RequestException as e:
        write_to_file(f"Error processing Flashcards command: {e}")
        print(f"Error processing Flashcards command: {e}")
    except json.JSONDecodeError as e:
        write_to_file(f"Error decoding JSON response for Flashcards command: {e}")
        print(f"Error decoding JSON response for Flashcards command: {e}")
    write_to_file("-" * 80)

    print(f"\nSample responses saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()