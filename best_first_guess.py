import os
import string

#Import Word List
word_file = open(os.path.expanduser("~/five_letter_words.txt"))
target_list = []

for word in word_file:
    target_list.append(word.strip().lower())

##Initialize Letter Dictionaries
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

    top_word = list(dict(sorted(word_scoring_dict.items(), key=lambda item: item[1], reverse=True)).keys())[0:2]
    print(f"The top two words as a starting guess are: {' and '.join(str(x) for x in top_word)}")

word_scoring_function(target_list)

