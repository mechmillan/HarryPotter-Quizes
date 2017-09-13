from collections import namedtuple
from random import shuffle
from re import sub

Question = namedtuple("Question", "question answer")

questions = [Question("What did Cornelius Fudge turn a teacup into to prove to the Prime Minister that he is a Wizard?", ['a gerbil', 'gerbil']),
             Question("Who was previously the Head of the Auror Office in the Department of Magical Law Enforcement?", ['rufus scrimgeour', 'rufus', 'scrimgeour']),
             Question("True or False: Snape lives in a Muggle Town on Spinner's End.", ['true', 't']),
             Question("What is Buckbeak's new name when he returns to Hagrid?", ['witherwings', 'witherwing']),
             Question("What is Dumbledore's favorite jam flavor?", ['raspberry', 'raspberries']),
             Question("What does Molly like Arthur to call her (in private)? (This is a security question)", ['mollywobbles']),
             Question("What does Ginny call Fleur?", ['phlegm']),
             Question("What is the most popular Skiving Snackbox?", ['nosebleed nougat', 'nose bleed nougat', 'nosebleed nougats', 'nose bleed nougats']),
             Question("What color are the staff robes at Weasley's Wizard Wheezer?", ['magenta', 'they are magenta']),
             Question("Which O.W.L. does Neville's grandma, Augusta, fail (according to McGonagall)?", ['charms']),
             Question("Who wrote Advanced Potion-Making? (Marked up by The Half-Blood Prince)", ['libatius borage', 'libatius', 'borage']),
             Question("How much does the book Advanced Potion-Making cost at Flourish and Blotts?", ['9 galleons', 'nine galleons']),
             Question("Name one of the 4 potions that Slughorn shows his students for his first class.", ['veritaserum', 'polyjuice potion', 'amortentia', 'felix felicis']),
             Question("Who is the founder of The Most Extraordinary Society of Potioneers", ['hector dagworth granger', 'hector dagworth', 'hector granger', 'dagworth granger']),
             Question("During what two ages did Slughorn take Felix Felicis?", ['24 and 57', '24  57', '57 and 24', '57  24', 'twenty four and fifty seven', 'fifty seven and twenty four']),
             Question("Who had to go to the hospital for eating a pound of doxy eggs as a bet?", ['cormac mclaggen', 'cormac', 'mclaggen']),
             Question("What is the counter spell to Levicorpus?", ['liberacorpus']),
             Question("What spell, written by the Half-Blood Prince, causes the ears of anyone nearby to be filled with unidentifiable buzzing?", ['muffliato']),
             Question("What does Trewlaney call Firenze?", ['dobbin']),
             Question("Fred and George try to make Ron perform the Unbreakable Vow when Ron is what age?", ['5', 'five']),
             Question("Who is Mrs. Weasley's favorite signer?", ['celestina warbeck', 'celestina', 'warbeck']),
             Question("Who is Scrimgeour's successor as Head of the Auror Office?", ['gawain robards', 'gawain', 'robards']),
             Question("How many Galleons do Appartion lessons cost? (They last 12 weeks)", ['12', 'twelve', '12 galleons', 'twelve galleons']),
             Question("Which spell can correctly identify a potion's ingredient? (Created by Scarpin Revelaspell)", ['specialis revelio']),
             Question("Who is the Ministry Appartion instructor?", ['wilkie twycross', 'wilkie', 'twycross']),
             Question("Name one of the wrong names that Slughorn call Ron?", ['ralph', 'rupert']),
             Question("What is excellent at warding off Gulping Plimpies?", ['gurdyroot', 'gurdyroots']),
             Question("Who was Tom Riddle trying to replace as Defense Against the Dark Arts professor?", ['galatea merrythought', 'galatea', 'merrythought']),
             Question("Who came up with the idea to use Felix Felicis to get the memory from Slughorn?", ['ron', 'ron weasley']),
             Question("How many months does it take to make Felix Felicis?", ['6 months', 'six months', '6', 'six']),
             Question("Romilda Vane asks Ginny if it’s true that Harry has a hippogriff tattooed across his chest. She tells her that it's actually what animal?", ['hungarian horntail', 'a hungarian horntail', 'horntail']),
             Question("Who does Hermione think is the Half-Blood Prince? (After finding an old photo of the Captain of Hogwart's Gobstones team)", ['eileen prince', 'eileen']),
             Question("Eileen Prince married what Muggle?", ['tobias snape', 'tobias', 'snape']),
             Question("Name one of the words that is in Dumbledore's idea of 'saying a few words'.", ['nitwit', 'oddment', 'blubber', 'tweak']),
             Question("What is the name of a dead body bewitched to do a Dark Wizard's bidding?", ['inferi', 'inferius']),
             Question("Dumbledore tells the Dursley's that which of their flowers is flourishing?", ['agapanthus', 'lily of the valley', 'agapanthus plant', 'agapanthus flower', 'lily of the valley plant', 'lily of the valley flowers']),
             Question("Who is the editor of The Daily Prophet? Hint: He is an ex-student of Slughorn.", ['barnabas cuffe', 'barnabas', 'cuffe']),
             Question("Who is captain of the Holyhead Harpies? Hint: She is an ex-student of Slughorn.", ['gwenog jones', 'gwenog', 'jones']),
             Question("Where does Fleur work part-time to practice her english?", ['gringotts']),
             Question("How many O.W.L.s. does Ron receive?", ['7', 'seven']),
             Question("How many O.W.L.s. does Hermione receive?", ['10', 'ten']),
             Question("How many Shield Hats did the Ministry buy for their support staff, on the initial order?", ['500', 'five hundred', '500 hats', 'five hundred hats', '500 shield hats', 'five hundred shield hats']),
             Question("Who bit Lupin (causing him to become a werewolf)?", ['fenrir greyback', 'fenrir', 'greyback']),
             Question("According to Luna, what invisible creatures float in through your ears and make your brain go fuzzy?", ['wrackspurts', 'wrackspurt']),
             Question("What potion does Slughorn ask the class to make for their first class?", ['draught of living death', 'the draught of living death']),
             Question("Which Head of the Magical Law Enforcement Squad visits the Gaunt house?", ['bob ogden', 'ogden', 'bob']),
             Question("What city does Stan Shunpike live in?", ['clapham']),
             Question("Name one of the children that is never the same after exploring some caves with Tom Riddle?", ['amy benson', 'amy', 'dennis', 'dennis bishop']),
             Question("What is the name of Ginny's Pygmy Puff?", ['arnold']),
             Question("Who is the author of Blood Brothers: My Life Amongst the Vampires? Hint: Ex-student of Slughorn.", ['eldred worple', 'eldred', 'worple'])]

print('\n')
print('Welcome to a short quiz for Harry Potter and the Half-Blood Prince!')
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
