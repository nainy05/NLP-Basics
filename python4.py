import re

sentence = "Hello I am Nainy Jain"

# print(re.match(r"[a-zA-Z ]*",sentence))

# print(re.match("1996$",sentence))

print(re.sub(r"[a-z]","0", sentence,1, flags = re.I))
