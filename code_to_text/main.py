""" 
Get all code from project into one markdown or txt file - useful for inputting code to LLMs.
"""

import os
from pygments.lexers import get_lexer_for_filename, ClassNotFound

def get_files_in_dir(dir_path, code_extensions, exclude_files):
    """
    Generate all file paths in a directory and its subdirectories, 
    excluding files with certain names or extensions.
    """
    for dirpath, _, filenames in os.walk(dir_path):  # Iterate over all directories and files in the given directory
        for filename in filenames:  # Iterate over each file in the current directory
            if filename in exclude_files:  # If the file is in the exclude list, skip it
                continue
            ext = os.path.splitext(filename)[1][1:]  # Get the file extension without the dot
            if ext in code_extensions:  # If the file extension is in the list of code file extensions, yield the file
                yield os.path.join(dirpath, filename)

def get_code_language(filename):
    """
    Get the language of a file based on its filename. If the language can't be determined,
    default to 'nohighlight'.
    """
    try:
        language = get_lexer_for_filename(filename).name.lower()
    except ClassNotFound:  # If pygments can't determine the language, default to 'nohighlight'
        language = 'nohighlight'
    return language

def write_files_to_markdown(dir_path, output_path, code_extensions, exclude_files):
    """
    Write all code files in a directory and its subdirectories to a markdown or txt file.
    Each section of code is preceded by the filename and language, enclosed in markdown code fences.
    """
    with open(output_path, 'w') as output_file:  # Open the output file in write mode
        # Iterate over all code files in the directory and its subdirectories
        for file_path in get_files_in_dir(dir_path, code_extensions, exclude_files):
            lang = get_code_language(file_path)  # Get the language of the current file
            output_file.write(f'{os.path.basename(file_path)}\n')  # Write the filename to the output file
            output_file.write(f'```{lang}\n')  # Write the start of a markdown code block, with the language specifier
            with open(file_path, 'r') as code_file:  # Open the current file in read mode
                code = code_file.read()  # Read the contents of the file
                output_file.write(code)  # Write the contents to the output file
            output_file.write('\n```\n\n')  # Write the end of the markdown code block

if __name__ == "__main__":
    # Define the path to the directory to read files from, and the path to the output file
    dir_path = 'DS_toolbox/box_1_data_collection/web_extraction_tools'
    output_path = dir_path + '/allcode.txt' # change extension to .md if you want change to markdown output
    # Define a list of file extensions that are considered to be code
    code_extensions = ['py', 'java', 'js', 'cpp', 'c', 'rb', 'go', 'rs']  
    # Define a list of filenames to exclude
    exclude_files = ['__init__.py']
    # Call the function to write all code files to the output file
    write_files_to_markdown(dir_path, output_path, code_extensions, exclude_files)
