from collections import namedtuple
from random import shuffle
from re import sub

Question = namedtuple("Question", "question answer")

questions = [Question("Which Deatheater asks Voldemort for forgiveness first?", ['avery', 'deatheater avery']),
             Question("Who was the gamekeeper before Hagrid?", ['ogg', 'a man called ogg']),
             Question("What date is the third task scheduled for?", ['june 24th', 'june 24', '24th of june', 'the 24th of june', 'june 24th at dusk']),
             Question("How many points does Harry get for the second task?", ['45']),
             Question("What is the name of Fleur's sister?", ['gabrielle']),
             Question("The Gobbledegook word 'blavak' means what?", ['pickax', 'pick ax', 'pick axe']),
             Question("What is the password to the Prefect's bathroom? (On the 4th floor, to the left of a statue of Boris the Bewildered.)", ['pine fresh', 'pinefresh']),
             Question("What is Hagrid's mother's name?", ['fridwulfa']),
             Question("What does WWN stand for in the wizarding world?", ['wizarding wireless network']),
             Question("Which band did Dumbledore book for the Yule Ball?", ['the weird sisters', 'weird sisters']),
             Question("How many barrells of mulled mead did Dumbledore buy for the Yule Ball?", ['800']),
             Question("What curse was Sirius going to suggest to Harry for him to get past the dragon task?", ['the conjunctivitus curse', 'conjunctivitus curse', 'conjunctivitus']),
             Question("What date is the second task scheduled for?", ['february 24th', 'february 24', 'the 24th of february']),
             Question("Which dragon type does Krum draw for the dragon task?", ['chinese fireball', 'fireball', 'the chinese fireball']),
             Question("Which dragon type does Harry draw for the dragon task?", ['the horntail', 'horntail', 'horn tail', 'hungarian horntail', 'the hungarian horntail', 'hungarian horn tail']),
             Question("What date is the first task scheduled for?", ['november 24th', 'november 24', 'the 24th of november']),
             Question("What does Hagrid use to tame his hair?", ['axle grease', 'grease', 'axlegrease']),
             Question("Who was the caretaker when Molly and Arthur were at Hogwarts?", ['apollyon pringle', 'apollyon', 'pringle']),
             Question("Where are Nifflers (they like sparkly things and are useful treasure detectors) often found?", ['in mines', 'mines', 'they are found in mines', 'mine']),
             Question("Name one of the ingredients that is missing from Snape's private storage.", ['gillyweed', 'gillyweeds', 'boomslang skin', 'boomslang skins', 'the sking of a boomslang']),
             Question("What language does Dumbledore speak with Merchieftaness Murcus?", ['mermish']),
             Question("How many points does Fleur get for the second task?", ['25', 'twenty five', 'twenty five points', '25 points']),
             Question("How many points does Cedric get for the second task?", ['47', 'forty seven', 'forty seven points', '47 points']),
             Question("What is the name of Dumbledore's brother?", ['aberforth']),
             Question("Who is the temporary Care of Magical Creatures professor?", ['professor grubby plank', 'grubby plank', 'plank', 'grubby']),
             Question("True or False: Harry and Krum are tied for first place after the first task.", ['true', 't']),
             Question("On what date does Sirius ask Harry to be alone (by the fire in Gryffindor Tower at 1AM) to speak with him?", ['november 22nd', 'november 22', '22 of november', 'november twenty second', 'the twenty second of november']),
             Question("Who did Victor Krum get his wand from?", ['gregorovitch']),
             Question("What does Rita Skeeter use to write?", ['a quick quotes quill', 'quick quotes quill']),
             Question("Who performs the wand weighing for the tournament?", ['ollivander']),
             Question("What do Madam Maxine's horses only drink?", ['single malt whiskey', 'whiskey']),
             Question("In what year of the Triwizard Tournament were all 3 judges injured when a cockatrice went on a rampage?", ['1792', 'seventeen ninety two']),
             Question("How many Sickles does it cost to join S.P.E.W? (Society for the Promotion of Elfish Welfare)", ['2', 'two', '2 sickles', 'two sickles']),
             Question("What position does Harry hold in S.P.E.W?", ['secretary', 'the secretary', 'he is the secretary']),
             Question("What book does Moody give Neville after their first lesson?", ['magical water plants of the mediterranean']),
             Question("What is an excellent remedy for acne in the wizarding world?", ['bubotuber pus', 'a bubotubers pus', 'a bubotuber s pus']),
             Question("The Triwizard Tournament includes a prize of how many Galleons?", ['1000', '1 000', 'one thousand', 'a thousand', '1000 galleons', '1 000 galleons', 'one thousand galleons', 'a thousand galleons']),
             Question("Where did Lucius Malfoy consider sending Draco instead of Hogwarts?", ['durmstrang']),
             Question("What spell is used to determine the previous spell that a wand has cast?", ['prior incantato', 'priori incantatem']),
             Question("Which Clause of the Code of Wand Use states, 'no non-human creature is permitted to carry or use a wand.'", ['3', 'three', 'clause 3', 'clause three', 'the third clause']),
             Question("What spell conjures the Dark Mark?", ['morsmordre', 'the morsmordre spell', 'morsmordre spell']),
             Question("Who is the campsite manager at the Quidditch Worldcup?", ['mr. roberts', 'roberts']),
             Question("The final score of the Quidditch Worldcup is: Bulgaria - 160 and Ireland: ?", ['170', 'one hundred seventy', 'one hundred and seventy']),
             Question("What do Fred and George drop that Dudley finds and eats?", ['ton tongue toffee', 'ton tongue toffy']),
             Question("What does Ron name his owl?", ['pigwidgeon', 'pig', 'pig for short']),
             Question("Who was the Riddles' gardener?", ['frank bryce', 'frank', 'bryce', 'mr. bryce']),
             Question("Where is the Riddle House?", ['little hangleton', 'hangleton']),
             Question("Which Quidditch team did Oliver Wood sign with?", ['puddlemere united', 'the puddlemere united', 'puddlemere united reserve team', 'the puddlemere united reserve team']),
             Question("Fred and George bet 3 Knuts, 15 Sickles, and how many Galleons on the Quidditch Worldcup?", ['37', 'thirty seven', '37 galleons', 'thirty seven galleons']),
             Question("What maneuvour does Krum use in the Quidditch Worldcup that causes Lynch to crash twice?", ['wronskei feint', 'the wronskei feint'])]

print('\n')
print('Welcome to a short quiz for Harry Potter and the Goblet of Fire!')
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
