# open answers for reading and create list of answers
answers = []
lines = 0
with open('wordle-nyt-answers-alphabetical.txt', 'r') as reader:
    while True:
        line = reader.readline()
        if line == '':
            print('End of file')
            break
        else:
            lines += 1
            line = line.strip('\n')
            answers.append(line)

print(str(lines) + ' lines read')
print('number of answers: ' + str(len(answers)))
print(str(answers[10]))
print(str(answers[100]))
print(str(answers[1000]))
print(str(answers[lines-1]))
print(str(answers[-1]))
