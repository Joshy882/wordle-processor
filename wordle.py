###
# Process list of Wordle answers to find the frequency of each letter
###

def get_list_from_file(file_name):
    data_list = []
    datum_read = 0
    with open(file_name, 'r') as reader:
        line = reader.readline()
        line = line.strip('[')
        line = line.strip(']')
        words = line.split(',')
        for index in range(len(words)):
            data_list.append(words[index].strip('\"'))
            datum_read += 1
    return data_list, datum_read


# open answers for reading and create list of answers
answers, num_answers = get_list_from_file('lists/answers.txt')
print('\n' + str(num_answers) + ' number of answers read')
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


###
# Process list of Wordle allowed guesses
###

# open allowed guesses for reading and create list of allowed guesses
allowed, num_allowed = get_list_from_file('lists/allowed.txt')
print('\n' + str(num_allowed) + ' number of allowed guesses read')
print('Number of allowed guesses in list: ' + str(len(allowed)))

# combine answers and allowed lists to create master list
master = allowed + answers
print('\nTotal number of words in wordle list: ' + str(len(master)))


###
# reorder alphabet based on frequency
###
print('\nAlphabet sorted by frequency')
zipped = list(zip(alphabet, frequency))
zipped.sort(key=lambda x: x[1], reverse=True)
a, f = zip(*zipped)
for i in range(len(zipped)):
    print(str(a[i]) + ' : ' + str(f[i]))


###
# functions for finding words
###


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
    for j in range(len(words)-1, -1, -1):  # loop through potential next words
        num_contained = 0
        for i in range(num_top_letters):  # loop through letters
            contained = False
            for k in range(len(first_words)):  # loop through existing words
                if a[i] in first_words[k]:
                    contained = True
            if not contained and a[i] in words[j]:
                num_contained += 1
        if num_contained < 5:
            del words[j]
    return words


# need to write to file because it is too long. can make it shorter by only remembering unique triplets
def list_to_string(list_of_strings):
    str1 = '[ '
    for elem in list_of_strings:
        str1 += elem + ' '
    str1 += ']'
    return str1


###
# Find the single best starting word
# pick the five most common letters and look for matching word in answers
###

with open('output/singles.txt', 'w') as writer:
    writer.write('Best starting words that are accepted answers\n')
    top_six = 6
    first_words = find_words_3(['     '], answers, top_six)
    writer.write(list_to_string(first_words))
    writer.write('\n')

    writer.write('\nBest starting words that aren\'t accepted answers\n')
    top_five = 5
    first_words = find_words_3(['     '], master, top_five)
    writer.write(list_to_string(first_words))
    writer.write('\n')

print('\nBest single starting words can be found in output/singles.txt')


###
# Find the two best starting words
# pick the ten most common letters and look for matching words in answers
###

with open('output/pairs.txt', 'w') as writer:
    writer.write('Best pairs of starting words\n')
    top_ten = 10
    first_words = find_words_3(['     '], answers, top_ten)
    for first_word in first_words:
        second_words = find_words_3([first_word], first_words, top_ten)
        if len(second_words) > 0:
            line = first_word + ' ' + list_to_string(second_words)
            writer.write(line)
            writer.write('\n')

print('\nBest pairs of starting words can be found in output/pairs.txt')


###
# Find the two best starting words
# pick the ten most common letters and look for matching words in answers
###

with open('output/triplets.txt', 'w') as writer:
    writer.write('Best triplets of starting words\n')
    top_fifteen = 15
    first_words = find_words_3(['     '], answers, top_fifteen)
    for first_word in first_words:
        second_words = find_words_3([first_word], first_words, top_fifteen)
        for second_word in second_words:
            third_words = find_words_3(
                [first_word, second_word], second_words, top_fifteen)
            if len(third_words) > 0:
                line = first_word + ' ' + second_word + \
                    ' ' + list_to_string(third_words)
                writer.write(line)
                writer.write('\n')

print('\nBest triplets of starting words can be found in output/triplets.txt')
