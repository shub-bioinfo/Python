
import os

#Try for exception handling, if file exist in the folder or not.
try:
    # Get the list of all files in the current directory
    files = os.listdir('.')

    # Filter files with .pdb extension
    pdb_files = [file for file in files if file.endswith('.pdb')]

    if not pdb_files:
        raise FileNotFoundError("No .pdb files found in the current directory.")

    # Store the name of the first .pdb file without the extension
    pdb_filename_without_extension = os.path.splitext(pdb_files[0])[0]

    print(f"Found .pdb file: {pdb_files[0]}")
    print(f"Filename without extension: {pdb_filename_without_extension}")

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

