
define h = Character("Hanako", color="#8A7587", image="hanako", what_prefix='“', what_suffix='”')
define l = Character("Lilly", color="#F8F3B6", image="lilly", what_prefix='“', what_suffix='”')
define me = Character("Meito", color="#1A73E8", what_prefix='“', what_suffix='”')
define m = Character("Miki", color="#AD735E", image="miki", what_prefix='“', what_suffix='”')

label start:
    $ quick_menu = False
    stop music fadeout 1
    hide screen main_menu
    scene blackout 
    with Dissolve(0.5)
    
    pause 1.0
    
    play music "Lullaby_of_Open_Eyes.ogg" fadein 1

    window show Dissolve(0.2)
    $ quick_menu = True
    "I wish I was born normal..."
    "To have a normal heart..."
    
    #python:
    #    studio_init()
    
    "Able to go to a normal school..."
    "Live in a normal society..."
    "..."
    "Well..."
    "Maybe I haven't fully accept that there's no normal."
    "People here and there are all different."
    "\"Normal\" doesn't exist, it only makes fake standards."
    "We are all incomplete, a non-perfect creatu- {w=1}{nw}"
    $ quick_menu = False
    window hide Dissolve(0)
    
    stop music
    play sound "wumph.ogg"
    scene school_scienceroom
    show miki grin 
    with vpunch
    
    pause 0.5
    
    window show Dissolve(0.2)
    $ quick_menu = True
    m grinclosed "Wake up, my dude!"
    m "School is over!"
    me "Ah, sorry. I accidentally slept."
    m smile "It's fine."
    m wink "If I'm not here, you'd probably be sleeping here overnight!"
    me "Hahaha, that's very kind of you."
    m "Sure thing."
    m smile "Anyway, see ya around!"
    
    hide miki with Dissolve(0.4)
    pause 0.5
    
    "..."
    "I actually don't mind being here."
    "Since I have friends and I think that's all that matters for me."
    $ quick_menu = False
    window hide Dissolve(0.4)
    pause 0.4
    
    scene blackout with Dissolve(1)
    pause 1
    
    play sound "Passing_of_Time.ogg"
    show logo_large with ImageDissolve("tr-clockwipe.png", 2.2):
        align(0.5, 0.5) zoom 1.5
    pause 2.2
    hide logo_large with ImageDissolve("tr-clockwipe.png", 2.2)
    stop sound fadeout 1
    pause 1
    
    jump day_1

label day_1:
    scene school_gate with Fade(0.5, 0.2, 0.5, color="#000")
    play music "Daylight.ogg" fadein 1
    pause 0.2
    
    window show Dissolve(0.2)
    $ quick_menu = True
    "Today I will be having a meeting with Lilly from the next classroom."
    "We'll mostly be discussing about the upcoming school event."
    "I haven't seen her before, but I heard rumours spread about her."
    "Some said she's from Ireland, others said her attitude is like an angel."
    "I believe that last one is a joke, but I can't get it off my head."
    $ quick_menu = False
    window hide Dissolve(0.2)
    
    scene school_hallway with Fade(0.5, 0.2, 0.5, color="#000")
    
    window show Dissolve(0.2)
    $ quick_menu = True
    "As I'm walking down the hall, I spot someone I know."
    $ quick_menu = False
    window hide Dissolve(0.2)
    show hanako def_worry with Dissolve(0.4)
    window show Dissolve(0.2)
    $ quick_menu = True
    me "Good morning, Hanako!"
    $ quick_menu = False
    window hide Dissolve(0)
    show hanako defarms_shock
    with vpunch
    pause 0.4
    window show Dissolve(0.1)
    $ quick_menu = True
    h "G-Good morning, M-Meito."
    me "Sorry for making you startled again."
    h defarms_worry "I-"
    h def_worry "It's fine."
    $ quick_menu = False
    window hide Dissolve(0.2)
    pause 0.4
    
    scene school_scienceroom with Fade(0.5, 0.2, 0.5, color="#000")
    play sound "crowd_indoors.ogg" loop fadein 1
    pause 0.2
    
    window show Dissolve(0.2)
    $ quick_menu = True
    "Today's class goes by fast."
    "Some students, however, cannot care less about it and slept the entire round."
    "..."
    "......"
    "Oh yeah. I should probably go to Lilly's classroom now."
    $ quick_menu = False
    window hide Dissolve(0.2)
    
    show hanako emb_blushdowntimid with Dissolve(0.4)
    window show Dissolve(0.2)
    $ quick_menu = True
    h "M-Meito."
    me "Huh?"
    "As I'm about to head out, Hanako stops me midway."
    h "Uh... Can I ask you something?"
    me "What is it?"
    h emb_blushtimid "Uhm... I was thinking if we could go to the library together."
    h "I-I think we can read some books together."
    "Why so sudden, Hanako?"
    
    menu:
        "Hmm... I think I should..."
        
        "Go to the meeting.":
            me "I'm sorry, Hanako."
            show hanako emb_blushing
            me "But I have a plan today."
            h emb_blushdowntimid "A-ah, sorry!"
            h emb_blushsad "I didn't mean to interrupt you."
            h emb_blushdownsad "I'm really sorry, Meito."
            $ quick_menu = False
            window hide Dissolve(0.1)
            hide hanako with Dissolve(0.3)
            window show Dissolve(0.2)
            $ quick_menu = True
            "She runs away with her face fully red."
            "*Sigh*"
            "I stand up and move out from the room."
            $ quick_menu = False
            window hide Dissolve(0.2)
            
            stop sound fadeout 1
            stop music fadeout 1
            pause 1.2
            
            jump meeting
            
        "Accompany Hanako to the library":
            me "Sure. Let's go."
            h emb_smile "mhm."
            $ quick_menu = False
            window hide Dissolve(0.2)
            show hanako emb_smile with Dissolve(0.2)
            pause 0.2
            
            stop sound fadeout 1
            stop music fadeout 1
            pause 1.5
            
            jump library
    
label meeting:
    scene school_room32 with Fade(0.5, 0.2, 0.5, color="#000")
    
    play music "Concord.ogg" fadein 1
    
    pause 0.4
    
    window show Dissolve(0.2)
    $ quick_menu = True
    "As I entered the class, I can feel the change of atmosphere greets me."
    l "Could it be Meito from the next class?"
    "She picked up my precense very fast."
    me "Yeah, it's me, Meito."
    l "Please take a seat."
    $ quick_menu = False
    window hide Dissolve(0.2)
    
    pause 0.4
    #Sit down
    show lilly smileclosed:
        subpixel True
        ypos 40 xalign 0.5 alpha 0.0
        parallel:
            easein 0.5 ypos 0
        parallel:
            easein 0.5 alpha 1.0
    pause 0.5
    
    window show Dissolve(0.2)
    $ quick_menu = True
    "She's drinking what seems to be a cup of tea."
    "Her finger caresses on the handle each time she pulls it up to her mouth."
    l "Meito. I heard you are recently transferred to this school, is it not?"
    me "Yeah. I'm still very much new here."
    "She nods slowly as she sips her tea."
    l "Sorry for the sudden, but do you mind if I request something to you?"
    me "Sure, what is it?"
    l weaksmile "Since the school festival is coming up in the next few weeks, I want you to help our class on it."
    me "Hm? What help do you want me to do?"
    l "Our students here have either total or near-total visual impairment, so it would be grand if you could set up some of the decorations."
    l smileclosed "Of course, we would be very thankful for your hardwork."
    me "I would help you, but why do you choose me?"
    show lilly displeased
    "She sips her tea before speaking again."
    l "To put it simply, you are the only student left that have not contributed to the festival."
    "*Sigh* I knew coming to this school won't be easy."
    me "Alright. I think I can handle it for your class."
    l smileclosed "I am as the class representative would thank you very much."
    me "Haha, no problem."
    me "If I may ask, When can I start working on it?"
    l "Oh, you can begin doing so tomorrow."
    l "Feel free to come to our class, we would kindly help you if you need one."
    me "Alright. I'll do my best."
    l "Once again, thank you, Meito."
    me "Hahaha, it's fine..."
    me "I think I'm going to head out now."
    l "Very well, see you."
    me "See you, Lilly."
    $ quick_menu = False
    window hide Dissolve(0.2)
    
    stop music fadeout 1
    pause 0.4
    hide lilly smileclosed with Dissolve(0.4)
    pause 0.6
    
    jump lilly_end
    
label library:
    scene school_library with Fade(0.5, 0.2, 0.5, color="#000")
    pause 0.4
    
    play music "Everyday_Fantasy.ogg"
    
    window show Dissolve(0.2)
    $ quick_menu = True
    "Library is quiet as usual."
    "There are only a few other students reading, some are obviously sleeping in the corner."  #Scrapped idea: reading textbook
    $ quick_menu = False
    window hide Dissolve(0.2)
    
    show hanako normal with Dissolve(0.5)
    
    window show Dissolve(0.2)
    $ quick_menu = True
    h "Meito, I think I found an interesting book."
    me "Huh? Is that a book about chess strategies?"
    h smile "Mhm!"
    "Hanako has been a chess player since her middle school."
    "Her skill is way beyond mine even though I've known it since childhood."
    "She should have gone to chess tournament one day..."
    "... Only if she's not so shy in public."
    h worry "Meito? Are you okay?"
    me "Y-Yes, I'm fine. I think it's a great book."
    show hanako normal
    me "It would be better if we read and play it."
    h bashful "Mhm, agree!"
    $ quick_menu = False
    window hide Dissolve(0.2)
    
    pause 0.4
    
    scene school_library_ss 
    show hanako distant
    with Fade(0.5, 0.4, 0.5, color="#000")
    
    window show Dissolve(0.2)
    $ quick_menu = True
    "We had some fun and intense matches after that."
    me "Huff, that was tough."
    h smile "I learned a lot of new moves today."
    h bashful "Thank you, Meito."
    me "You're welcome."
    me "The sun is setting, I think we should pack up soon."
    h worry "You're right."
    "We clean the table we used to play chess and put everything back."
    me "Are you going to borrow this book?"
    h bashful "Yes. This book is very helpful."
    me "That's good then. We can play again sometimes."
    show hanako emb_smile
    "She nods and then we head out of the library."
    $ quick_menu = False
    window hide Dissolve(0.2)
    
    stop music fadeout 1
    pause 0.4
    
    jump hanako_end
    
label hanako_end:
    play sound "cicadas.ogg" fadein 2 loop
    scene school_dormext_start_ss
    show hanako emb_blushtimid
    with Fade(0.5, 0.4, 0.5, color="#000")
    pause 0.2
    
    window show Dissolve(0.2)
    $ quick_menu = True
    h "Uhm, Meito..."
    me "Yeah?"
    h emb_smile "T-Thank you again for accompanying me today."
    me "..."
    me "No problem. It was a pleasure."
    "We waved at each other and parted off."
    $ quick_menu = False
    window hide Dissolve(0.2)
    
    pause 0.2
    hide hanako emb_smile with Dissolve(0.4)
    stop sound fadeout 2
    pause 1
    
    scene school_dormhisao with Fade(0.5, 0.2, 0.5, color="#000")
    pause 0.2
    
    window show Dissolve(0.2)
    $ quick_menu = True
    "I put my school bag on the floor and jump head first to my bed."
    "..."
    "*Sigh*"
    "Today I had a blast with Hanako."
    "I wonder if we will meet again..."
    "No. We definitely will meet again."
    "..."
    "......"
    "My eyes are starting to feel heavy now."
    "I should just let my body sleep..."
    $ quick_menu = False
    window hide Dissolve(0.4)
    
    pause 0.2
    scene blackout with Dissolve(1)
    pause 1
    
    $ persistent.hanako_end = True
    
    ## CREDITS   #special tahnks to Bambang, Udin, Ucok.
    jump credits
    
    
label lilly_end:
    scene school_dormext_start with Fade(0.5, 0.4, 0.5, color="#000")
    pause 0.2
    
    play sound "parkambience.ogg" fadein 1 loop
    
    window show Dissolve(0.2)
    $ quick_menu = True
    "I decided to walk to my dorm after the meeting."
    "Honestly, how come no one says anything about the school festival?"
    "If I've known it before, I'd probably have helped my class instead of hers..."
    "But Lilly's class do seem to be in trouble though..."
    "..."
    "......"
    "Maybe..."
    "Just maybe..."
    "There's a silver lining after it all..."
    $ quick_menu = False
    window hide Dissolve(0.4)
    
    stop sound fadeout 1
    pause 0.4
    
    scene blackout with Dissolve(1)
    pause 1
    
    $ persistent.lilly_end = True
    
    jump credits
    
label credits:
    play sound "Credits.mp3"
    
    show screen credit
    
    pause
    pause 
    
    $ renpy.rollback(force=False, checkpoints=1, defer=False, greedy=True, label=None, abnormal=True)  #Just an alternative. Could've used call screen, but meh.