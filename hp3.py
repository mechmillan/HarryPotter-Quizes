from collections import namedtuple
from random import shuffle
from re import sub

Question = namedtuple("Question", "question answer")

questions = [Question("How many Galleons do the Weasley's win for The Daily Prophet's Grand Prize?", ['700', 'seven hundred', '700 galleons', 'seven hundred galleons']),
             Question("While in Egypt, what does Ron send Harry for his birthday?", ['a pocket sneakoscope', 'pocket sneakoscope', 'sneakoscope']),
             Question("What is the name of the executioner that is set to execute Buckbeak and Sirius?", ['walden macnair', 'walden', 'macnair']),
             Question("What spell does Lupin use to bind Ron's broken leg?", ['ferula', 'the ferula spell', 'ferula spell']),
             Question("What date is Buckbeak's appeal set for?", ['june 6', 'june 6th', 'on june 6', 'on june 6th', 'the 6th of june', 'on the 6th of june']),
             Question("Cho Chang (Ravenclaw's Seeker) has what type of broom?", ['comet two sixty', 'comet 260']),
             Question("Who is the bartender at the Three Broomsticks in Hogsmeade?", ['madam rosmerta', 'rosmerta']),
             Question("What is the name of the spell that opens the secret passage to Hogsmeade in Honeyduke's cellar?", ['dissendium', 'the dissendium spell', 'dissendium spell']),
             Question("When Lupin was at Hogwarts as a student, who almost lost an eye to the Whomping Willow?", ['davey gudgeon', 'davey']),
             Question("What is the name of the one-legged creature that looks as if it is made of wisps of smoke (frail and harmless looking) that lures travelers into bogs?", ['hinkypunks', 'hinkypunk']),
             Question("Who is Hufflepuff's new Captain and Seeker this year?", ['cedric diggory', 'cedric']),
             Question("Who replaces the Fat Lady after she is attacked?", ['sir cadogan', 'cadogan']),
             Question("Where does the Fat Lady hide after she is attacked by Sirius?", ['a map', 'map', 'a map of argyllshire', 'map of argyllshire', 'argyllshire']),
             Question("Where are Kappas commonly found? (They are creepy water-dwellers that look like scaly monkeys, with webbed hands itching to strangle unwitting waders in their ponds)", ['mongolia']),
             Question("What is the name of Ron's uncle who died 24 hours after seeing a Grim?", ['uncle bilius', 'bilius']),
             Question("What is the name of the little goblin like creatures that lurk wherever there has been bloodshed?", ['red caps', 'red cap', 'redcaps', 'redcap']),
             Question("What is the most haunted building in Britain?", ['the shrieking shack', 'shrieking shack']),
             Question("Who is the landlord of The Leaky Cauldron?", ['tom']),
             Question("Who is the conductor of The Knight Bus?", ['stan shunpike', 'stan']),
             Question("Who is the driver of The Knight Bus?", ['ernie prang', 'ernie']),
             Question("What is the name of Aunt Marge's dog that is with her during her stay at the Dursley's?", ['ripper']),
             Question("How many dogs does Aunt Marge have?", ['12', 'twelve', '12 dogs', 'twelve dogs']),
             Question("What book does Hagrid give Harry for his 13th birthday?", ['the monster book of monsters', 'monster book of monsters']),
             Question("How long is Ron's new wand?", ['14 in', '14 inches', 'fourteen inches', '14 ']),
             Question("Who wrote Unfogging the Future?", ['cassandra vablatsky', 'cassandra']),
             Question("What charm are Firebolt's charmed with?", ['unbreakable braking charm', 'braking charm', 'braking']),
             Question("What does Harry first think Sirius looks like when he sees him in a newspaper?", ['a vampire', 'vampire']),
             Question("Who is taking care of Aunt Marge's dogs while she is staying with the Dursley's?", ['colonel fubster', 'the colonel', 'fubster']),
             Question("What is the street name where Harry is picked up by the Knight Bus?", ['magnolia crescent', 'magnolia', 'crescent']),
             Question("What color are Buckbeak's eyes?", ['orange', 'they are orange']),
             Question("What is the name of water demons that are sickly green creatures? (With horns and abnormally long fingers that are strong but brittle)", ['grindylows', 'grindylow']),
             Question("Who was the professor who retired from Care of Magical Creatures the previous year?", ['professor kettleburn', 'kettleburn']),
             Question("Scabbers used to belong to which Weasley?", ['percy', 'percy weasley']),
             Question("What room number does Harry stay in when he visits The Leaky Cauldron?", ['11', 'eleven', 'room 11', 'room eleven', 'the 11th room']),
             Question("How many Sickles does a ticket to London on The Knight Bus cost?", ['11', 'eleven', '11 sickles', 'eleven sickles']),
             Question("What destroys Harry's Nimbus 2000?", ['the whomping willow', 'whomping willow']),
             Question("How many passages are there from Hogwarts to Hogsmeade?", ['7', 'seven', '7 passages', 'seven passages']),
             Question("How many passages does Filch know of from Hogwarts to Hogsmeade?", ['4', 'four', '4 passages', 'four passages']),
             Question("What potion is a recent discovery?", ['the wolfsbane potion', 'wolfsbane', 'wolfsbane potion']),
             Question("What is the name of the charm used by the Potters and Peter Pettigrew?", ['fidelius charm', 'the fidelius charm', 'fidelius']),
             Question("What do N.E.W.T.s stand for?", ['nastily exhausting wizarding tests', 'nastily exhausting wizarding test']),
             Question("Which charm does Snape think Sirius used on Hermione, Ron, and Harry?", ['confundus charm', 'the confundus charm', 'confundus']),
             Question("How many turns of the Time Turner does Dumbledor advise Harry and Hermione use?", ['3', 'three', '3 turns', 'three turns']),
             Question("How many minutes do Harry and Hermione have to get back to the hospital wing after saving Sirius?", ['10', 'ten', '10 minutes', 'ten minutes']),
             Question("Sirius is locked in which professor's office?", ['flitwick', 'flitwicks', 'in flitwicks office', 'in flitwick s office']),
             Question("What does Fudge tell Snape he will receive?", ['order of merlin second class', 'order of merlin', 'order of merlin  second class']),
             Question("What floor is Professor Flitwick's office on?", ['7th', 'the 7th', 'on the 7th floor', '7th floor', 'the 7th floor', 'floor 7']),
             Question("Who hits Malfoy after he makes fun of Hagrid when Buckbeak loses his case?", ['hermione', 'hermione granger']),
             Question("Penelope and Percy have a bet on the Gryffindor-Ravenclaw match for how many Galleons?", ['10', 'ten', '10 galleons', 'ten galleons']),
             Question("In what department did Cornelius Fudge work during the time of Sirius' and Pettigrews' duel?", ['department of magical catastrophes', 'magical catastrophes'])]

print('\n')
print('Welcome to a short quiz for Harry Potter and the Prisoner of Azkaban!')
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
