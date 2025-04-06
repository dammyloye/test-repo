def read_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()
            return content

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

    except PermissionError:
        print(f"Error: Permission denied to read file '{filename}'.")
        return None

    except OSError as e:
        print(f"Error: An OS error occurred while reading file '{filename}': {e}")
        return None

def main():
    # Ask the user for a filename
    filename = input("Please enter a filename: ")

    # Attempt to read the file
    content = read_file(filename)

    # If the file was read successfully, print its content
    if content is not None:
        print("File content:")
        print(content)

if __name__ == "__main__":
    main()

