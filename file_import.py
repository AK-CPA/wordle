import os
import string

#Import Word List
word_file = open(os.path.expanduser("~/words.txt"))
word_list = []

for word in word_file:
    word_list.append(word.strip().lower())

#Import Name File
#name_file = open(os.path.expanduser("~/names.txt"))
#name_list = []

#for name in name_file:
#    name_list.append(name.strip().lower())

##Filter to Target List (5 letter words and no names)
target_list = [x for x in word_list if len(x) == 5]
#target_list = [x for x in target_list if x not in name_list]



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


##Find Most Advantageous Word
letter_count_1 = dict((key,0) for key in string.ascii_lowercase)
letter_count_2 = dict((key,0) for key in string.ascii_lowercase)
letter_count_3 = dict((key,0) for key in string.ascii_lowercase)
letter_count_4 = dict((key,0) for key in string.ascii_lowercase)
letter_count_5 = dict((key,0) for key in string.ascii_lowercase)

##Frequency of each letter in each position
for word in target_list:
    try:
        letter_count_1[word[0]] += 1
        letter_count_2[word[1]] += 1
        letter_count_3[word[2]] += 1
        letter_count_4[word[3]] += 1
        letter_count_5[word[4]] += 1
    except:
        target_list.remove(word)



##Score
def word_scoring_function(target_list):
    word_scoring_dict = dict.fromkeys(target_list, 0)
    for word in target_list:
        word_score = 0
        try:
            word_score += letter_count_1[word[0]]
            word_score += letter_count_2[word[1]]
            word_score += letter_count_3[word[2]]
            word_score += letter_count_4[word[3]]
            word_score += letter_count_5[word[4]]
            word_scoring_dict[word] = word_score
        except:
            continue

    top_word = list(dict(sorted(word_scoring_dict.items(), key=lambda item: item[1], reverse=True)).keys())[0:1]
    print(top_word[0])

##Top Word Analysis
#top_words = list(dict(sorted(word_scoring_dict.items(), key=lambda item: item[1], reverse=True)).keys())[0:6]
#print("The top words are:")
#print(*top_words, sep = " ")


for x in range(0,6):
    attempt = x+1
    word_guess = input("Word " + str(attempt) + " - Enter Word Guess:").lower()
    print("Enter Wordle Response Here")
    print("'x' for not in word")
    print("'y' for yellow response")
    print("'g' for green response")
    wordle_response = input("Enter Wordle response: ").lower()

    for i in range(0,5):

        if wordle_response[i] == 'x':
            target_list = [x for x in target_list if word_guess[i] not in x]

        if wordle_response[i] == 'g':
            target_list = [x for x in target_list if x[i] == word_guess[i]]

        if wordle_response[i] == 'y':
            target_list = [x for x in target_list if (x[i] != word_guess[i]) and (word_guess[i] in x)]

    print("the number of words remaining is:" , len(target_list))

    for word in target_list:
        print(word)

    "The most advantageous guess is:"
    word_scoring_function(target_list)
    print("There are " ,len(target_list),"word remaining")
###























