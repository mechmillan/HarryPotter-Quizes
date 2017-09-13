from collections import namedtuple
from random import shuffle
from re import sub

Question = namedtuple("Question", "question answer")

questions = [Question("What is Mrs. Mason mortally afraid of?", ['birds','bird', 'birds of all shapes and sizes']),
             Question("Risking notice of the Muggle community is a serious offense under which section of the International Confederation of Warlocks' Statue of Secrecy?", ['13', 'thirteen', 'section 13', 'section thirteen']),
             Question("What is the name of Percy's owl? (He receives it after becoming a Prefect)", ['hermes']),
             Question("What is the name of the Weasleys' famiy owl?", ['errol']),
             Question("In what division of the Ministry of Magic does Arthur Weasley work?", ['the misuse of muggle artifacts office', 'misuse of muggle artifacts','misuse of muggle artifacts office']),
             Question("Harry and Ron receive the same amount of house points at the end of the year with their Special Services to the School award. How many points do they each earn?", ['200', 'two hundred', '200 points', 'two hundred points']),
             Question("Where is Voldemort rumored to be hiding?", ['albania', 'the forests of albania', 'in the forests of albania', 'forests of albania']),
             Question("What are Basilisks' also commonly referred to as?", ['king of serpents', 'the king of serpents', 'king serpent']),
             Question("What is the name of Aragog's wife?", ['mosag']),
             Question("How many Galleons was Arthur Weasley fined for bewitching the blue Ford Anglia?", ['50', '50 galleons', 'fifty galleons']),
             Question("What kind of broom does Ron have? (Often outstripped by passing butterflies)", ['a shooting star', 'shooting star']),
             Question("What was Hagrid looking for in Knockturn Alley?", ['flesh eating slug repellent', 'slug repellent', 'repellent']),
             Question("What is another name for a Mandrake?", ['mandragora']),
             Question("Which house is Justin Finch-Fletchly in?", ['hufflepuff']),
             Question("If he hadn't gone to Hogwarts, where would Justin Finch-Fletchly have attended?", ['eton']),
             Question("What is Gilderoy Lockhart's favorite colour?", ['lilac']),
             Question("What spell does Lockhart use to try and contain the Cornish Pixies that he releases in his first class?", ['peskipiksi pesternomi']),
             Question("How many times was Nearless Headless Nick hit with a blunt axe?", ['45', 'forty five']),
             Question("Nearly Headless Nick celebrates his 500th deathday on Halloween; what year did he die?", ['1492', 'fourteen ninety two']),
             Question("What does Harry have to take after Lockhart mistakenly removes all the bones in his arm? (33 bones)", ['skele gro', 'skelegro', 'skelegrow', 'skele grow']),
             Question("Who was teasing Myrtle about her glasses when she died?", ['olive hornby', 'olive']),
             Question("Fred bewitches Percy's Prefect badge to read what?", ['pinhead', 'pin head']),
             Question("The Bludger that was hexed to target Harry during his first Quidditch match was hexed by who?", ['dobby']),
             Question("How many days must lacewing flies be stewed for as one of the ingredients of Polyjuice Potion?", ['21', 'twenty one']),
             Question("Name one of Gilderoy Lockhart's robe colors during the school year.", ['turquoise', 'deep plum', 'pink', 'jade green', 'lilac', 'midnight blue']),
             Question("True or False: the crowing of a rooster is fatal to a Basilisk.", ['true', 't']),
             Question("Who is the first victim to the Basilisk?", ['mrs norris', 'norris', 'mrs. norris']),
             Question("Who is the second victim to the Basilisk?", ['colin creevey', 'colin']),
             Question("Who is the third victim to the Basilisk?", ['justin finch fletchly', 'nearly headless nick', 'justin']),
             Question("How many death threats does Dobby get per day at home?", ['5', 'five']),
             Question("Which curse does Lockhart suspect is the cause of the first attack?", ['transmogrifian curse', 'the transmogrifian curse']),
             Question("What kind of course is Filch enrolled in?", ['kwikspell', 'kwikspells']),
             Question("What does Hagrid use on the pumpkins growing in his garden?", ['an engorgement charm', 'the engorgement charm', 'engorgement charm']),
             Question("What is Colin Creevey's dads' profession?", ['a milkman', 'milkman', 'the milkman']),
             Question("How many O.W.L.s do Bill and Percy each receive?", ['12', 'twelve']),
             Question("Who wrote The Standard Book of Spells, Grade 2?", ['miranda goshawk', 'miranda g']),
             Question("What is Ron's Quidditch team? (9th in the league)", ['chudley cannons', 'the chudley cannons']),
             Question("The Weasley brothers rescue Harry from Vernon and Petunia in what color Ford Anglia?", ['turquoise']),
             Question("When was the Decree for the Reasonable Restriction of Underage Sorcery written?", ['1875', 'eighteen seventy five']),
             Question("Which paragraph from the Decree for the Reasonable Restriction of Underage Sorcery is cited by Mafalda Hopkirk when the notice is sent to Harry?", ['c']),
             Question("Who ruins the punchline of Mr. Vernon's Japanese golfer joke?", ['dobby']),
             Question("Who does Bill Weasley work for in Egypt?", ['gringotts']),
             Question("Name one of the cities where the flying Ford Anglia was spotted by Muggles.", ['norfolk', 'peebles']),
             Question("Name one of the things that Hagrid thinks is killing his chickens.", ['fox', 'blood sucking bugbear', 'bugbear', 'bugbears', 'foxes']),
             Question("What do the Dursley's give Harry for Christmas this year?", ['toothpick', 'a toothpick']),
             Question("What is the Slytherin password this year?", ['pure blood', 'pureblood']),
             Question("True or False: The Chamber of Secrets was opened in T.M. Riddle's 5th year.", ['true', 't']),
             Question("Who is Percy's girlfriend?", ['penelope clearwater', 'penelope']),
             Question("How many times has Gilderoy Lockhart won Witch Weekly's Most-Charming-Smile Award?", ['5', 'five', 'five times', '5 times']),
             Question("True or False: Filch uses Mrs. Skower’s All-Purpose Magical Mess Remover in an attempt to remove the message from the castle’s stones.", ['true', 't'])]

print('\n')
print('Welcome to a short quiz for Harry Potter and the Chamber of Secrets!')
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
