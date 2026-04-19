text = "This  is  problem  3"
text = text.replace("  ", " ")
print(text)

text = "This   is    problem   3"
text = " ".join(text.split())
print(text)

import re

text = "This   is    problem   3"
text = re.sub(r"\s+", " ", text)
print(text)
