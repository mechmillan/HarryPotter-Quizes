from collections import namedtuple
from random import shuffle
from re import sub

Question = namedtuple("Question", "question answer")

questions = [Question("Who does Voldemort ask to sit next to him?", ['snape', 'severus snape']),
             Question("Whose wand does Voldemort borrow?", ['lucius malfoy', 'malfoy', 'lucius']),
             Question("Who taught Muggle Studies at Hogwarts? (killed by Voldemort)", ['charity burbage', 'charity', 'burbage', 'professor burbage']),
             Question("What is the title of Rita Skeeter's forthcoming biography on Albus Dumbledore?", ['the life and lies of albus dumbledore']),
             Question("Who claims that Dumbledore 'borrowed' his papers on the 8 uses of dragons blood?", ['ivor dillonsby', 'ivor', 'dillonsby']),
             Question("What are Dumbledore's last words to Lupin and Kingsley?", ['harry is the best hope we have. trust him.', 'harry is the best hope we have  trust him']),
             Question("The Decree for Justifiable Confiscation gives the Ministry the power to confiscate the contents of a will for up to how many days?", ['31', 'thirty one', '31 days', 'thirty days']),
             Question("What is the correct name for garden gnomes?", ['gernumbli gardensi', 'gernumblis', 'gardensi s']),
             Question("Who killed Krum's grandfather?", ['grindelwald', 'gellert grindelwald', 'gellert']),
             Question("On what road is The Leaky Cauldron on?", ['charing cross']),
             Question("What is Arthur Weasley's Patronus?", ['weasel', 'a weasel']),
             Question("What is Dolores Umbridge's Patronus?", ['cat', 'a cat']),
             Question("In which town did the Dumbledores live before they moved to Godric's Hollow?", ['mould on the would']),
             Question("What color robes do Magical Maintenance employees at the Ministry wear?", ['navy', 'navy blue']),
             Question("Rita Skeeter wrote a biography about another Hogwarts Headmaster. What was it called?", ['armando dippet  master or moron ', 'armando dippet master or moron ', 'armando dippet master or moron']),
             Question("Umbridge says the S on the locket stands for what? Hint: she says she's related to this family.", ['selwyn']),
             Question("What is the only spell Hermione ever has trouble with?", ['patronus', 'expecto patronum']),
             Question("What is the first of the 5 Elemental Principal Exceptions to Gamp's Law of Elemental Transfiguration?", ['food']),
             Question("In which year was the International Statute of Secrecy signed?", ['1689']),
             Question("Where did Bowman Bright forge the first ever Gold Snitch?", ['godrics hollow', 'godric s hollow']),
             Question("True or false: Kendra and Ariana's tombstone reads 'The last enemy that shall be destroyed is death.'", ['f', 'false']),
             Question("True or false: James and Lily's tombstone reads 'Where your treasure is, there will your heart be also.'", ['f', 'false']),
             Question("What is Kingsley's Patronus?", ['a lynx', 'lynx']),
             Question("What are the names of the original 3 Peverell brothers?", ['antioch  ignotus  cadmus', 'antioch  cadmus  ignotus', 'ignotus  antioch  cadmus', 'ignotus  cadmus  antioch', 'cadmus  ignotus  antioch', 'cadmus  antioch  ignotus']),
             Question("What radio program does Ron use to track news? (only one telling the truth anymore)", ['potterwatch']),
             Question("What is the feature in Gringotts called that washes away all enchantments and concealments?", ['thief s downfall', 'thief\'s downfall']),
             Question("There are two curses in the Lestrange's vault; name one of them.", ['flagrante', 'gemino']),
             Question("Which spell does McGonagall use to bring the castle's suits of armor to life to protect the school?", ['piertotum locomotor']),
             Question("True or false: Harry is a living descendent of Ignotus Peverell", ['t', 'true']),
             Question("Molly gives Harry a watch for his 17th birthday; whose was it before?", ['fabian s', 'fabian', 'fabian prewett']),
             Question("Molly has two brothers who were killed during Voldemort's first reign. Name one of them.", ['fabian', 'gideon', 'fabian prewett', 'gideon prewett']),
             Question("19 years later, Harry overhears Percy discussing what on the Platform 9 3/4? He tries to avoid him.", ['broomstick regulations'])]

print('\n')
print('Welcome to a short quiz for Harry Potter and the Deathly Hallows!')
print('Please type in your response and hit enter to submit your answer.')
print('If you don\'t know an answer, hit enter or just type \'idk\'.')
print('To end the quiz early (without calculating a final score), press CTRL-D')
print('\n')

def quiz(questions):

    score = 0
    for question in questions:
        print(question.question)
        user_answer = input('> ').lower().strip(' ')
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
