# Letter template
letter = '''Dear <|Name|>,
You are selected!
<|Date|>
'''

# Inputs
name = input("Enter your name: ")
date = input("Enter the date (e.g., 16 April 2026): ")

# Replace placeholders
filled_letter = letter.replace("<|Name|>", name).replace("<|Date|>", date)

# Output
print("\n--- Filled Letter ---")
print(filled_letter)
