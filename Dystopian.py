"""Dystopian is a text adventure game set in a
dystopian society. Note that the game is currently beta.
Copyright Evan Thomas"""

# You can't copy and paste from a word processor
#into a python file
def spacer():
    print "\n===========================================================\n" * 2

def play_again():
    play_again = raw_input("\nWould you like to play again?")
    play_again = play_again.lower()
    if play_again == 'yes' or play_again == 'y':
        intro()
    else:
        print "The End."

def make_choice(options):
    number_of_choices = len(options.split('\n')) - 1 # -1 because of \n at prompt
    while True:
        try:
            choice = int(raw_input(options))
            if choice > number_of_choices:
                raise ValueError
            else:
                break
        except:
            print "\nPlease enter a number 1 - %d\n" % number_of_choices
            continue
    return choice

# Contains all death sequences. Use an integer as the argument
def die(death):
    while True:
        if death == 1:
            print '\n"Yeah, I need some food."'
            print "\nTobias kneels down, and grabs a bow off his back. You don't \
know how you didn't notice it before. \nHe slowly lines up with the deer and pulls \
back the string. SNAP! The wooden handle of the bow broke and hit Tobias on the head."
            raw_input()
            print "Tobias was knocked back from being hit and law still on the ground a \
drops of blood oozed from his head. \nAs your eyes grew heavy, you heard a howl, \
and five large dogs charged into the clearing and rip open Tobias' body, eagerly devouring his insides.\n\
Your vision goes dark.\n"
            break

        elif death == 2:
            print '''\n"Oh. You're right, the world will always be like this. There is no \
hope."'''
            print "Tobias looks up at you, his face is pale and his eyes look dull.\n"
            print '''"Well then, goodbye friend. I guess I always knew it would come
to this."\n'''
            print "Tobias picks up the knife holstered on his belt and plunges it into his heart."
            print "Your vision goes dark."
            break

        else:
            print "Change parameter for die() to an integer."
            break

    spacer()
    raw_input("Press Enter")
    play_again()

# Put raw input in between long paragraphs
def intro():
    raw_input("\nWelcome To Dystopian! Press Enter to continue:")
    print '''\nYour eyes flicker open. Looking around,
you realize that you are in some kind of room, an apartment maybe.'''
    raw_input()
    print '''The floor is littered with cans of food and some books.
Except for the uncomfortable wooden chair you are sitting on, the apartment is bare of furnishings.
A window is directly in front of you, offering a view of dilapidated skyscrapers, the sides of which are painted
green from the countless vines clinging to the building's concrete.'''
    raw_input()
    print '''A noise from behind you interrupts your observations. Turning your head,
you see a tall boy, maybe seventeen or eighteen years old. He must have been standing
behind you the entire time. He had jet black hair with long, pointed bangs complemented
by a pair of sharp black eyes. "Alright then, it's time to go."\n'''

    options = "1.What are you talking about?\n2.Go Where?\n> "
    make_choice(options)

    print '''\nMan, I must really be going nuts. Since when do imaginary friends talk back?'''

    raw_input("\n\tImaginary friend?\n")
    print '''The boy seems flustered. "Well of course. My name is Tobias and you're my imaginary friend. Right?"
You nod your head, even though that doesn't make sense. A look of relief comes over Tobias' face. "Man,
for a minute there, I thought I was going insane. It's too easy, you know...to go insane. That's what happened to everyone else."'''
    raw_input()
    print '''His voice becomes hesitant, "That's what happened to my parents. But not me. I'm the only one left. That's why I made you. You're my
safeguard against insanity. Otherwise, I might go insane, like the rest of them."'''
    print "Or maybe I already am insane..."
    print "I can't think like that! I'm wasting time. I'll talk some more after I get some food."
    print "Tobias walks out of the apartment, and you suddenly feel very sleepy...\n"
    raw_input("Press Enter to continue:")
    spacer()
    crossroad()

def crossroad():
    print '''You snap back awake - it feels like no time has passed
but around you is a dense collection of trees and bushes instead of the
dirty apartment walls. A slight breeze blows and the ground feels damp.'''
    raw_input()
    print '''"Hey, are you there? I know I said that I wouldn't talk to you until later,
but I could really use some help right now. That's why you exist after all -
to give me help - to keep me sane. Anyway, I just found tracks -- chaser tracks."

Tobias is pointing towards the ground in front of you where some paw prints lie.'''
    raw_input()

    print'''"They must be big - maybe 150lb each, and it's a big pack,"
Tobias' voice started growing shaky, "maybe five or six...or more." '''

    raw_input("\n\t\"Whoa. Slow down. What are chasers, and why are you getting so panicky?\"")

    print '''\n"Chasers are like wolves, except worse. The only time I've seen one was the night that a chaser killed my parents.
I only saw one that night, but I never forgot it. Since then I've been able to keep
track of where they are through their tracks, but I've never seen any so fresh or so many in the same place.
What should I do?"\n'''
    # The below code works only when options are split using \n
    options = "1.Run Home\n2.Continue Hunting\n> "
    choice = make_choice(options)

    if choice == 1:
        run_home()
    elif choice == 2:
        die(1)
    else:
        print "Something happened...exiting"
        exit(0)

def run_home():
    spacer()
    print "Yeah. I need to get out of here before anything really bad happens. \
I can live without food for a little while."
    print "\nTobias turns away and starts sprinting. This time, and \
you follow him out of the forest. "
    print "It only seems like a few minutes before Tobias suddenly stops."
    print '''\n"Look!" Tobias is pointing towards a stag not very far from where
you are standing, in between two oak trees.'''
    print '''\n"Should I kill it?"'''

    options = "1.No. Go home.\n2.Yes. You need to eat.\n> "
    choice = make_choice(options)

    if choice == 1:
        at_home()
    elif choice == 2:
        die(1)
    else:
        print "Something happened...exiting"
        exit(0)

def at_home():
    spacer()
    print '''"So, here we are...back home again. It's a good thing I ran because
I think those chasers were a lot closer than we thought. But look at this, I found
some kind of book on the way home - it was just lying out in the open! Let's look
at what it says!"'''
    raw_input()
    print '''Tobias opens the book. A lot of the text is illegible but you can
make out a few sentences:

'I made the world this way. If only...(the text is blurry at this point)
But it's no use. Things can't be undone. The world is destined to be like this
forever. (The rest is gibberish)  - Dr. Oliph O. McCarter' '''
    raw_input()
    print '''"Gosh that's dark. Do you think what he said was true, about the
world always being like this?"

Tobias' eyes were tearing up. He had a panicked look on his face.'''

    options = "1.Yes, I think it's true.\n2.Don't worry, we'll be fine\n> "
    choice = make_choice(options)

    if choice == 1:
        die(2)
    elif choice == 2:
        end_game()
    else:
        print "Something happened...exiting"

def end_game():
    print '''\n"Maybe not. Maybe I can change it! Thanks!\n'''
    print "Tobias is clearly in much better spirits. You feel content having helped \
Tobias. Your vision slowly grows fuzzy, and then dark."
    spacer()
    print "Congratulations! You just finished Dystopian! Play again to find alternate endings. \
(Hint: There are 4 in total)\n"
    raw_input("Press Enter to continue")
    play_again()

intro()
