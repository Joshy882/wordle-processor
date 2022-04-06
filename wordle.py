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

# # open allowed guesses for reading and create list of allowed guesses
# allowed = []
# num_allowed = 0
# with open('allowed.txt', 'r') as reader:
#     line = reader.readline()
#     line = line.strip('[')
#     line = line.strip(']')
#     words = line.split(',')
#     for index in range(len(words)):
#         allowed.append(words[index].strip('\"'))
#         num_allowed += 1
        
# print(str(num_allowed) + ' number of allowed guesses read')
# print('Number of allowed guesses in list: ' + str(len(allowed)))

# # combine answers and allowed lists to create master list
# allowed += answers
# print('Number of words in wordle list: ' + str(len(allowed)))


### 
# Find the single best starting word
###

# reorder alphabet based on frequency
print('\nAlphabet sorted by frequency')
zipped = list(zip(alphabet, frequency))
zipped.sort(key = lambda x: x[1], reverse=True)
a, f = zip(*zipped)
for i in range(len(zipped)):
    print(str(a[i]) + ' : ' + str(f[i]))
