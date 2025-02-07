import gradio as gr
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def summarize_text(text):
    payload = {
        "model": "deepseek-r1:7b",
        "prompt": f"Summarize the following text:\n\n{text}",
        "stream": False,
    }
    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No summary generated.")
    else:
        return f"Error:{response.text}"


# Test Summarization
if __name__ == "__main__":
    sample_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.
    Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions
    that maximize its chance of successfully achieving its goals.
    """
    print("Summary:")
    print(summarize_text(sample_text))
