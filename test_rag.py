import os
from dotenv import load_dotenv
from query_data_gemini import query_rag
from langchain_google_genai import GoogleGenerativeAI
load_dotenv(dotenv_path='.env')

EVAL_PROMPT = """
Expected Response: {expected_response}
Actual Response: {actual_response}
---
(Answer with 'true' or 'false') Does the actual response contain all the key information from the expected response? In other words, does the actual response mention all the items/names/facts from the expected response, regardless of formatting?
"""


def test_alice_in_wonderland():
    assert query_and_validate(
        question="Who are the three characters at the Mad Tea Party?",
        expected_response="The Mad Hatter, the March Hare, and the Dormouse.",
    )


def test_game_of_thrones_song_of_ice_and_fire():
    assert query_and_validate(
        question="What are the names of the Stark children's direwolves?",
        expected_response="Ghost, Nymeria, Summer, Shaggydog, Grey Wind, and Lady",
    )


def query_and_validate(question: str, expected_response: str):
    response_text = query_rag(question)
    prompt = EVAL_PROMPT.format(
        expected_response=expected_response, actual_response=response_text
    )

    model = GoogleGenerativeAI(
        model="gemini-flash-latest", google_api_key=os.environ['GEMINI_API_KEY'])
    response_text = model.invoke(prompt)
    evaluation_results_str_cleaned = response_text.strip().lower()

    print(prompt)

    if "true" in evaluation_results_str_cleaned:
        # Print response in Green if it is correct.
        print("\033[92m" +
              f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return True
    elif "false" in evaluation_results_str_cleaned:
        # Print response in Red if it is incorrect.
        print("\033[91m" +
              f"Response: {evaluation_results_str_cleaned}" + "\033[0m")
        return False
    else:
        raise ValueError(
            f"Invalid evaluation result. Cannot determine if 'true' or 'false'."
        )


if __name__ == "__main__":
    test_alice_in_wonderland()
    test_game_of_thrones_song_of_ice_and_fire()
