import csv

search_word = "antony" # the word to be searched
names = []

with open("baby-names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print("line one")
            line_count += 1
            # ignore the first line of the csv file
        else:
            names.append(row[1])
            line_count += 1
    print(f'Processed {line_count} lines.')
##    print(names)

with open("names.txt", "w") as nam:
    nam.write(str(names))

word_dict = names


def search_the_word(search_word, word_dict):

    i = 0
    total = 0
    do_you_mean = []
    match = None
    
    for word in word_dict:
        """go through each word in the word dictionary"""

        word = word.strip(",.\'\"").lower().replace(" ", "")
        search_word = search_word.strip().lower().replace(" ", "")


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

        if (percentage_score == 100) and len(word) == len(search_word):
            match = word
        elif (percentage_score >=70) and (percentage_score != 100) and (len(search_word) == (len(word)+1) or (len(word)-1)):
            do_you_mean.append(word)
        elif percentage_score <=10:
            pass


        # reset the i'th and total values to check the next dictionary word
        i = 0
        total = 0

    do_you_mean = list(dict.fromkeys(do_you_mean))
    # print the list of close words
    print("do you mean :: ", do_you_mean)
    print("match :: ", match)

"""call the function"""
search_the_word(search_word, word_dict)
