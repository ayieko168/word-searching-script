import csv
from serach_function import search_the_word

search_word = "antony" # the word to be searched
names = []

# Create a "names" list that is used as the search list
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




"""call the function"""
rest = search_the_word(word_dict, search_word)
print(rest)
pause = input("enter")
