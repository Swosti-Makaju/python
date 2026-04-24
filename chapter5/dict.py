fav_lang = {}

for i in range(4):
    name = input("Enter friend's name: ")
    lang = input("Enter favorite language: ")
    fav_lang[name] = lang

print("Favorite languages:", fav_lang)