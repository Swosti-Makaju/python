# Program to detect double spaces in a string

def detect_double_space(text):
    """
    Detects if there is any double space in the given text.
    Returns a list of positions (indices) where double spaces occur.
    """
    positions = []
    index = text.find("  ")  # Find first occurrence of double space
    while index != -1:
        positions.append(index)
        index = text.find("  ", index + 1)  # Search for next occurrence
    return positions

def main():
    try:
        # Get user input
        text = input("Enter a string: ")
        
        # Detect double spaces
        positions = detect_double_space(text)
        
        if positions:
            print(f"Double spaces found at positions: {positions}")
        else:
            print("No double spaces found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
