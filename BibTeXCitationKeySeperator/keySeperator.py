import re

def keySeperator(input_file_path):
    # Citation Key Seperator from Bibtex File
    
    # Read the input file
    with open(input_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    content = content.split("@")
    content = content[1:]  # Skip the first element (it's empty)

    keys = []

    for bibtex in content:
        match = re.search(r"{(.*?),", bibtex)  # Gets the first value in the first curly bracket
        if match:
            keys.append(match.group(1))  # Add to first object to keys list
    with open("GoogleScholarBibTeXAutomation\BibTeXCitationKeySeperator\outputForKeys.txt", "w", encoding="utf-8") as output:
        for key in keys:
            output.write(f"{key}\n")

keySeperator("GoogleScholarBibTeXAutomation\BibTeXCitationKeySeperator\inputBibTeX.txt")