
search_word = "contents"
word_dict = ["contents", "concempt", "container", "contempt"]
names = []

def search_the_word(word_dict, search_word):

    i = 0
    total = 0
    do_you_mean = []
    match = None
    
    for word in word_dict:
        """go through each word in the word dictionary"""

        # clean the words ie: remove punctuation
        word = word.strip(",.\'\"!@#$%?<>^&*()_+/*-+").lower().replace(" ", "")
        search_word = search_word.strip(",.\'\"!@#$%?><^&*()_+/*-+").lower().replace(" ", "")

        #break the dictinary word to a list of letters
        word_letters = list(word)
        #break the search word to a list fo letters 
        search_word_letters = list(search_word)

        try:
            for x in search_word_letters:
                """look if the i'th letter of the dict word mathces to the search word"""
                if x == word_letters[i]:
                    # if they match, incerase the confidence score
                    total+=1
                else:
                    total = total + 0
                    # if no match, do nothing to the confidence score
                i+=1
        except:
            pass

        percentage_score = (total*100)/len(search_word) # the confidece score in percentage

        if percentage_score == 100:
            match = word
        elif (percentage_score >=45) and (percentage_score != 100) and (len(search_word) == (len(word)+3) or (len(word)-3)):
            do_you_mean.append(word)
        elif percentage_score <=10:
            pass

        # reset the i'th and total values to check the next dictionary word
        i = 0
        total = 0

    # print the list of close words
    print("do you mean :: ", do_you_mean)
    print("match :: ", match)

"""call the function"""

search_the_word(word_dict, search_word)
