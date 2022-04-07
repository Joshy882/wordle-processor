# Description

This program processes the list of Wordle answers found on the official New York Times game website, and determines the frequency of each letter. It will then pick the best starting combination of 1, 2, or 3 words based on the frequencies of letters.

# Best starting words

The best starting words, as of 7th April 2022, can be found in the text files in the output folder.

# Updating local Wordle lists

1. Go to the wordle website here: https://www.nytimes.com/games/wordle/index.html
2. Right-click anywhere on page and click `View page source`
3. Scroll to the bottom of the page and click on the link that looks like this: `main.3d28ac0c.js`
4. Scroll down to see the two lists of five letter words. They will be in the format `var Ma=[answers-list],Oa=[allowed-guesses-list]`. The list following `var Ma=` is the answers list. The list following `Oa=` is the allowed guesses list (not including the answers).
5. Copy the lists into their respective text files in the lists folder.

# Running the program

Note: you will need [Python](https://www.python.org/) installed to run the `wordle.py` program.

1. Open a bash terminal or command prompt in the same directory as the `wordle.py` program.
2. Run `python wordle.py` in the terminal.
