###
# Process list of Wordle answers to find the frequency of each letter
###

# open answers for reading and create list of answers
answers = []
num_answers = 0
with open('answers.txt', 'r') as reader:
    line = reader.readline()
    line = line.strip('[')
    line = line.strip(']')
    words = line.split(',')
    for index in range(len(words)):
        answers.append(words[index].strip('\"'))
        num_answers += 1

print(str(num_answers) + ' number of answers read')
print('Number of answers in list: ' + str(len(answers)))

# create letter frequency table
alphabet = []
for alpha in range(ord('a'), ord('z') + 1):
    alphabet.append(chr(alpha))

frequency = [0] * len(alphabet)
for answer in answers:
    for i in range(5):
        letter = answer[i]
        letter_val = ord(letter)
        alphabet_index = letter_val - ord('a')
        frequency[alphabet_index] += 1

# print frequency of each letter in answers
print('\nFrequency in alphabetical order')
for i in range(len(alphabet)):
    print(alphabet[i] + ' : ' + str(frequency[i]))


# ###
# # Process list of Wordle allowed guesses
# ###

# open allowed guesses for reading and create list of allowed guesses
allowed = []
num_allowed = 0
with open('allowed.txt', 'r') as reader:
    line = reader.readline()
    line = line.strip('[')
    line = line.strip(']')
    words = line.split(',')
    for index in range(len(words)):
        allowed.append(words[index].strip('\"'))
        num_allowed += 1
        
print(str(num_allowed) + ' number of allowed guesses read')
print('Number of allowed guesses in list: ' + str(len(allowed)))

# combine answers and allowed lists to create master list
master = allowed + answers
print('Number of words in wordle list: ' + str(len(allowed)))

###
# reorder alphabet based on frequency
###
print('\nAlphabet sorted by frequency')
zipped = list(zip(alphabet, frequency))
zipped.sort(key = lambda x: x[1], reverse=True)
a, f = zip(*zipped)
for i in range(len(zipped)):
    print(str(a[i]) + ' : ' + str(f[i]))


### 
# Find the single best starting word
###

# def find_words(word_list, num_top_letters):
#     first_words = word_list.copy()
#     num_letters = num_top_letters
#     for j in range(len(first_words)-1, -1, -1):
#         num_contained = 0
#         for i in range(num_letters):
#             if a[i] in first_words[j]:
#                 num_contained += 1
#         if num_contained < 5:
#             del first_words[j]

#     if len(words) > 0:
#         return find_words(words, num_letters)
#     else:
#         return words

def find_words(word_list, num_top_letters):
    words = word_list.copy()
    num_letters = num_top_letters
    for j in range(len(words)-1, -1, -1):
        num_contained = 0
        for i in range(num_letters):
            if a[i] in words[j]:
                num_contained += 1
        if num_contained < 5:
            del words[j]
    return words

def find_words_2(existing_word, search_words, num_top_letters):
    first_word = str(existing_word)
    words = search_words.copy()
    for j in range(len(words)-1, -1, -1):
        num_contained = 0
        for i in range(num_top_letters):
            if a[i] not in first_word and a[i] in words[j]:
                num_contained += 1
        if num_contained < 5:
            del words[j]
    return words

def find_words_3(existing_words, search_words, num_top_letters):
    first_words = existing_words.copy()
    words = search_words.copy()
    for j in range(len(words)-1, -1, -1): # loop through potential next words
        num_contained = 0
        for i in range(num_top_letters): # loop through letters
            contained = False
            for k in range(len(first_words)): # loop through existing words
                if a[i] in first_words[k]:
                    contained = True
            if not contained and a[i] in words[j]:
                num_contained += 1
        if num_contained < 5:
            del words[j]
    return words
    


# pick the five most common letters and look for matching word in answers
top_five = 5
# single = answers.copy()
# for j in range(len(single)-1, -1, -1):
#     for i in range(top_five):
#         if a[i] not in single[j]:
#             del single[j]
#             break

# if (len(single) == 0):
#     print('No single best starting word found in answers list. Retrying with master list...')
#     # repeat with master list guesses
#     single = master.copy()
#     for j in range(len(single)-1, -1, -1):
#         for i in range(top_five):
#             if a[i] not in single[j]:
#                 del single[j]
#                 break
    
#     if (len(single) == 0):
#         print('No single best starting word found in master list.')
#     else:
#         print(single)
# else:
#     print(single)




single = master.copy()
for j in range(len(single)-1, -1, -1):
    for i in range(top_five):
        if a[i] not in single[j]:
            del single[j]
            break

if (len(single) == 0):
    print('No single best starting word found in master list.')
else:
    print(single)

single = master.copy()
print()
# print(find_words(single, 15))
print()
# print(find_words_2('chord', single, 15))
print()
# print(find_words_3(['chord','aunts'], single, 16))

# one_word = find_words_3(['     '], master, 26)

test_list = answers.copy()

first_words = find_words_3(['     '], test_list, 15)
for first_word in first_words:
    second_words = find_words_3([first_word], first_words, 15)
    for second_word in second_words:
        third_words = find_words_3([first_word,second_word], second_words, 15)
        if len(third_words) > 0:
            print(first_word, second_word, third_words)



# ### 
# # Find the two best starting words
# ###

# # pick the ten most common letters only look at answers that contain five of the ten letters
# top_ten = 10
# suitable_first = 0
# double_first = master.copy() # master.copy()
# for j in range(len(double_first)-1, -1, -1):
#     num_contained = 0
#     for i in range(top_ten):
#         if a[i] in double_first[j]:
#             num_contained += 1
#     if num_contained < 5:
#         del double_first[j]
#     else:
#         suitable_first += 1
#         # print(double_first[j])
#         # first word is good, find the second word
#         double_second = find_words_2(double_first[j], double_first, top_ten)
#         if len(double_second) > 0:
#             print(double_first[j])
#             print(double_second)
#         # else:
#         #     print('No suitable second word for ' + double_first[j])

# print(suitable_first)


# # pick the fifteen most common letters and make three words out of them
# suitable_first_words = find_words_2('     ', master, 10)
# print(suitable_first_words)
# print(len(suitable_first_words))
# suitable_first_words = find_words_3(['     '], master, 10)
# print(suitable_first_words)
# print(len(suitable_first_words))