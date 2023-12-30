def extsort(file_list):
    # Define a custom sorting key function that extracts the file extension
    def get_extension(filename):
        return filename.split('.')[-1]

    # Sort the list of files based on their extensions
    sorted_files = sorted(file_list, key=get_extension)

    return sorted_files

# Example usage:
file_list = ["file.txt", "image.png", "document.docx", "script.py"]
sorted_files = extsort(file_list)
print(sorted_files)
