import os
import subprocess

# Define the paths to your folders
FOLDER_1 = "/path/to/folder1"  # Folder for tagging with 'Comics & Graphic Novels'
FOLDER_2 = "/path/to/folder2"  # Folder for tagging and downloading metadata
FOLDER_3 = "/path/to/folder3"  # Folder for downloading metadata only

# Define the Calibre library path
CALIBRE_LIBRARY = "/path/to/your/calibre/library"

# Tag for comics and graphic novels
TAG = "Comics & Graphic Novels"

def import_to_calibre(folder, tag=None, download_metadata=False):
    # Supported file extensions
    extensions = ('.cbz', '.cbr', '.pdf', '.epub')
    
    for filename in os.listdir(folder):
        if filename.endswith(extensions):
            file_path = os.path.join(folder, filename)
            cmd = ['calibredb', 'add', '--library-path', CALIBRE_LIBRARY, file_path]
            
            # Add tag if provided
            if tag:
                cmd += ['--tags', tag]
            
            # Download metadata if specified
            if download_metadata:
                cmd += ['--with-library-path', CALIBRE_LIBRARY, '--download-metadata']
            
            # Execute the command
            print(f"Importing '{file_path}' with command: {' '.join(cmd)}")
            subprocess.run(cmd)

# Import files from each folder with specified options
import_to_calibre(FOLDER_1, TAG, False)  # Folder 1: Tag only
import_to_calibre(FOLDER_2, TAG, True)   # Folder 2: Tag and download metadata
import_to_calibre(FOLDER_3, None, True)  # Folder 3: Download metadata only

print("Import process completed.")
