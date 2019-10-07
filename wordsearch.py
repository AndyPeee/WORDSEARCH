import random
print("WORDSEARCH")
print("please only submit each word once") # sets rules for game
gameon = True #starts the while statement
answerlistrow, answerlistcol = [], [] #creates the lists that will be used for starting coordinates for each word
score = 0 #sets the score
alphabet="abcdefghijklmnopqrstuvwxyz" #sets a string of letters to be taken from later

'''
This next function takes the players input of a word they think they see and checks it against the words in the
gamewords.txt file (the file which contains the words used for the game). If the word is in the file, the score
increases. If it is not it tells the player to keep looking. It returns the score to be used to check how many times
to continue doing the function (it does this by increasing the value in the while loop that ends the loop once it hits
a certain number)
'''


def are_you_right(score,numofwords):  # uses score to change score value, uses numofwords to tell user how may words to go
    right = open("gamewords.txt", "r")  # opens the file with the answers
    wrong = right.read()  # turns the answer words into a variable that can be checked
    guess = input("what word do you see? ")  # asks the user for the word they guess
    if guess in wrong:  # checks to see if the guess is in the answer list
        score = score+1  # increases score, which means this function will run one less time each right answer
        print("Amount of words solved: "+str(score)+str("/")+str(numofwords))  # tells the user that they were right and how many words remain
    else:
        print("That word isn't in the search, try again")  # tells the user that they were wrong
    return score  # returns score to increase the value in the while loop to end once all words are chosen


'''
This next function randomly determines whether a word will be placed into the wordsearch forward or backword
'''


def fwdbwd():
    fwdorbwd = random.randint(1, 2)  # makes a 50/50 chance of the word being forward or backward
    if fwdorbwd == 1:
        return True  # returns true if the word is to be forward
    if fwdorbwd == 2:
        return False  # returns false if the word is to backward


'''
This next function randomly generates a list of words to be used for the game. It does this by picking from a txt file
by selecting a random number and using that number as the index value for the txt file. It then writes these words
to a seperate txt file where the words will be used later during the game
'''


def wordpicker():
    gamewords = []  # sets the list to append the numbers associated with the words used in the game
    first_time = True  # used for writing words to the gamewords txt file
    for words in range(numofwords):  # picks a random number for each word that should be in the game, based on difficulty
        rndmnm = random.randint(0, 660)
        if first_time:  # appends the number to the list
            gamewords.append(rndmnm)
            e = 0  # if its the first time, sets e to 0 to be used as the initial index number so the list restarts properly if the player wants to play again
        else:
            if rndmnm != gamewords:
                gamewords.append(rndmnm)
    file = open("listofwords.txt", "r")  # reads the txt file where the numbers will be converted to
    words = file.readlines()  # reads all the lines in the file
    for num in range(len(gamewords)):  # looks through each of the words in the list
        gamewords[num] = words[gamewords[num]].strip()  # removes the \n property from the words
    gmwrds = open("gamewords.txt", "w")  # opens the new txt file to write the new words to
    for w in gamewords:
        if e-1 != numofwords:
            wordsforthegame = gmwrds.write(str(gamewords[e]+str(" ")))  # writes the words to the new file, ensures that there is a space inbetween each word
            e = e+1
        else:
            wordsforthegame = gmwrds.write(str(gamewords[e]))  # same as above, but used for the first word


'''
This next function decides on where the word will be placed. It does this by selecting the first word and deciding on a 
random row and column. It then checks if the place chosen is already taken, and if so randomly picks a new location
It also decides if a word will go into the grid forward or backward. Finally, it prints the grid to be seen by the
player
'''


def wordplacement():
    answerlistrow = []  # used to see if the row has been used before
    answerlistcol = []  # used to see if the column has been used before
    wordplacer = open("gamewords.txt", "r")  # reads the txt file to be used for the game
    words = wordplacer.read().split(" ")  # splits apart the different words in the text file
    words.pop()  # there was an error in which the computer thought that the extra space at the end of the document was a word, this gets rid of the last word in the file, thus getting rid of the last space
    for theword in words:  # looks through each word in the file individually
        maxcol = length - len(theword)  # finds the maximum column the word could be in based off of the length of the word and the length of the grid
        row = random.randint(0, length-1)  # finds a random row based on the size of the grid
        col = random.randint(0, maxcol-1)  # finds a random column based on the maximum column it could fit in
        firstletter = True  # next couple lines set variables
        wordvalue = 0
        repeating = 1
        if not fwdbwd():  # calls the function to randomly decide on whether the word is forward or backwards
            theword = theword[::-1]  # checks through each index in the list from the back and places it in the front, effectively reversing the word
        if repeating == 1:  # constantly checks if a word is already in the row
            if row in answerlistrow:
                col = random.randint(0, maxcol - 1)  # picks a new starting point if there is already a word in this row
            else:
                for letter in theword:  # runs through each letter in the word and places it in its respective spot
                    grid[row][col + wordvalue] = letter
                    if firstletter:  # appends the starting point to a list to be checked when picking another word
                        answerlistrow.append(row)  # same as above
                        answerlistcol.append(col + wordvalue)  # same as above
                        firstletter = False  # ensures this doesn't happen every time
                    wordvalue = wordvalue + 1  # increases the number of blocks away from the starting point to append to in the grid, ensuring the word is spelt out accross multiple blocks
    for numz in range(len(grid)):  # checks through every row in the grid
        for j in range(len(grid[numz])):  # checks through every column in the grid
            if grid[numz][j] == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15:  # checks to see if the value in the grid is a number, this could be done in a function or a list, but I got lazy. I would definetly use the float() function if there was more than 15 numbers though
                randholder = random.randint(0, 25)  # picks a random index for a random letter
                randletter = alphabet[randholder]  # uses the random index to take a letter out of the alphabet string
                grid[numz][numz] = randletter  # appends the random letter to the grid position
    for i in grid:  # prints out each row in the grid individually
        print(i)
    #print("These are the words in the game: "+str(words)) I LEFT THIS IS SO YOU CAN EASILY SEE THE WORDS FOR MARKING


'''
This next while loop starts the game and takes the difficulty and score and allows for the player to play again if they 
want to. It also sets a lot of variables for replayability, and also calls the other functions
'''
while gameon:
    howhard = input("would you like easy, medium, hard, or leave? ")  # takes in the variable used to determine the amount of words and grid size for the game
    score = 0
    num1 = 0
    num2 = 0
    if howhard == "easy":  # uses the input to determine the length of the grid
        difficulty = "easy"
        length = 7
    elif howhard == "medium":
        difficulty = "medium"
        length = 9
    elif howhard == "hard":
        difficulty = "hard"
        length = 15
    elif howhard == "leave":
        gameon = False
        quit(code="thanks for playing")
    grid = []  # creates the grid for the game
    if difficulty == "easy":  # uses the input to determine the amount of words in the game
        numofwords = 5
    if difficulty == "medium":
        numofwords = 10
    if difficulty == "hard":
        numofwords = 15
    for i in range(length):  # appends a new row to the grid depending on the length of the grid
        grid.append([])
        for increasingnum in range(length):  # changes all characters to random letters. For some odd reason, these few lines of code are still necessary even though it is done more efficiently in a function above. This section cannot function without the function, and the function cannot work without these lines. I have no idea why, but it seems as if they cover each others weaknesses and thus are both essential
            randholder = random.randint(0, 25)
            randletter = alphabet[randholder]
            grid[i].append(randletter)
    wordpicker()  # calls the function to choose the words for the game
    wordplacement()  # calls the function to choose the placement for these words
    while score < int(numofwords):  # while loop to call the function to let the player guess. The while loops ends when the player has a score equal to the number of words in the game, AKA has found all the words
        score = are_you_right(score, numofwords)
