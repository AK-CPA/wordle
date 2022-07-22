import os

#Import Word List
word_file = open(os.path.expanduser("~/wordlist.txt"))
word_list = []

for word in word_file:
    word_list.append(word.strip().lower())


##Filter to Target List (5 letter words and no names)
target_list = [x for x in word_list if len(x) == 5]


for word in target_list:
    if word.find("'") >= 0:
        target_list.remove(word)
    if word.find("-") >= 0:
        target_list.remove(word)
    if word.find(")") >= 0:
        target_list.remove(word)
    if word.find("/") >= 0:
        target_list.remove(word)
    if ' ' in word:
        target_list.remove(word)

print(f"The number of words is {len(target_list)}")

with open(os.path.expanduser("~/five_letter_words.txt") , 'w') as f:
    for line in target_list:
        f.write(f"{line}\n")


