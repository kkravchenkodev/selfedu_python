import pprint
from string import punctuation, digits, whitespace

message = input()
print(message)

skip = punctuation + digits + whitespace
for ch in skip:
    if ch in message:
        message = message.replace(ch, '')
print(message)
count = {}

for character in message.lower():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
