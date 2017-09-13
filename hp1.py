from collections import namedtuple
from random import shuffle
from re import sub

Question = namedtuple("Question", "question answer")

questions = [Question("Where does Mr. Dursley work?", ['grunnings']),
             Question("What do they make at Grunnings?", ['drills']),
             Question("What shape are Professor Dumbledore's glasses?", ['half moon', 'halfmoon']),
             Question("What shape are Professor McGonagall's glasses?", ['square', 'square shaped']),
             Question("What is one of Dumbledore\'s favorite Muggle candies?", ['lemon drops', 'lemondrops', 'lemon drop', 'lemondrop']),
             Question("What vault is the Sorcerer's Stone in?", ['713', 'vault 713']),
             Question("Who is Dudley's best friend?", ['piers', 'piers polkiss']),
             Question("How many Sickles to a Galleon?", ['17', 'seventeen']),
             Question("How many Knuts to a Sickle?", ['29', 'twenty nine']),
             Question("How many Knuts to a Galleon?", ['493', 'four hundred ninety three']),
             Question("How much do silver unicorn horns cost?", ['21 galleons', 'twenty one galleons']),
             Question("How much do Beetle Eyes cost? (per scoop)",['5 knuts', 'five knuts']),
             Question("In which book did Harry find Hedwig's name?",['a history of magic']),
             Question("In what year did Dumbledore defeat Grindewald?", ['1945', 'nineteen forty five']),
             Question("Asphodel and wormwood make what sleeping potion?", ['draught of death']),
             Question("True or False: Monkshood, Wolfsbane and Aconite are the same plant?", ['true', 't']),
             Question("How many fouls are possible in the game of Quidditch?", ['700', 'seven hundred']),
             Question("In what year were all the possible Quidditch fouls committed? (In a single game)", ['1473', 'fourteen seventy three']),
             Question("What is Charlie studying in Romania?",['dragons', 'dragon']),
             Question("What is the name of the leg-locker curse?", ['locomotor mortis', 'loco motor mortis']),
             Question("The Warlock's Convention outlawed dragon breeding in what year?", ['1709', 'seventeen o nine']),
             Question("What book does Hagrid read in preperation for Norbert?", ['dragon breeding for pleasure and profit']),
             Question("What type of dragon is Norbert?", ['norwegian ridgeback', 'norwegian', 'ridgeback', 'a norwegian ridgeback']),
             Question("Name one of the two wild dragon types of Britain.", ['common welsh green', 'common welsh', 'welsh green', 'hebridean', 'hebridean black']),
             Question("How old is Nicolas Flamel?", ['665', 'six hundred sixty five', 'six hundred and sixty five']),
             Question("How old is Nicolas Flamel's wife, Perenelle?", ['658', 'six hundred fivty eight', 'six hundred and fifty eight']),
             Question("In which tower do Harry, Ron and Hermione meet Charlie to give him Norbert?", ['astronomy tower', 'astronomy', 'the astronomy tower']),
             Question("Dumbledore's watch has twelve hands; does it have numbers?", ['no', 'n']),
             Question("What moves around the edges of Dumbledore's watch?", ['planets', 'planet']),
             Question("What does Dumbledore have a map of above his left knee?", ['the london underground', 'london underground']),
             Question("True or False: Some of Mrs. Figg's cats' names are Tibbles, Snowy, Mr. Paws and Tufty.", ['true', 't']),
             Question("Which secondary/high school is Dudley accepted to?", ['smeltings']),
             Question("What school would Harry have gone to if he didn't go to Hogwarts?", ['stonewall high', 'stone wall high', 'stonewall', 'stone wall']),
             Question("How many uses of dragon's blood are there?", ['12', 'twelve']),
             Question("Who discovered the 12 uses of dragon's blood?", ['dumbledore']),
             Question("How many presents does Dudley get on his 11th birthday?", ['39', 'thirty nine']),
             Question("What color uniforms do Gringott's goblins wear?", ['scarlet and gold', 'gold and scarlet']),
             Question("True or False: Ollivander wand cores are made from the following:\n\t\tUnicorn hairs, phoenix tail feathers, and dragon heartstring?", ['true','t']),
             Question("Which two witches/wizards is Ron missing from his chocolate frog collection?", ['agrippa and ptolemy', 'ptolemy and agrippa']),
             Question("Name one of the books that Ron, Hermione and Harry use when trying to look for information on Niocals Flamel.", ['great wizards of the twentieth century', 'notable magical names of our time', 'important modern magical discoveries', 'a study of recent developments in wizardry']),
             Question("What does Harry receive from Hagrid for Christmas?", ['wooden flute', 'hand carved wooden flute','flute', 'hand carved flute', 'a hand carved wooden flute']),
             Question("What does Harry receive from Dumbledore for Christmas?", ['invisibility cloak', 'the invisibility cloak']),
             Question("What does Harry receive from Hermione for Christmas?", ['chocolate frogs']),
             Question("What potion does Snape ask students to make for their final exams?", ['forgetfullness potion','the forgetfullness potion', 'forgetfullness']),
             Question("How many house points does Gryffindor have when they win the House Cup?", ['482', 'four hundred eighty two', 'four hundred and eighty two']),
             Question("Which house is in last place for the House Cup at the end of the year?", ['hufflepuff']),
             Question("Name the three Centaurs that save Harry in the Forbidden Forest.", ['ronan bane firenze', 'ronan firenze bane', 'bane ronan firenze', 'bane firenze ronan', 'firenze ronan bane', 'firenze bane ronan', 'ronan  bane  and firenze', 'ronan  firenze  and bane', 'bane  ronan  and firenze', 'bane  firenze  and ronan', 'firenze  ronan  and bane', 'firenze  bane  and ronan']),
             Question("What does Harry receive from Vernon and Petunia for Christmas?", ['a fifty pence piece', '50 pence', 'fifty pence', '50 pence piece']),
             Question("How many house points does Slytherin have at the end of the year?", ['472','four hundred seventy two', 'four hundred and seventy two']),
             Question("What percentage does Hermione receive on Flitwick's final exam? (They make a pineapple tap dance across the desk)", ['112 ', '112  ', 'one hundred twelve percent', 'one hundred and twelve percent', '112'])]

print('\n')
print('Welcome to a short quiz for Harry Potter and the Sorcerer\'s Stone!')
print('Please type in your response and hit enter to submit your answer.')
print('If you don\'t know an answer, hit enter or just type \'idk\'.')
print('To end the quiz early (without calculating a final score), press CTRL-D')
print('\n')

def quiz(questions):

    score = 0
    for question in questions:
        print(question.question)
        user_answer = input('> ').lower().strip()
        stripped_answer = sub('[^a-zA-Z0-9 \n\.]', ' ', user_answer)

        if stripped_answer in question.answer and stripped_answer != '':
            print("Correct")
            score += 1
        else:
            print("Incorrect!\nThe correct answer is:", question.answer)

    percentage = (score / len(questions)) * 100
    print("{} out of {}. That is {:.2f} % correct.".format(score, len(questions), percentage))

    if 0 <= percentage < 50.00:
        print('That\'s a pretty terrible score! This isn\'t weighted you know, Dudley!')
    elif 50.00 <= percentage < 70.00:
        print('Below average! Just like Crabb and Goyle.')
    elif 70.00 <= percentage < 80.00:
        print('A bit better - but I bet you paid someone to take this for you Malfoy!')
    elif 80.00 <= percentage < 90.00:
        print('Pretty good, Ron.')
    elif 90.00 <= percentage <= 99.99:
        print('The art of cramming is paying off! Go get them Potter!')
    elif percentage == 100:
        print('What a true Hermione! Congratulations, you\'ve won!')
    else:
        print('You found a bug. Are you Voldemort?')

    print('\n')

if __name__ == "__main__":
    # print(len(questions))
    try:
        n = 0
        while n <= 0:
            shuffle(questions)
            quiz(questions[:])
            n += 1
    except EOFError:
        print('Thanks for playing! Alas, earwax!')
        print('\n')
