
# load prompt completion pairs using a directory of pdf files with each pdf being a prompt completion pair
import os
import fitz
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_prompt_completion_pairs_from_text(text):
    pairs = re.findall(r"Prompt: (.*)\nCompletion: (.*)", text)
    return pairs

prompt_completion_pairs = []
def load_prompt_completion_pairs_from_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            text = extract_text_from_pdf(pdf_path)
            pairs = extract_prompt_completion_pairs_from_text(text)
            prompt_completion_pairs.extend(pairs)

load_prompt_completion_pairs_from_directory("prompt_completion_pairs")

# prepare the prompt completion pairs as a list of dictionaries
def prepare_documents():
    return [
        {"prompt": prompt, "completion": completion}
        for prompt, completion in prompt_completion_pairs
    ]   