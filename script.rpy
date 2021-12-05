# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Zeil")
define unknown = Character("???")
define m_name = "Me"
define m = DynamicCharacter("m_name")
define n = Character("")

define mom = Character("Mom")

image eileenShadow:
    "eileen concerned copy.png"

style shadow is image:
    color "#000"

define blink_transition_down = CropMove(0.1, mode = "wipedown", startcrop=(0.0, 0.0, 0.0, 1.0), startpos=(0.0, 0.0), endcrop=(0.0, 0.0, 1.0, 1.0), endpos=(0.0, 0.0), topnew= False)
define blink_transition_up = CropMove(0.1, mode = "wipedown", startcrop=(0.0, 0.0, 0.0, 1.0), startpos=(0.0, 0.0), endcrop=(0.0, 0.0, 1.0, 1.0), endpos=(0.0, 0.0), topnew= False)


default points = 0


# The game starts here.

label start:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    stop music fadeout 5.0

    scene bg_hospital_room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    m "."
    m ".."
    m "..."

    m "Who am I?"

    scene entrance - dark night
    with fade

    play music "audio/dream.mp3" volume 1.0

    m "I don't know who I am."
    m "I have wrinkled skin. Brittle bones. Needles and syringes are pushing into my sides."
    m "I know I'm sick. I can feel it."
    m "But what is my name?"

    show black_screen
    with blink_transition_down

    unknown "..."

    hide black_screen

    show entrance - dark night
    with blink_transition_up

    show zeil shocked

    m "And who is she?"

    m "I can't remember. There's a faint part of her in my mind,
       but I can't remember the source."

    show zeil shocked
    with zoominout

    m "She was close to me, though. I know that."

    show zeil sad

    unknown "..."

    m "I can't hear what she's saying. My body won't let me summon the words to speak."

    m "I'm feeling sleepy again. It's getting harder and harder to blink, and
       my head feels even more foggy than before."

    m "It feels like the last time I will ever close my eyes."

    show black_screen
    with blink_transition_down

    m "I can't go yet."

    hide black_screen

    show entrance - dark night
    with blink_transition_up
    show zeil sad

    m "I need to know who she is. Why she's here,
       in this room, crying for me."

    show black_screen

    m "I need to know her name."

    show title_screen at center:
        yoffset 130
    with Fade(5.0, 1.0, 1.0, color= "#fff")

    n "It's said that when a person is about to die, they dream."

    scene galaxy_image

    n "Beaches, fields, cities, lights. A birthday, a first kiss,"

    n "a glimpse from the beginning to the end of their life."

    n "That is a dream. Beautiful, yet fleeting."

    n "A lifetime of one's life in a second,"

    n "dreams can help find what once was forgotten."

    show bg_hospital_room
    with fade

    n "Find your way."

    show city a s3st2 evening
    with fade

    n "Experience the good in life."

    show clubroom a st2 evening
    with fade

    n "Survive the bad in it."

    show kitchen dining day
    with fade

    n "Stick true to the story of your existence,"

    show zeil smile copy

    n "and a memory now dull may find itself lit."

    show black_screen
    with Fade(5.0, 1.0, 1.0, color= "#fff")

    jump act_1

label act_1:
    n "ACT 1: Childhood"
    scene kitchen dining day

    #play music "audio/hu.mp3" fadein 1.0 volume 0.5

    m "I awoke to the sound of a pan sizzling."

    m "The smell of bacon wafted through the air, and I
       could hear laughter in the next room."

    m "I could tell immediately where I was."

    m "My home."

    show mom at center:
        zoom 0.6

    mom "Good morning!"

    m "I was speechless."

    hide mom

    m "The last time I saw my mom was over 50 years ago,
        when I was still in school."

    show mom at center:
        zoom 0.6
    with dissolve

    m "I looked down at my hands."

    m "Firm, strong, and unsoiled by age."

    m "Am I young again?"

    show mom smile at center:
        zoom 0.6

    mom "Honey, you don't look so well. How'd you like a cup of orange juice?"

    m "I smiled."

    m "I wish I could stay, like this, forever."

    show apartment b living room day
    with fade

    m "My mom passed away when I was young."

    show personal room c day
    with fade

    m "A weak heart, they said. Too much stress in her life."

    show personal room c day
    with zoomin

    mom "Breakfast is ready!"

    show mom at center:
        zoom 0.6

    m "Something I've wondered for my entire life, "

    show mom smile at center:
        zoom 0.6
    with dissolve

    m "was whether I was the one to stress her out."

    mom "..."

    m "What should I do?"

    menu:
        "Stay with her":
            jump act_1_bad_end
        "Move on":
            jump act_1_conclusion

label act_1_bad_end:
    m "I know that this is a dream, and that I should move on."

    show mom at center:
        zoom 0.6

    n "Mom beckons."

    m "But home feels too comforting to let go."

    show black_screen
    with Fade(5.0, 1.0, 1.0, color= "#fff")

    n "BAD END 1: ENDLESS DREAM"

    return

label act_1_conclusion:

    m "It would be nice to stay in this dream forever."

    m "It would be nice to see my mom again, alive and well."

    m "But this is a dream, and nothing more."

    show zeil sad
    with fade

    m "I need to remember who I came for."

    show black_screen
    with Fade(5.0, 1.0, 1.0, color= "#fff")

    jump act_2

label act_2:
    n "ACT 2: College"

    n "The sound of a bell rung through the air."

    m "I opened my eyes."

    show school a s1st2 day
    with pixellate

    unknown "Hey! How's it hanging, you got any plans for the weekend?"
    unknown "I can't wait for fall break, this semester feels like its
             been too long already."
    unknown "Man, I could really use some coffee right now."

    n "Someone waved in the distance."

    unknown "Hey Will, what's up?"

    m "I suddenly felt a memory come back to me."

    m "So close, it was shocking how I lost it in the first place."

    m "My name."

    $ m_name = "Will"


    unknown "Will!"

    show eileenShadow
    unknown "Hey, get over here."

    scene clubroom a st2 evening


























    # This ends the game.

    return
