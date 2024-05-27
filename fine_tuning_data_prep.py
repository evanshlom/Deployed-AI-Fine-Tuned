import os
import fitz

prompt_completion_pairs = []
def load_prompt_completion_pairs_from_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            doc = fitz.open(pdf_path)
            for page in doc:
                text = page.get_text()
                prompt_completion_pairs.append({"prompt": text, "completion": text})

load_prompt_completion_pairs_from_directory("prompt_completion_pairs")

def prepare_documents():
    '''prepare your data as a list of dictionaries, with "prompt" and "completion" keys
    outputs:
        data = [
            {"prompt": "prompt1", "completion": "completion1"},
            {"prompt": "prompt2", "completion": "completion2"},
            ...]
    '''
    return prompt_completion_pairs

