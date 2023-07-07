import os
import tempfile
from code_to_text.main import write_files_to_markdown, get_files_in_dir, get_code_language

def test_get_files_in_dir():
    """
    Test the get_files_in_dir function by creating a temporary directory with 
    files of different extensions and checking that it only returns the ones with the correct extensions.
    """
    with tempfile.TemporaryDirectory() as temp_dir:  
        file_exts = ['py', 'txt', 'java']  # Create some test files with these extensions
        exclude_files = ['exclude.py']
        files = [f'test.{ext}' for ext in file_exts] + exclude_files  # List of file names
        for file in files:  # Create each file in the temp directory
            open(os.path.join(temp_dir, file), 'w').close()

        code_files = list(get_files_in_dir(temp_dir, ['py', 'java'], exclude_files))  # Get the code files in the temp directory
        assert len(code_files) == 2  # There should be two code files: 'test.py' and 'test.java'
        assert os.path.join(temp_dir, 'test.txt') not in code_files  # The .txt file should not be included
        assert os.path.join(temp_dir, 'exclude.py') not in code_files  # The 'exclude.py' file should not be included

def test_get_code_language():
    """
    Test the get_code_language function by checking it returns the correct language for a few test cases.
    """
    assert get_code_language('test.py') == 'python'  # Python files should return 'python'
    assert get_code_language('test.java') == 'java'  # Java files should return 'java'
    assert get_code_language('test.unknown') == 'nohighlight'  # Files with an unknown extension should return 'nohighlight'

def test_write_files_to_markdown():
    """
    Test the write_files_to_markdown function by creating a temporary directory with a test Python file,
    running the function, and checking the contents of the output file.
    """
    with tempfile.TemporaryDirectory() as temp_dir:  
        input_file_path = os.path.join(temp_dir, 'test.py')  # Path to the input file
        with open(input_file_path, 'w') as f:
            f.write('print("Hello, world!")')  # Write some test code to the input file

        output_file_path = os.path.join(temp_dir, 'output.md')  # Path to the output file
        write_files_to_markdown(temp_dir, output_file_path, ['py'], [])  # Run the function

        with open(output_file_path, 'r') as f:
            contents = f.read()  # Read the contents of the output file
            # The output file should contain the filename, the start of a code block with the correct language, the code, and the end of the code block
            assert contents == 'test.py\n```python\nprint("Hello, world!")\n```\n\n'
