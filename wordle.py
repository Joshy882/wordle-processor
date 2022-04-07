# Wordle Processor
#
# Process the list of Wordle answers to find the frequency of each letter.
# Find the best starting combinations of 1, 2, and 3 words based on the letter frequencies.

def get_list_from_file(file_name):
    """Open a text file containing a list and create a python list."""
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


# process the list of Wordle answers
answers, num_answers = get_list_from_file('lists/answers.txt')
print('\n' + str(num_answers) + ' number of answers read')
print('Number of answers in list: ' + str(len(answers)))

# create letter frequency table from answers list
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

# process the list of Wordle allowed guesses
allowed, num_allowed = get_list_from_file('lists/allowed.txt')
print('\n' + str(num_allowed) + ' number of allowed guesses read')
print('Number of allowed guesses in list: ' + str(len(allowed)))

# combine answers and allowed lists to create master list
master = allowed + answers
print('\nTotal number of words in wordle list: ' + str(len(master)))

# find the frequency of each letter in the answers list
with open('output/letter-frequencies.txt', 'w') as writer:
    writer.write('Frequency in alphabetical order\n')
    for i in range(len(alphabet)):
        line = alphabet[i] + ' : ' + str(frequency[i]) + '\n'
        writer.write(line)

    # reorder alphabet based on frequency
    writer.write('\nAlphabet sorted by frequency\n')
    zipped = list(zip(alphabet, frequency))
    zipped.sort(key=lambda x: x[1], reverse=True)
    a, f = zip(*zipped)
    for i in range(len(zipped)):
        line = str(a[i]) + ' : ' + str(f[i]) + '\n'
        writer.write(line)


def find_words(existing_words, search_words, num_top_letters):
    """Using the top num_top_letters most frequent letters, find suitable
    words from the search_words list that contain the letters that aren't
    in any of the words in the existing_words list."""
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


def list_to_string(list_of_strings):
    """Convert a list into a printable string."""
    str1 = '[ '
    for elem in list_of_strings:
        str1 += elem + ' '
    str1 += ']'
    return str1


# Find the single best starting word
# pick the five most common letters and look for matching word in answers
with open('output/singles.txt', 'w') as writer:
    writer.write('Best starting words that are accepted answers\n')
    top_six = 6
    first_words = find_words(['     '], answers, top_six)
    writer.write(list_to_string(first_words))
    writer.write('\n')
    writer.write('\nBest starting words that aren\'t accepted answers\n')
    top_five = 5
    first_words = find_words(['     '], master, top_five)
    line = list_to_string(first_words) + '\n'
    writer.write(line)
print('\nBest single starting words can be found in output/singles.txt')

# Find the two best starting words
# pick the ten most common letters and look for matching words in answers
with open('output/pairs.txt', 'w') as writer:
    writer.write('Best pairs of starting words\n')
    top_ten = 10
    first_words = find_words(['     '], answers, top_ten)
    for first_word in first_words:
        second_words = find_words([first_word], first_words, top_ten)
        if len(second_words) > 0:
            line = first_word + ' ' + list_to_string(second_words) + '\n'
            writer.write(line)
print('\nBest pairs of starting words can be found in output/pairs.txt')

# Find the three best starting words
# pick the fifteen most common letters and look for matching words in answers
with open('output/triplets.txt', 'w') as writer:
    writer.write('Best triplets of starting words\n')
    top_fifteen = 15
    first_words = find_words(['     '], answers, top_fifteen)
    for first_word in first_words:
        second_words = find_words([first_word], first_words, top_fifteen)
        for second_word in second_words:
            third_words = find_words(
                [first_word, second_word], second_words, top_fifteen)
            if len(third_words) > 0:
                line = first_word + ' ' + second_word + \
                    ' ' + list_to_string(third_words) + '\n'
                writer.write(line)
                break
print('\nBest triplets of starting words can be found in output/triplets.txt')

# Find the four best starting words
# pick the twenty most common letters and look for matching words in answers
with open('output/quadruplets.txt', 'w') as writer:
    writer.write('Best quadruplets of starting words\n')
    top_twenty = 20
    first_words = find_words(['     '], answers, top_twenty)
    for first_word in first_words:
        second_words = find_words([first_word], first_words, top_twenty)
        for second_word in second_words:
            comb_found = False
            third_words = find_words(
                [first_word, second_word], second_words, top_twenty)
            for third_word in third_words:
                fourth_words = find_words(
                    [first_word, second_word, third_word], third_words, top_twenty)
                if len(fourth_words) > 0:
                    line = first_word + ' ' + second_word + ' ' + \
                        third_word + ' ' + list_to_string(fourth_words) + '\n'
                    writer.write(line)
                    comb_found = True
                    break
            if comb_found:
                break
print('\nBest quadrulets of starting words can be found in output/quadruplets.txt')

# Find the next three best words after starting with 'crate'
# pick the twenty most common letters and look for matching words in answers
with open('output/crate-quadruplet.txt', 'w') as writer:
    writer.write(
        'Best quadrulets of starting words when starting with \'crate\'\n')
    top_twenty = 21
    first_words = ['crate']
    for first_word in first_words:
        second_words = find_words([first_word], answers, top_twenty)
        for second_word in second_words:
            third_words = find_words(
                [first_word, second_word], second_words, top_twenty)
            for third_word in third_words:
                fourth_words = find_words(
                    [first_word, second_word, third_word], third_words, top_twenty)
                if len(fourth_words) > 0:
                    line = first_word + ' ' + second_word + ' ' + \
                        third_word + ' ' + list_to_string(fourth_words) + '\n'
                    writer.write(line)
print('\nBest quadrulets of starting words when starting with \'crate\' can be found in output/crate-quadruplet.txt')
