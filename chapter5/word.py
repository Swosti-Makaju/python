words = {
    "namaste": "hello",
    "paani": "water",
    "khana": "food",
    "sathi": "friend"
}

word = input("Enter Nepali word: ")

print("Meaning:", words.get(word, "Word not found"))