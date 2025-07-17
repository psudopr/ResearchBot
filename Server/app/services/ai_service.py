import google.generativeai as genai
from app.core.config import Config

# Configure the Gemini API
# genai.configure(api_key=Config.GEMINI_API_KEY)

# model = genai.GenerativeModel('gemini-pro')

def summarize_text(text: str, user_narrative: str, global_prompt: str) -> dict:
    """Summarizes the text using the AI service."""

    # This is a placeholder for the actual implementation.
    # You will need to construct the prompt using the hierarchical
    # prompting structure (Global -> Company -> RSS).

    prompt = f"""Global Prompt: {global_prompt}

    User Narrative: {user_narrative}

    Article Text: {text}

    Please provide a three-tiered summary of the article text, taking into account the global prompt and the user narrative.

    The summary should be in the following format:
    - Summary Sentence: [A single compound sentence]
    - Summary Bullets: [Up to 6 bullet points]
    - Summary Narrative: [A narrative of up to 250 words that indicates alignment with the user narrative]
    """

    # response = model.generate_content(prompt)

    # This is a mock response for demonstration purposes.
    mock_response = {
        "summary_sentence": "This is a summary sentence.",
        "summary_bullets": [
            "This is a bullet point.",
            "This is another bullet point."
        ],
        "summary_narrative": "This is a summary narrative."
    }

    return mock_response
