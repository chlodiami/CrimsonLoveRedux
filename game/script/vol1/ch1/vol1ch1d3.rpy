label vol1ch1d3_start:
    scene bg bedroom day
    show hareka pajamas blinking smile_mouth
    with fade
    "I wake up at the same time as Hareka once more."
    mc "Good morning!"
    show hareka talking
    hareka "Good morning."
    show hareka smile_mouth
    "We both get out of bed and tidy up, then she leaves to make me breakfast once more."
    hide hareka with moveoutleft
    "This time I let her decide what to make for me."
    window hide
    pause 1.0
    show hareka pajamas blinking smile_mouth with moveinleft
    "She returns a few minutes later with a plate of toast. I take it, thanking her, and eat."
    "After I finish, she bins the plate, then we get dressed and ready for the day."
    scene bg bedroom day
    show hareka hair_band ribbon blinking smile_mouth
    with fade
    "Hareka turns to me."
    show hareka talking
    hareka "So, what do you want to do today?"
    show hareka smile_mouth
    mc "Well..."
    menu vol1ch1d3_activitychoice:
        "Reading":
            $ vol1ch1d3_activitychoice_v = "reading"
            mc "I'd like to do some more reading."
            show hareka talking
            hareka "Okay! I'll do some of my work then, while you do that."
            show hareka smile_mouth
            mc "Sounds good!"
            show hareka at left with move
            "Hareka goes to her desk, and I pick out a new book from the box, beginning to read."
        "Playing more games":
            $ vol1ch1d3_activitychoice_v = "board game"
            mc "I'd like to play another game today."
            show hareka talking
            hareka "Okay! What would you like to play?"
            show hareka smile_mouth
            mc "Hm..."
            "I take a moment to think."
            mc "Maybe Chess?"
            mc "You seem pretty good at strategic games."
            show hareka talking
            hareka "Okay, that sounds good!"
            show hareka smile_mouth
            "We grab the box and get out the Chess set, getting the board set up, and begin playing."
    scene bg bedroom day
    show hareka hair_band ribbon blinking smile_mouth
    "Lunchtime arrives, and Hareka makes me a chicken sandwich."
    mc "Thanks!"
    show hareka talking
    hareka "You're welcome."
    show hareka smile_mouth
    if vol1ch1d3_activitychoice_v == "reading":
        "I eat the sandwich, and then I continue reading, while Hareka types away on her laptop."
    else:
        "I eat the sandwich, and then we continue playing our game of Chess."
        window hide
        pause 1.0
        "We play for a few more rounds, and then decide to pack away. Hareka returns to her laptop, and I continue reading my book."
    show hareka closed_eyes at bounceUp
    "After a couple more hours, Hareka stands up."
    show hareka blinking talking
    hareka "Are you ready for dinner now?"
    show hareka smile_mouth
    mc "Oh, yes please!"
    "I fold the page to find my place later, standing up and stretching."
    mc "I really need to move around more..."
    "I chuckle."
    mc "Anyways, what's for dinner today?"
    show hareka closed_eyes
    show hareka talking
    hareka "You'll see."
    show hareka smile_mouth
    hide hareka with moveoutleft
    "She leaves to make the food, and I'm left waiting patiently for her return."
    window hide
    pause 1.0
    show hareka hair_band ribbon smile_mouth with moveinleft
    "She does return, of course, this time with a plate of butter chicken and pilau rice."
    mc "Mm, I love butter chicken!"
    show hareka talking
    hareka "Good. Eat up then."
    show hareka smile_mouth
    "I enjoy every bite."
    mc "You really are great at cooking."
    show hareka talking
    hareka "Thanks. You don't have to keep saying that though."
    show hareka smile_mouth
    mc "I mean it!"
    show hareka closed_eyes
    "She averts her gaze."
    show hareka talking
    hareka "Just eat the food."
    show hareka smile_mouth
    "I chuckle."
    mc "Okay then."
    "I finish the food quickly and bin the plate."
    "..."
    "Then I realise something."
    mc "Um..."
    show hareka blinking talking
    hareka "What?"
    show hareka smile_mouth
    "I gulp."
    mc "Uh, it's been a few days since I've... had a shower..."
    show hareka talking
    hareka "Oh. You want one?"
    show hareka smile_mouth
    "I nod, embarrassed."
    show hareka closed_eyes neutral_mouth
    "She closes her eyes, contemplating for a moment."
    show hareka talking
    hareka "You're not allowed out of this room."
    show hareka neutral_mouth
    mc "Yeah..."
    show hareka blinking talking
    hareka "So how do you expect to shower?"
    show hareka neutral_mouth
    mc "Well isn't it a basic human right?!"
    "I begin to get slightly defensive again, raising my voice a bit."
    show hareka talking
    hareka "Calm down."
    show hareka neutral_mouth
    mc "Nnng... Don't tell me to calm down! You-"
    show hareka at center:
        ease 0.5 zoom 1.5 yanchor 0.8
    "She grabs my shoulders, startling me."
    window hide
    show hareka closed_eyes
    pause 0.5
    show hareka smile_mouth
    pause 0.5
    show hareka sad_blinking
    pause 0.5
    show hareka talking
    hareka "Please. Take some deep breaths."
    show hareka smile_mouth
    mc "What...?"
    show hareka talking
    hareka "Trust me."
    show hareka smile_mouth
    "Her grip is firm but not hurtful. She maintains eye contact with me."
    mc "...Okay..."
    show hareka talking
    hareka "Good. Now... Take a deep breath in."
    show hareka smile_mouth
    "I inhale deeply."
    show hareka sad_closed_eyes talking
    hareka "Now let it out."
    show hareka smile_mouth
    "I exhale."
    show hareka sad_blinking talking
    hareka "In..."
    show hareka smile_mouth
    "I inhale again."
    show hareka sad_closed_eyes talking
    hareka "And out..."
    show hareka smile_mouth
    "We repeat this a few times, until I begin to feel much calmer."
    show hareka sad_blinking
    mc "Thanks..."
    show hareka talking
    hareka "You're welcome."
    show hareka smile_mouth
    ## fall
    #show hareka:
        #easeout 0.5 zoom 1.0 yanchor 0.0
    #hareka "i fell help ;.;"
    show hareka:
        easeout 0.5 zoom 1.0 yanchor 1.0
    ## fall 2: electric boogaloo
    #hide hareka with moveoutbottom
    "We both smile awkwardly."
    "It's odd... She's being so nice to me despite being my captor... I don't know if I should be relieved or scared, to be honest…"
    show hareka talking
    hareka "Now then. Just give me a moment."
    show hareka smile_mouth
    mc "Okay..."
    show hareka at left with move
    "She heads to the desk and opens a drawer, pulling out a fancy-looking phone, and dials a number."
    hide hareka with moveoutleft
    "To my disappointment, she leaves the room, so I can't earwig the conversation. I have to wait for her to return."
    window hide
    pause 1.0
    show hareka hair_band ribbon smile_mouth with moveinleft
    "She does, a little while later."
    mc "Well? Who was that?"
    show hareka talking
    hareka "You sure are nosey."
    show hareka closed_eyes smile_mouth
    "She chuckles."
    show hareka blinking talking
    hareka "It's my manager."
    show hareka smile_mouth
    mc "Oh!"
    show hareka talking
    hareka "I spoke to her about your dilemma, and she gave me permission to let you out of the room to shower and tend to hygiene, providing I'm in the room with you at all times."
    show hareka smile_mouth
    mc "Oh... That doesn't seem too bad..."
    show hareka talking
    hareka "Are you sure you don't mind?"
    show hareka smile_mouth
    mc "Why would I?"
    show hareka sad_closed_eyes talking
    hareka "Because..."
    show hareka sad_mouth
    pause 0.5
    show hareka blush
    "Her face goes a bit red, surprisingly."
    show hareka talking
    hareka "I have to watch you bathe..."
    show hareka sad_mouth
    mc "Oh..."
    "I laugh."
    mc "We're both girls, right? It's fine!"
    show hareka sad_blinking talking
    hareka "Really?"
    show hareka sad_mouth
    mc "Yeah! I don't care too much."
    show hareka talking
    hareka "Oh... Okay..."
    show hareka sad_closed_eyes sad_mouth
    "She seems to be much more embarrassed than I am about this fact. How funny. I'll definitely tease her about this later."
    "I grab my pyjamas, and we head into the bathroom."
    scene bg bathroom
    show hareka hair_band ribbon sad_blinking sad_mouth at right
    with fade
    "The bathroom is rather small, but very clean, just like her bedroom."
    show hareka talking
    hareka "Sorry but, there's only a bath here, no shower."
    show hareka sad_mouth
    mc "Oh, that's fine. I can make do with a bath."
    show hareka talking
    hareka "Okay then."
    show hareka sad_mouth
    pause 0.5
    show hareka sad_closed_eyes blush
    "I get undressed, and Hareka's face turns red again. I laugh."
    mc "You're such a baby."
    show hareka sad_blinking talking
    hareka "Am not!"
    show hareka sad_mouth
    mc "Am too!"
    show hareka sad_closed_eyes pouty_mouth
    "She pouts, and I laugh more."
    mc "Come on, it's nothing you haven't seen before."
    show hareka sad_blinking talking
    hareka "True but... Surely you're embarrassed too?"
    show hareka sad_mouth
    mc "No, I'm not."
    show hareka sad_closed_eyes
    "She sighs."
    show hareka talking
    hareka "Jeez..."
    show hareka sad_mouth
    "I run the bath, making sure the water is the correct temperature, and get a towel ready."
    show hareka sad_blinking at quarterright with move
    "I notice from the corner of my vision that Hareka has approached the bath and watch curiously as she dips her hand in the water."
    "I approach her."
    mc "What'cha doing?"
    show hareka talking
    hareka "Oh... Nothing..."
    show hareka sad_mouth at right with move
    "She steps back awkwardly."
    mc "You sure are acting strange..."
    show hareka talking
    hareka "How so?"
    show hareka sad_mouth
    "I shake my head."
    mc "Ah, never mind."
    "I get in the bath. It's the perfect temperature, nice and warm for this harsh winter. I sink into the water, relaxing a bit."
    show hareka closed_eyes
    pause 0.5
    show hareka -blush
    pause 0.5
    show hareka talking
    hareka "Is it nice?"
    show hareka sad_mouth
    mc "Yeah, it is..."
    show hareka blinking
    "She pulls out her phone from her pocket. I didn't even notice she'd put it in her pocket..."
    mc "You're not gonna take nude photos of me, are you?"
    show hareka blush at bounceUp
    "I remark, smirking. Her face goes bright red."
    show hareka talking
    hareka "No! I'd never!"
    show hareka sad_mouth
    "I laugh."
    mc "Relax, it was a joke."
    show hareka closed_eyes pouty_mouth
    hareka "Uuu..."
    show hareka blinking
    "She puts the phone to her ear."
    show hareka talking
    hareka "Look, I'm taking this phone call, okay? I'll be back in a minute."
    show hareka sad_mouth
    mc "Huh, what about having to keep strict monitoring on me?"
    show hareka talking
    hareka "I'll just be a minute!"
    show hareka sad_mouth
    hide hareka with moveoutright
    "She basically runs out the bathroom."
    "Poor girl seems to be so shy around naked bodies... Not sure why..."
    "I wash myself thoroughly, my hair and body, then sink back down again, enjoying this moment of alone time."
    show hareka pajamas closed_eyes sad_mouth at right with moveinright
    "She returns a few minutes later, seemingly calmed down, and in her pyjamas. She still doesn't really look at me though. Oh well."
    "I finish my bath, dry off, and get into my pyjamas, then we return to the bedroom."
    scene bg bedroom night
    show hareka pajamas blinking smile_mouth
    with fade
    mc "Bedtime..."
    show hareka talking
    hareka "Yep."
    show hareka sad_mouth
    "We both get into bed."
    mc "Well, goodnight Hareka!"
    show hareka talking
    hareka "Goodnight!"
    show hareka smile_mouth
    pause 0.5
    scene black
    with fade
    "{b}Volume 1 - Chapter 1 - Day 3{/b} complete!"
    menu vol1ch1d3_endmenu:
        "Would you like to return to the selection screen, or carry onto the next chronological day?"
        "Return to the selection screen":
            jump volumeselect
        "Carry onto the next day":
            jump vol1ch1d4_start