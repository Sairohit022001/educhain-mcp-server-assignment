import random
import json
from typing import Any, Optional, Union   

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import ollama

llm_model: Optional[Union[any, 'ollama', 'ChatOpenAI']] = None # type: ignore 



class EduChainContentGenerator:
    """
    Simulates the content generation capabilities of the educhain library.
    In a real scenario, this would wrap the actual educhain functions.
    """

    def __init__(self, llm: Optional[Union[any, 'Ollama', 'ChatOpenAI']] = None): # type: ignore # 
        self.llm = llm

    def generate_mcqs(self, topic: str, num_questions: int = 5) -> list[dict]:
        """
        Generates multiple-choice questions for a given topic. 
        This function simulates interaction with an LLM or educhain's MCQ generator. 
        """
        print(f"Generating {num_questions} MCQs on: {topic}")
        mcqs: list[dict] = [] 
        if self.llm:
            prompt_template = ChatPromptTemplate.from_messages([
                ("system", "You are an educational content generator. Create multiple-choice questions."),
                ("user", "Generate {num_questions} multiple-choice questions about '{topic}'. For each question, provide 4 options (A, B, C, D) and specify the correct answer. Format the output as a JSON array of objects, each with 'question', 'options' (an object with A, B, C, D keys), and 'correct_answer' keys.")
            ])

            chain = prompt_template | self.llm | StrOutputParser()

            try:
                llm_response_content: str = chain.invoke({"num_questions": num_questions, "topic": topic}) #  Type hint the response
                
                if not isinstance(llm_response_content, str):
                    raise TypeError("LLM response was not a string, cannot parse JSON.")

                json_start = llm_response_content.find("[")
                json_end = llm_response_content.rfind("]")

                if json_start != -1 and json_end != -1 and json_end > json_start:
                    json_string = llm_response_content[json_start : json_end + 1]
                    mcqs = json.loads(json_string)
                else:
                    print("Warning: LLM response did not contain valid JSON or was not parsed correctly. Generating mock MCQs.")
                    mcqs = self._generate_mock_mcqs(topic, num_questions)

            except json.JSONDecodeError as e:
                print(f"JSON decoding error: {e}. LLM response: {llm_response_content[:200]}...") #  Use typed variable
                mcqs = self._generate_mock_mcqs(topic, num_questions)
            except Exception as e:
                print(f"An error occurred during LLM interaction: {e}. Generating mock MCQs.")
                mcqs = self._generate_mock_mcqs(topic, num_questions)

        else:
            mcqs = self._generate_mock_mcqs(topic, num_questions)

        return mcqs

    def _generate_mock_mcqs(self, topic: str, num_questions: int) -> list[dict]:
        """Generates mock MCQs for demonstration purposes."""
        mock_data: list[dict] = [] #  Explicitly type the list
        for i in range(num_questions):
            question_text = f"What is a key concept in {topic} (Question {i+1})?"
            options_list = [
                f"Option A for {topic} {i+1}",
                f"Option B for {topic} {i+1}",
                f"Option C for {topic} {i+1}",
                f"Option D for {topic} {i+1}"
            ]
            correct_option = random.choice(['A', 'B', 'C', 'D'])
            options_dict = {chr(65+j): opt for j, opt in enumerate(options_list)}
            mock_data.append({
                "question": question_text,
                "options": options_dict,
                "correct_answer": correct_option
            })
        return mock_data

    def generate_lesson_plan(self, subject: str) -> dict:
        """
        Generates a lesson plan for a given subject. 
        Simulates interaction with an LLM or educhain's lesson plan generator. 
        """
        print(f"Generating lesson plan for: {subject}")
        lesson_plan: dict = {} 
        if self.llm:
            prompt_template = ChatPromptTemplate.from_messages([
                ("system", "You are an educational content generator, expert in creating structured lesson plans."),
                ("user", "Generate a detailed lesson plan for teaching '{subject}'. Include sections like 'Objective', 'Materials', 'Introduction', 'Main Activities', 'Assessment', and 'Conclusion'. Provide it as a JSON object.")
            ])

            chain = prompt_template | self.llm | StrOutputParser()

            try:
                llm_response_content: str = chain.invoke({"subject": subject}) 
                
                
                if not isinstance(llm_response_content, str):
                    raise TypeError("LLM response was not a string, cannot parse JSON.")

                json_start = llm_response_content.find("{")
                json_end = llm_response_content.rfind("}")

                if json_start != -1 and json_end != -1 and json_end > json_start:
                    json_string = llm_response_content[json_start : json_end + 1]
                    lesson_plan = json.loads(json_string)
                else:
                    print("Warning: LLM response did not contain valid JSON or was not parsed correctly. Generating mock lesson plan.")
                    lesson_plan = self._generate_mock_lesson_plan(subject)

            except json.JSONDecodeError as e:
                print(f"JSON decoding error: {e}. LLM response: {llm_response_content[:200]}...") # 
                lesson_plan = self._generate_mock_lesson_plan(subject)
            except Exception as e:
                print(f"An error occurred during LLM interaction: {e}. Generating mock lesson plan.")
                lesson_plan = self._generate_mock_lesson_plan(subject)
        else:
            lesson_plan = self._generate_mock_lesson_plan(subject)

        return lesson_plan

    def _generate_mock_lesson_plan(self, subject: str) -> dict:
        """Generates a mock lesson plan for demonstration purposes."""
        return {
            "subject": subject,
            "objective": f"Students will be able to understand the basic concepts of {subject}.",
            "materials": ["Whiteboard", "Markers", "Textbook for {subject}", "Worksheets"],
            "introduction": f"Begin with an engaging question about {subject} or a real-world example.",
            "main_activities": [
                f"Activity 1: Explain core theories of {subject}.",
                "Activity 2: Group discussion on practical applications.",
                "Activity 3: Problem-solving exercises related to {subject}."
            ],
            "assessment": "Short quiz or assignment at the end of the lesson.",
            "conclusion": f"Summarize key takeaways and preview the next topic in {subject}."
        }

    def generate_flashcards(self, topic: str, num_cards: int = 5) -> list[dict]:
        """
        Generates flashcards for a given topic (Bonus Task). 
        """
        print(f"Generating {num_cards} flashcards on: {topic}")
        flashcards: list[dict] = [] 
        if self.llm:
            prompt_template = ChatPromptTemplate.from_messages([
                ("system", "You are an educational content generator. Create flashcards for learning."),
                ("user", "Generate {num_cards} flashcards about '{topic}'. Each flashcard should have a 'front' (term/question) and a 'back' (definition/answer). Format the output as a JSON array of objects, each with 'front' and 'back' keys.")
            ])

            chain = prompt_template | self.llm | StrOutputParser()

            try:
                llm_response_content: str = chain.invoke({"num_cards": num_cards, "topic": topic}) #  Type hint the response
                
                #  Ensure llm_response_content is a string before calling .find()
                if not isinstance(llm_response_content, str):
                    raise TypeError("LLM response was not a string, cannot parse JSON.")

                json_start = llm_response_content.find("[")
                json_end = llm_response_content.rfind("]")

                if json_start != -1 and json_end != -1 and json_end > json_start:
                    json_string = llm_response_content[json_start : json_end + 1]
                    flashcards = json.loads(json_string)
                else:
                    print("Warning: LLM response did not contain valid JSON or was not parsed correctly. Generating mock flashcards.")
                    flashcards = self._generate_mock_flashcards(topic, num_cards)

            except json.JSONDecodeError as e:
                print(f"JSON decoding error: {e}. LLM response: {llm_response_content[:200]}...") # 
                flashcards = self._generate_mock_flashcards(topic, num_cards)
            except Exception as e:
                print(f"An error occurred during LLM interaction: {e}. Generating mock flashcards.")
                flashcards = self._generate_mock_flashcards(topic, num_cards)
        else:
            flashcards = self._generate_mock_flashcards(topic, num_cards)

        return flashcards

    def _generate_mock_flashcards(self, topic: str, num_cards: int) -> list[dict]:
        """Generates mock flashcards for demonstration purposes."""
        mock_data: list[dict] = [] #  Explicitly type the list
        for i in range(num_cards):
            mock_data.append({
                "front": f"Term {i+1} in {topic}",
                "back": f"Definition for Term {i+1} in {topic}"
            })
        return mock_data


if __name__ == "__main__":
    # To test with a real LLM, uncomment and configure one of the LLM options above.
    # edu_gen = EduChainContentGenerator(llm=Ollama(model="llama3"))
    # edu_gen = EduChainContentGenerator(llm=ChatOpenAI(model="gpt-3.5-turbo", api_key="YOUR_OPENAI_API_KEY"))
    
    edu_gen = EduChainContentGenerator(llm=llm_model) #  Using mock generator if no LLM configured

    print("\n--- Testing MCQ Generation ---")
    mcqs = edu_gen.generate_mcqs("Python Programming Basics", 3)
    print(json.dumps(mcqs, indent=2))

    print("\n--- Testing Lesson Plan Generation ---")
    lesson_plan = edu_gen.generate_lesson_plan("Algebra")
    print(json.dumps(lesson_plan, indent=2))

    print("\n--- Testing Flashcard Generation (Bonus) ---")
    flashcards = edu_gen.generate_flashcards("Linear Algebra Concepts", 2)
    print(json.dumps(flashcards, indent=2))