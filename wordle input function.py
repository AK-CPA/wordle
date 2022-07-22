
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























