# Description: This script is used to modify the references in the text file.
# The script reads the input file and the keys file, and then replaces the references in the input file with the corresponding keys from the keys file.
import re

def modifier(input_file_path, keys_path, output_path):
    # Read to TXT and convert to list
    with open(keys_path, "r", encoding="utf-8") as file:
        references = [line.strip() for line in file.readlines()]

    # Read to Input TXT and convert to string
    with open(input_file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Find to references in string (example, (1, 2, 3, 4, 5, 6))
    pattern = r"\(([\d,\s]+)\)" # pattern for find references

    def replace_references(match):
        numbers = match.group(1)  # "1, 2, 3 , 4, 5, 6"
        ref_list = [int(num.strip()) - 1 for num in numbers.split(",")]  # Convert to integers to list
        ref_names = [references[i] for i in ref_list]  # Take to reference names
        # In the new format, add \cite{} and return
        return r"\cite{" + ", ".join(ref_names) + "}"  # return in \cite 

    # Change references in the text
    updated_text = re.sub(pattern, replace_references, text)

    # Write the updated text
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(updated_text)
    

modifier("GoogleScholarBibTeXAutomation\ReferencesModifierWithBibTeXKeys\inputText.txt","GoogleScholarBibTeXAutomation\ReferencesModifierWithBibTeXKeys\outputForKeys.txt","GoogleScholarBibTeXAutomation\ReferencesModifierWithBibTeXKeys\outputText.txt")
