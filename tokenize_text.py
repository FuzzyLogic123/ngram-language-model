import re

def tokenize_text(text):
    text = text.replace('.', '\n')
    text = re.sub(r'[^\w\s]','', text)
    return text