import re
import sys

def slugify(text):
    # Convert to lowercase
    text = text.lower()
    # Replace non-alphanumeric characters (excluding spaces) with nothing
    text = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces and underscores with hyphens
    text = re.sub(r'[\s_]+', '-', text)
    # Remove leading/trailing hyphens
    text = text.strip('-')
    return text


if len(sys.argv) > 1:
    input_text = " ".join(sys.argv[1:])
else:
    input_text = input("Enter your title: ")

slug = slugify(input_text)
print(slug)
