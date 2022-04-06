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
        
# open allowed guesses for reading and create list of allowed guesses (incl answers)
# answers = []
# num_answers = 0
# with open('answers.txt', 'r') as reader:
#     line = reader.readline()
#     line = line.strip('[')
#     line = line.strip(']')
#     words = line.split(',')
#     for index in range(len(words)):
#         answers.append(words[index].strip('\"'))
#         num_answers += 1

print(str(num_answers) + ' number of answers read')
print('number of answers in list: ' + str(len(answers)))

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
print('Letter: Frequency')
for i in range(len(alphabet)):
    print(alphabet[i] + '   : ' + str(frequency[i]))

