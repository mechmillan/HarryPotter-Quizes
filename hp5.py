from collections import namedtuple
from random import shuffle
from re import sub

Question = namedtuple("Question", "question answer")

questions = [Question("What date is Harry's disciplinary hearing scheduled for after he uses the Patronus Charm?", ['august 12th', 'august 12', 'the 12th of august']),
             Question("What spell does Dolohov use on Neville?", ['tarantallegra', 'tarantallegra spell', 'the tarantallegra spell']),
             Question("What spell is used by Harry, Ron, Hermione, Neville and Luna to smash the prophecy shelves?", ['reducto', 'reducto spell', 'the reducto spell']),
             Question("What spell does Hermione use to mark the doors that the group has been through when they are in the Department of Mysteries?", ['flagrate', 'flagrate spell', 'the flagrate spell']),
             Question("Who is the head of The Wizarding Examination Authority?", ['griselda marchbanks', 'griselda', 'marchbanks']),
             Question("How tall is Grawp?", ['16 feet', '16 ft', '16ft', 'sixteen feet', 'sixteen ft']),
             Question("During what year did Lily start dating James?", ['7th', '7', 'seven', 'year 7', 'the 7th year']),
             Question("What animal is Cho's Patronus?", ['swan', 'a swan']),
             Question("What is the term for the ability to extract feelings and memories from another person's mind?", ['legilimency']),
             Question("What is the branch name of obscure magic that protects ones mind against external penetration?", ['occlumency']),
             Question("According to Luna, what is mistletoe often infected with?", ['nargles', 'nargle']),
             Question("What is the name of Hagrid's favorite Thestral?", ['tenebrus']),
             Question("How long has Snape been teaching at Hogwarts?", ['14 years', 'fourteen years', 'for 14 years', 'for fourteen years']),
             Question("What potion does Snape ask students to make on their first day?", ['draught of peace', 'the draught of peace']),
             Question("What is Cho Chang's Quidditch team?", ['tornados', 'the tornadoes', 'tornadoes', 'the tornados']),
             Question("What new broom does Ron receive after becoming a Prefect?", ['cleansweep eleven', 'a cleansweep eleven', 'cleansweep 11', 'a cleansweep 11']),
             Question("What number does Arthur Weasley dial in the phonebooth to enter the Ministry of Magic?", ['62442']),
             Question("Who is Bellatrix married to?", ['rodolphus']),
             Question("Sirius thinks his mother used what charm on the back of her portrait’s canvas?", ['permanent sticking charm', 'a permanent sticking charm']),
             Question("Who was the Minister prior to Fudge?", ['millicent bagnold', 'millicent', 'bagnold']),
             Question("What is the Sirius' family motto?", ['toujours pur']),
             Question("Name one of the Griffindor prefects for this year.", ['hermione granger', 'hermione', 'ron weasley', 'ron']),
             Question("What charm does Hermione use on the Galleons used by Dumbledore's Army for meeting times?", ['protean charm', 'the protean charm', 'a protean charm', 'protean']),
             Question("Who replaces Harry as Seeker?", ['ginny', 'ginny weasley']),
             Question("Who replaces Trelawney as the new Divination professor?", ['firenze', 'the centaur firenze']),
             Question("Why do stunning spells bounce off of Hagrid?", ['because of his giants blood', 'giants blood', 'his giants blood', 'due to giants blood', 'giant blood']),
             Question("Which professor asks Harry to produce a Patronus for a bonus point? (A friend-Tiberius Ogden- told him Harry could)", ['professor tofty', 'tofty']),
             Question("What is Harry bitten by during his Herbology exam?", ['fanged geranium', 'a fanged geranium']),
             Question("Which 6th year Ravenclaw tries to sell Harry and Ron Baruffio's Brain Elixir for 12 Galleons for help on their exams?", ['eddie carmichael', 'eddie', 'carmichael']),
             Question("Which professor examined Dumbledore during his N.E.W.T.s as he 'did things with his wand that she had never seen before' Hint: She's the current Head of The Wizarding Examination Authority.", ['griselda marchbanks','professor marchbanks', 'marchbanks']),
             Question("True or False: Tonks is a Metamorphmagus.", ['true', 't']),
             Question("At what age did Sirius run away from home?", ['16', 'sixteen', 'at age 16', 'at age sixteen', 'when he was sixteen', 'when he was 16']),
             Question("Who is Rodolphus' brother?", ['rabastan']),
             Question("Give the full name of one of the two people acting as defense for Harry's disciplinary hearing.", ['albus percival wulfric brian dumbledore', 'arabella doreen figg']),
             Question("Who wrote Defensive Magical Theory?", ['wilbert slinkhard', 'wilbert']),
             Question("What plant does Neville get in Assyria for his birthday?", ['mimbulus mimbletonia', 'a mimbulus mimbletonia plant', 'mimbulus mimbletonia plant']),
             Question("Sturgis Podmore attempts a robbery at the Ministry of Magic on what date?", ['august 31', 'august 31st', 'august thirty first', 'the thirty first of august']),
             Question("Name one of the new Slytherin Prefects.", ['draco malfoy', 'draco', 'malfoy', 'pansy parkinson', 'pansy', 'parkinson']),
             Question("Name one of the new Hufflepuff Prefects.", ['ernie macmillan', 'ernie', 'macmillan', 'hannah abbott', 'hannah', 'abbott']),
             Question("Name one of the new Ravenclaw Prefects.", ['anthony goldstein', 'anthony', 'goldstein', 'padma patil', 'padma', 'patil']),
             Question("What is Umbridge's first lesson titled?", ['a return to basic principles']),
             Question("Who was Sturgis Podmore arrested by?", ['eric munch', 'eric', 'munch']),
             Question("Who is Trelawney's great-great-grandmother?", ['seer cassandra trelawney', 'cassandra trelawney', 'cassandra']),
             Question("Who claims that Fudge has his own army of heliopaths? (spirits of fire)", ['luna', 'luna lovegood', 'lovegood']),
             Question("What does the girl's dormitary stairs turn into when a boy tries to enter?", ['a slide', 'slide', 'it turns into a slide']),
             Question("Who tells Harry about the Room of Requirement? Hint: Two possible answers", ['dobby', 'dumbledore']),
             Question("Who still writes weekly to Gilderoy Lockhart during his permanent stay in St. Mungo's?", ['gladys gudgeon', 'gladys', 'gudgeon']),
             Question("Which Deatheater leaked Ministry secrets?", ['augustus rookwood', 'augustus', 'rookwood']),
             Question("What curse did Lucius Malfoy use on Broderick Bode the day of Harry's disciplinary hearing?", ['imperius curse', 'the imperius curse', 'imperius']),
             Question("What did Fred and George treat themselves too after their business started booming?", ['dragon skin suits', 'dragon skin suit', 'they got dragon skin suits', 'dragon skinned suits'])]

print('\n')
print('Welcome to a short quiz for Harry Potter and the Order of the Phoenix!')
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
