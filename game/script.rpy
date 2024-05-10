# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
#
define a = Character("Aya", image = "Aya", who_color = "#F859C8")
define r = Character("Ren", image = "Ren", who_color = "#1C0B82")
define d = Character("Dave", image = 'd')

define bitright = Position(xalign = 0.2, yalign = 0.8)
define bitleft = Position(xalign = 0.8, yalign = 0.8)

define bitcenter = Position(xalign = 0.5, yalign = 0.5)

$ Player_name = renpy.input("What is your name?")
$ Player_name = Player_name.strip()

# Defining all the images
# background
image i_1 = im.Scale("background.jpg", 1920, 1080)
image bg2 = im.Scale("bg2.jpg", 1920, 1080)

image fig_1 = "1.png"
image fig_2 = "2.png"
image fig_3 = "3.png"
image fig_4 = "4.png"
image fig_5 = "5.png"
image fig_6 = "6.png"
image fig_7 = "7.png"
image fig_8 = "8.png"
image fig_9 = "9.png"
image fig_10 = "10.png"
image fig_11 =  "11.png"
image fig_12 = "12.png"
image fig_13 = "13.png"
image fig_14 = "14.png"


# Aya
image Aya angry = "Aya angry.png"
image Aya blush = "Aya blush.png"
image Aya cry = "Aya cry.png"
image Aya frown = "Aya frown.png"
image Aya grin = "Aya grin.png"
image Aya neutral = "Aya neutral.png"
image Aya sad = "Aya sad.png"
image Aya scared = "Aya scared.png"
image Aya shocked = "Aya shocked.png"
image Aya smile blush = "Aya smile blush.png"
image Aya smile = "Aya smile.png"
image Aya smirk = "Aya smirk.png"

# Ren
image Ren angry = "Ren angry.png"
image Ren frown = "Ren frown.png"
image Ren laugh = "Ren laugh.png"
image Ren neutral = "Ren neutral.png"
image Ren sad = "Ren sad.png"
image Ren scared= "Ren scared.png"
image Ren shock blush= "Ren shock blush.png"
image Ren shock = "Ren shock.png"
image Ren shy blush = "Ren shy blush.png"
image Ren shy = "Ren shy.png"
image Ren smile blush= "Ren smile blush.png"
image Ren smile = "Ren smile.png"
image Ren smirk= "Ren smirk.png"

# This defines all of the pre-defined transitions beginning
# with "ease".
init python:
    define.move_transitions("ease", 1.0)

# # The game starts here.

label start:

    # Start by playing some music.
    play sound "background.mp3" loop
    # intro picture
    show i_1
    # intro welcome statement
    "Welcome to the History conversation."
    "We have with us Aya and Ren."

    # asking for player name
    $ Player_name = renpy.input("What is your name?")
    $ Player_name = Player_name.strip()

    # next bg

    # intro to the characters
    show Aya neutral with easeinright
    a "Hi [Player_name]! I'm Aya. Nice to meet you"
    # shift to the left
    show Aya neutral at right
    with dissolve



    show Ren neutral with easeinleft
    r "Hi! I'm Ren. Nice to meet you [Player_name]"
    # shift to the right
    show Ren neutral at left with dissolve


    # starting the conversation

    # Intro
    # Part 1


    # intro lines

    a smile "Guess what I learned about Aurangzeb and the British in history class today?"

    r smile "Hey Aya, what's up? Aurangzeb, huh? Isn't he the last big Mughal ruler?"

    # bg fig 1
    show fig_1 at bitcenter with dissolve

    a grin "Yeah, exactly! He controlled a huge chunk of what's now India. But after he passed away, things got chaotic."

    r shock "Chaotic? How so?"

    a neutral "Well, many Mughal governors and big landowners started doing their own thing, setting up their own mini-kingdoms."

    r frown "Sounds like a messy situation."

    a smile "Definitely! And guess who showed up on the scene? The British!"

    r smirk "Oh, those Brits! They always have a story, don't they?"

    a smile blush "You bet! They started off as a tiny trading company but ended up ruling a massive empire."

    r smile "Wait, how did they pull that off?"

    a frown "Beats me! Apparently, they weren't even trying to conquer land at first."

    r shock blush "Really? Then what changed?"

    a smirk "I guess they couldn't resist the temptation of power and riches!"

    r laugh "Typical! History's full of surprises, huh?"

    a grin "Absolutely! It's like a drama unfolding."

    r smile "Well, I'm curious to dive into that chapter now. Thanks for the sneak peek, Aya!"

    a smile blush "Anytime, Ren! Let's unravel the mystery of the British empire together!"
    # Quizzing

    hide fig_1

    # part 2
    a grin "Hey R, did you know the East India Company started off with Queen Elizabeth granting them a monopoly on trade in the East?"

    r shock "Really? So they had no competition?"

    a smile "Yep! They could sail across oceans, buy stuff cheap, then sell for big profits back in Europe."

    r frown "Sounds like a sweet deal. But what about other European powers?"

    show fig_2 at bitcenter with dissolve

    a frown "Portuguese were already in India, and the Dutch and French joined the party too."

    r frown "That must've led to some intense competition."

    a smile "You bet! They fought battles and blocked each other's routes for those prized goods like cotton, silk, and spices."

    r smirk "Did they play nice with local rulers?"

    a smirk "Not really. They built forts, bribed officials, and even got tax-free trade rights from Aurangzeb."

    r shock "But didn't that cause issues with revenue?"

    a smile blush "Big time! The Nawab of Bengal wasn't too happy about lost taxes."
    hide fig_2

    show fig_3 at bitcenter with dissolve
    r frown "So, A, what happened next with the East India Company and the Bengal nawabs?"

    a smile "Well, things got pretty heated. The nawabs like Murshid Quli Khan and Alivardi Khan weren't backing down."

    r shock "What were they upset about?"

    a neutral "They refused to give the Company any breaks, demanded hefty payments, and even stopped them from fortifying their settlements."

    r smile "Seems like a power struggle. What did the Company do?"

    a angry "The Company fought back, claiming the nawabs were ruining their trade by imposing unfair taxes."

    r shock "Did they find common ground?"

    a sad "Not really. The Company wanted to expand their settlements and forts, which only fueled the conflict."

    r smirk "And then what happened?"

    a grin "It all boiled down to the Battle of Plassey, a major showdown that changed everything!"

    hide fig_3
    show fig_4 at bitcenter with dissolve



    # part 3
    a shocked "Hey [Player_name], let me tell you what happened after the Battle of Plassey with Sirajuddaulah and the East India Company."

    r smile blush "Oh, I'm all ears! What happened next?"

    a grin "Well, after Alivardi Khan passed away, Sirajuddaulah became the nawab of Bengal. But the Company wasn't too happy with his power."

    r laugh "Why not? What did they want?"

    a neutral "They wanted a puppet ruler who'd give them trade concessions and privileges. So, they tried to help one of Sirajuddaulah's rivals take over, but he got really mad."

    r shock "Yikes! What did Sirajuddaulah do?"

    a smile "He captured Company officials, locked up their warehouse, and even marched to Calcutta to take over their fort."

    r shock blush "That sounds intense! What did the Company do?"

    a grin "They sent forces led by Robert Clive to sort things out. After negotiations failed, they battled it out at Plassey in 1757."

    r smile "And who won?"

    a sad "Clive's forces won, mainly because one of Sirajuddaulah's commanders didn't fight. Clive promised him power, and things took a turn."

    r neutral "What happened to Sirajuddaulah?"

    a neutral "He was out, and Mir Jafar was in as the new nawab. But this was just the start of the Company's power play."

    r shock "What did they do next?"

    a grin "The Company started flexing its muscles, making puppet nawabs dance to their tune."

    r frown "Did it work out for them?"

    a neutral "Sort of. They faced some bumps with Mir Qasim and others, but eventually, they got appointed as the Diwan of Bengal in 1765."

    r angry "Wow, that's a big step! What changed after that?"

    a neutral "Now they had the revenue to finance their trade and expand their influence."

    r smile "Seems like quite the adventure!"

    a grin "Absolutely! The Company officials even started living like nawabs themselves, amassing fortunes and flaunting their wealth."

    r smile "Sounds like a wild time in history!"

    a smile blush "Definitely! It's history full of drama and power struggles."

    hide fig_4

    hide Aya
    hide Ren

    show d normal at bitleft with dissolve
    # fade the music
    stop sound fadeout 1.0

    "Now Quiz Time"
    menu:
        "Are you ready..."
        "Yes":
            jump quiz
        "No. I need revision":
            pass

    # End of the script
    stop sound fadeout 1.0
    # This ends the game.

    return
label quiz:
    #Initialize score
    $ quiz_score = 0

    # 1st Question
    d speaking "which european country came first in India?"
    menu:
        "Portuguese":
            d normal "Correct"
            $ quiz_score += 1
        "Dutch":
            d normal "Wrong"

    # 2nd Question
    d speaking "when was battle of Plassey?"
    menu:
        "1757":
            d normal "correct"
            $ quiz_score += 1
        "1756":
            d speaking "wrong"

    hide d
    show Ren neutral at bitleft with dissolve

    # Check the quiz score
    if quiz_score == 2:
        # Win
        play sound "winning.mp3"
        r smirk "Winning winning .. "

    else:
        # Lose
        play sound "loss.mp3"
        r sad "You lose!!..Auuuuuuuugh!"
