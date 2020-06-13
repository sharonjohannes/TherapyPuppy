"""A collection of functions for doing my project, Therapy Puppy Session."""


def therapy_puppy_session():
    """ Main function that calls upon other functions to run
    interactive user input.
    
    Parameters
    ----------
    none
    
    Returns
    -------
    none
    """
    
    # Function call to introduce therapy puppy, visually and verbally
    introduction()
       
    chat = True    
    while chat:
        
        # This makes it so that the user will be forced to enter
        # a valid number by having the same input message
        # repeated until they do so.
        while True:
            
            # Since question asks for a number 1-10, this converts
            # the user input to an int.
            first_number = int(input(" \n For starters... on a scale from" +
                                     " 1-10, how are you feeling" +
                                     " mentally at the moment? (1 = bad," +
                                     " 10 = good!) : "))
            
            # If user enters valid number, break out of loop
            # to continue to next question.
            if 1 <= first_number <=10 and type(first_number) == int:
                break

        # Prints out statement corresponding to number inputted.
        print(mental_state(first_number))
        
        # This again makes it so that the user will be forced to enter
        # a valid number by having the same input message
        # repeated until they do so.
        while True:
            second_number = int(input("Hmm... how about a suggestion?" +
                                      " On a scale from 1-10, how" +
                                      " badly do you need to destress? (1" +
                                      " being VERY much needed, 10 being" +
                                      " you are already relaxed): "))
            
            if 1 <= second_number <=10 and type(second_number) == int:
                break
                
        print(destress_level(second_number))
        
        # Asks user final question, using same while loop method
        # so user will be forced to enter one of 10 valid moods
        # by having the same input message repeated until they
        # do so.
        while True:
            mood = input("Out of these 10 moods, which do you feel" +
                         " most closely right now? The options are" +
                         " happy, sad, frustrated, bored," +
                         " overwhelmed, hopeful, excited, relaxed," +
                         " hungry, silly: ")
            if mood in ["happy", "sad", "frustrated", "bored",
                        "overwhelmed","hopeful", "excited",
                        "relaxed", "hungry", "silly"]:
                break
            
        print(overall_feeling(mood))
        
        break
        
    # Function call to conclude session, visually and verbally
    goodbye()
            
        
def introduction():

    # ASCII art of dog to visually introduce students to the therapy 
    # dog session with Wizard Puppy, followed by brief dialogue of his
    # formal introduction.
    dog_image = """
           __
        o-''|\_____/)
         \_/|_)     )
            \  __  /
            (_/ (_/    
        
    Hello there! Having a ruff day? That's what pups are here for! My
    name is Wizard Puppy, and I am you therapy dog for today. I'm not
    a Wizard, my hoomans just named me that. Anyways, I am here
    today to evaluate your mental health and see what exactly might
    help you feel better!
        """
    
    print(dog_image)
        
        
def goodbye():
    
    dog_goodbye =  """
           __
        o-''|\_____/)
         \_/|_)     )
            \  __  /
            (_/ (_/    
    Thanks for chatting! Goodbye from Wizard Puppy! Hope all your
    dreams and wishes come true! I personally am hoping for more
    dog treats. :3
    """
    
    print(dog_goodbye)
     
        
def mental_state(first_number):
    """Offer words of encouragement to students based on how they feel.
    
    Parameters
    ----------
    first_number : int
        Student-chosen number between 1 and 10 on
        how they are doing mentally, in order to
        decide which statement of encouragement
        they will be given.
        
    Returns
    -------
    one_to_two_advice : str
        Statement of encouragement given to student
        who chooses a number between 1-2.
    three_to_five_advice : str
        Statement of encouragement given to student
        who chooses a number between 3-5.    
    six_to_eight_advice : str
        Statement of encouragement given to student
        who chooses a number between 6-8.
    nine_to_ten_advice : str
        Statement of encouragement given to student
        who chooses a number between 9-10.    
    """
    
    # Words of advice for students based on how they are doing mentally -
    # Choosing a number from 1-2: Not doing well at all.
    # 3-5: Mentally decent, could be better/could be worse.
    # 6-8: Mediocre, life is okay.
    # 9-10: Doing well, life is good!
    one_to_two_advice = (" \n *** Uh oh... maybe not too well." +
                         " Seems like you are at or near rock-bottom." +
                         " But have no fear, pup is here! Keep" +
                         " talking to Wizard Puppy for more words" +
                         " of wisdom. *** \n" )
    three_to_five_advice = (" \n *** Not completely horrible right" +
                            " now, but definitely not as good as it" +
                            " can get, I see. It is quite an odd" +
                            " feeling, not necessarily happy, but" +
                            " not necessarily sad... Don't worry," +
                            " that's why I'm here! Keep talking to"
                            " Wizard Puppy for more words of" +
                            " wisdom. *** \n")
    six_to_eight_advice = (" \n *** Hmm, seems like you're doing" +
                           " pretty decent right now! I know just" +
                           " what can get you back on the up and up" +
                           " again! Keep talking to Wizard Puppy for" +
                           " more words of wisdom. *** \n")
    nine_to_ten_advice = (" \n *** Wow! You must be on cloud 9, or" +
                          " pretty doggone close! Wanna hear more?" +
                          " Keep talking to Wizard Puppy for more" +
                          " words of wisdom. *** \n")
    
    # If/elif statements to determine which statement the student should
    # be given based on which number from 1-10 they input.
    if first_number == 1 or first_number == 2:
        return(one_to_two_advice)
    elif 3 <= first_number <= 5:
        return(three_to_five_advice)
    elif 6 <= first_number <= 8:
        return(six_to_eight_advice)
    elif first_number == 9 or first_number == 10:
        return(nine_to_ten_advice)
    

def destress_level(second_number):
    """Provides randomly-picked suggestions for students on
    how to destress based on how they feel.
    
    Parameters
    ----------
    second_number : int
        Student-chosen number between 1 and 10 on
        how they are doing mentally, in order to
        decide which destressor activity they 
        will be suggested.
        
    Returns
    -------
    one_to_two_suggestions : str
        Suggestion of a destressor activity given 
        to student who chooses a number between 1-2.
    three_to_five_suggestions : str
        Suggestion of a destressor activity given 
        to student who chooses a number between 3-5.
    six_to_eight_suggestions : str
        Suggestion of a destressor activity given 
        to student who chooses a number between 6-8.
    nine_to_ten_suggestions : str
        Suggestion of a destressor activity given 
        to student who chooses a number between 9-10.
    """
    # Randomly select from list of suggestions on how to destress
    # to help students relax at the end of the quarter.
    import random
    
    one_to_two_suggestions = [" \n *** Have some ice cream! My physics" +
                              " teacher told me that ice cream cures" +
                              " sadness. *** \n ", " \n *** Sometimes" +
                              " you just have to cry it out, my" +
                              " fur-rend. Ice cream after helps. *** \n",
                              " \n *** Take a walk, let it all out. *** \n"]
    three_to_five_suggestions = [" \n *** Feeling pretty 'meh'? Have a" +
                                 " dance party! My favorite song to jam" +
                                 " out to is 'Don't Stop Me Now!' *** \n",
                                 " \n *** Go hiking! Explore the great" +
                                 " outdoors! *** \n", " \n *** Meditate," +
                                 " relax, find some peace of mind. *** \n"]
    six_to_eight_suggestions = [" \n *** Sing. Loudly. Badly. Why not?" +
                                " :) *** \n", "\n *** Call someone you" +
                                " love! I'm sure they'll appreciate" +
                                " it. *** \n", " \n *** Bored? Clean" +
                                " your room! Or your whole house! Mom" +
                                " will love you even more! ***\n"]
    nine_to_ten_suggestions = [" \n *** Listen to happy tunes. Might" +
                               " I suggest 'Walking on Sunshine'? :) ***\n ",
                               " \n *** Tell someone you love and" +
                               " appreciate them. Maybe even your pet if" +
                               " you have one! *** \n", " \n *** You only" +
                               " live once, this is your sign!!! Go do" +
                               " things! Go climb a tree! Just don't go" +
                               " barking up the wrong one! Only one life to" +
                               " live, or as my hoomans say, 'yolo'! *** \n"]
    
    # First check if student's number input is in the 1-2 range.
    if second_number == 1 or second_number == 2:
        return(random.choice(one_to_two_suggestions))
    # If not in 1-2 range, check if the input is in the
    # 3-5 range, 6-8 range, then 9-10 range.
    elif 3 <= second_number <= 5:
        return(random.choice(three_to_five_suggestions))
    elif 6 <= second_number <= 8:
        return(random.choice(six_to_eight_suggestions))
    elif second_number == 9 or second_number == 10:
        return(random.choice(nine_to_ten_suggestions))
        
        
def overall_feeling(mood):
    """Gives students a quote and parting words of wisdom
    based on what current mood they have chosen.
    
    Parameters
    ----------
    mood : str
        One of the 10 moods that students will pick
        that they most closely resemble, from:
        happy, sad, frustrated, bored, overwhelmed,
        hopeful, excited, relaxed, hungry, silly.
        
    Returns
    -------
    mood_happy : str
        Relevant quote and last words of encouragement given 
        to student who chooses "happy" as their current mood.
    mood_sad : str
        Relevant quote and last words of encouragement given 
        to student who chooses "sad" as their current mood.
    mood_frustrated : str
        Relevant quote and last words of encouragement given 
        to student who chooses "frustrated" as their current mood.
    mood_bored : str
        Relevant quote and last words of encouragement given 
        to student who chooses "bored" as their current mood.
    mood_overwhelmed : str
        Relevant quote and last words of encouragement given 
        to student who chooses "overwhelmed" as their current mood.
    mood_hopeful : str
        Relevant quote and last words of encouragement given 
        to student who chooses "hopeful" as their current mood.
    mood_excited : str
        Relevant quote and last words of encouragement given 
        to student who chooses "excited" as their current mood.
    mood_relaxed : str
        Relevant quote and last words of encouragement given 
        to student who chooses "relaxed" as their current mood.
    mood_hungry : str
        Relevant quote and last words of encouragement given 
        to student who chooses "hungry" as their current mood. 
    mood_silly : str
        Relevant quote and last words of encouragement given 
        to student who chooses "silly" as their current mood.
    """
    
    # Quote and parting words of advice for students based on 
    # what mood they have chosen to be currently feeling, from:
    # happy, sad, frustrated, bored, overwhelmed, hopeful, excited,
    # relaxed, hungry, and silly.
    mood_happy = (" \n *** 'Create the highest, grandest vision possible for" +
                  " your life, because you become what you believe.'" +
                  " -Oprah Winfrey. \n Never take your happiness for" +
                  " granted. :D U r pawsome! *** \n ")
    mood_sad = (" \n *** 'There are only two ways to live your life. One is" +
                " as though nothing is a miracle. The other is as though" +
                " everything is a miracle.' -Albert Einstein \n When I" +
                " am sad, I ask hooman to play fetch with me. However," +
                " I don't think know how effective that is for you." +
                " Sadness is really a tough one, there are just so many" +
                " angles to it... if only I could make you feel better" +
                " with just one quote. This too shall pass, my" +
                " fur-end! *** \n ")
    mood_frustrated = (" \n *** 'If you can't fly, then run, if you can't" +
                       " run, then walk, if you can't walk, then crawl," +
                       " but whatever you do, you have to keep moving" 
                       " forward.' -Martin Luther King Jr. \n" +
                       " Frustration is extremely stressful, but keep" +
                       " going! No need to terrier-self up about it." +
                       " The end is near! Soon you will find peace of" +
                       " mind. I'm rooting for you! *** \n ")
    mood_bored = (" \n *** 'The time is always right to do what is right.'" + 
                  " -Martin Luther King Jr. \n Go out and get some" +
                  " fresh air! Or take this time to educate yourself" +
                  " on current worldwide issues. This is a perfect" +
                  " op-paw-tunity! There is no such thing as being" +
                  " overeducated! :D *** \n ")
    mood_overwhelmed = (" \n *** Believe you can and you're halfway there.'" +
                        " -Theodore Roosevelt \n Don't stress" +
                        " yourself out, Puppy believes in you! You have" +
                        " so much pet-tential! :D *** \n ")
    mood_hopeful = (" \n *** ' All of our dreams can come true if we have" +
                    " the courage to pursue them.' -Walt Disney \n" +
                    " Anything is paw-sible! :-) *** \n ")
    mood_excited = (" \n *** 'You're only given a little spark of madness." +
                    " You mustn't lose it.' -Robin Williams \n Looks like" +
                    " fun things are happening in your life! Must be" +
                    " having the ulti-mutt time of your life!! :D *** \n ")
    mood_relaxed = (" \n *** 'Rest and be thankful.' -William Wadsworth \n" +
                    " Good for you! Hope you live long and paws-per! :)" +
                    " *** \n ")
    mood_hungry = (" \n *** I see that you're hungry. I am always hungry, but" +
                   " my hooman only feeds me three times a day. How" +
                   " prepawsterous! I hope you realize you are lucky to" +
                   " have such long legs and arms to walk to the fridge" +
                   " and grab yourself some food! Might I recommend" +
                   " pup-eroni pizza...?  *** \n ")
    mood_silly = (" \n *** 'Why did the man fall into the well? He couldn't" +
                  " see that well!' \n If you're feeling silly, you" +
                  " probably like puns. Hope you got a good chuckle out" +
                  " of that one! I thought it was howlarious! :D *** \n ")
    
    # Based on what mood the student feels, will return the corresponding
    # statement through if statements.
    if mood == 'happy':
        return(mood_happy)
    elif mood == 'sad':
        return(mood_sad)
    elif mood == 'frustrated':
        return(mood_sad)
    elif mood == 'bored':
        return(mood_bored)
    elif mood == 'overwhelmed':
        return(mood_overwhelmed)
    elif mood == 'hopeful':
        return(mood_hopeful)
    elif mood == 'excited':
        return(mood_excited)
    elif mood == 'relaxed':
        return(mood_relaxed)
    elif mood == 'hungry':
        return(mood_hungry)
    elif mood == 'silly':
        return(mood_silly)
