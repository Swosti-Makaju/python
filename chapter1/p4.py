import os

def list_directory_contents(path="."): #print all files and folders in the given directory
    """
    Prints all files and folders in the given directory.
    :param path: Directory path (default is current directory)
    """
    try:
        # Validate if the path exists and is a directory
        if not os.path.exists(path):
            print(f"Error: The path '{path}' does not exist.")
            return
        if not os.path.isdir(path):
            print(f"Error: '{path}' is not a directory.")
            return

        print(f"Contents of directory: {os.path.abspath(path)}")
        items = os.listdir(path)  # Get list of files and folders

        if not items:
            print("The directory is empty.")
        else:
            for item in items:
                print(item)

    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
# You can replace "." with any directory path, e.g., "C:/Users/YourName/Documents"
list_directory_contents(".")
