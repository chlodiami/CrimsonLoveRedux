label vol1ch1d2_start:
    scene bg bedroom day
    with fade
    "I slowly awaken. The soft pitter patter of rain on the window is the first thing I hear."
    "I smile to myself. A new day..."
    hareka "Good morning."
    show hareka pajamas blinking smile_mouth with dissolve
    "I turn my head to see Hareka sitting on her mattress on the floor."
    "By her dishevelled appearance, it seems she's also just woken up."
    mc "Oh, good morning!"
    show hareka talking
    hareka "Did you sleep well?"
    show hareka smile_mouth
    mc "Uh, yeah, I think I did. Did you?"
    show hareka talking
    hareka "I did."
    show hareka smile_mouth
    "We both get up. I make my bed and Hareka tidies up her area."
    show hareka talking
    hareka "Would you like breakfast now?"
    show hareka smile_mouth
    mc "Yes please!"
    show hareka talking
    menu vol1ch1d2_breakfastchoice:
        hareka "What would you like?"
        "Chocolate cereal":
            $ vol1ch1d2_breakfastchoice_v = "chocolate cereal"
        "Toast":
            $ vol1ch1d2_breakfastchoice_v = "toast"
        "Pancakes":
            $ vol1ch1d2_breakfastchoice_v = "pancakes"
    hareka "Okay, please wait here. I'll return shortly."
    show hareka smile_mouth
    hide hareka with moveoutleft
    "Hareka leaves."
    "While waiting, I get dressed and fold the pyjamas neatly, placing them on my pillow."
    show hareka pajamas blinking smile_mouth with moveinleft
    "She returns a few minutes later with [vol1ch1d2_breakfastchoice_v]. I take it gratefully."
    mc "Thank you!"
    show hareka talking
    hareka "You're welcome."
    show hareka closed_eyes smile_mouth
    "I eat my [vol1ch1d2_breakfastchoice_v] happily."
    "She waits patiently for me to finish, tidying her appearance."
    show hareka -pajamas with dissolve
    show hareka hair_band ribbon with dissolve
    "When I'm done, I put the paper plate in the bin, then turn back to her."
    mc "So, what should we do today?"
    show hareka blinking talking
    hareka "What would you like to do? Within this room, of course."
    show hareka smile_mouth
    mc "I'm not entirely sure what's available..."
    show hareka talking
    hareka "Hm."
    show hareka smile_mouth at right with move
    "She heads over to the closet and pulls out another box, this time full of board games."
    show hareka at center with move
    mc "Oh!"
    show hareka talking
    hareka "I hope these are enough to keep you occupied for a bit."
    show hareka smile_mouth
    mc "Thank you!"
    "I shuffle through what's in the box. There's a few games here. Connect 4, Chess, Naughts & Crosses..."
    mc "Yes, I'm sure this will be enough, alongside the books you gave me yesterday."
    show hareka talking
    hareka "Good."
    show hareka smile_mouth at left with move
    "She sits at her desk and boots up her laptop. I'm left with the two boxes."
    menu vol1ch1d2_activitychoice:
        "What activity should I do today?"
        "Reading quietly":
            $ vol1ch1d2_activitychoice_v = "reading"
            "I pick the box with the books."
            "Shuffling through them again, I find one that catches my eye, and begin reading."
            "The story really draws me in once more. I'm captivated."
            "I'd never have thought Hareka had such good taste in this..."
        "Play a board game with Hareka":
            $ vol1ch1d2_activitychoice_v = "board game"
            "I pick the box with the board games."
            "After some thinking, I decide on Connect 4, and approach Hareka."
            mc "Hey, Hareka?"
            show hareka talking
            hareka "Yes?"
            show hareka smile_mouth
            mc "Would you like to play this game with me? It's a two-player one, so..."
            "I hope I'm not bothering her too much..."
            show hareka talking
            hareka "Sure!"
            show hareka smile_mouth
            mc "Oh, thanks!"
            show hareka at center with move
            "We set up the game, and begin to play."
            "I've always been terrible at strategic tasks, and so Hareka beats me easily."
            "Still, it's fun! She seems to be enjoying herself a bit too!"
    scene bg bedroom day
    if vol1ch1d2_activitychoice_v == "reading":
        show hareka hair_band ribbon smile_mouth at left
    else:
        show hareka hair_band ribbon smile_mouth
    with fade
    "Lunchtime rolls around."
    "Hareka heads to the kitchen to make lunch, and returns shortly after, with a cheese wrap and water."
    mc "Thanks!"
    show hareka talking
    hareka "You're welcome."
    show hareka smile_mouth
    "I eat the food."
    mc "Hey, I just realised something."
    show hareka talking
    hareka "What is it?"
    show hareka smile_mouth
    "I look up at her."
    mc "I've never seen you eat since I met you."
    show hareka sad_blinking talking
    hareka "Well."
    show hareka sad_closed_eyes sad_mouth
    "She averts her gaze, to my surprise."
    show hareka talking
    hareka "We've only just met, so you have hardly seen anything of me..."
    show hareka sad_mouth
    "She shuffles, clearly uncomfortable."
    "This is new to me. She's usually pretty apathetic, from what little I've witnessed..."
    "I sigh."
    mc "Sorry if I made you uncomfortable."
    show hareka sad_blinking talking
    hareka "Oh, no, it's fine."
    show hareka sad_mouth
    mc "Are you sure?"
    hareka "Mhm."
    mc "Okay..."
    "I finish my lunch in silence."
    if vol1ch1d2_activitychoice_v == "reading":
        "After lunch, Hareka returns to her laptop and I go back to reading my book."
    else:
        "After lunch, we decide to continue the games another time, and pack away the stuff. Hareka returns to her laptop and I grab a new book to read."
        show hareka at left with move
    scene bg bedroom evening
    show hareka hair_band ribbon smile_mouth at left
    with fade
    "A few hours later, it's dinnertime."
    hide hareka with moveoutleft
    "Hareka heads back to the kitchen to prepare dinner, and I'm left alone once more while she does."
    "I always get a harsh pang of loneliness whenever she leaves. She's probably the only company I'll have for a long time, so I can't let my paranoia ruin our already murky relationship..."
    show hareka hair_band ribbon smile_mouth at left with moveinleft
    "She eventually returns, bringing me a steaming plate of fish and chips with mushy peas, and once again, the cup of water."
    mc "Mm, this is so good again!"
    show hareka talking
    hareka "I'm glad you like it."
    show hareka smile_mouth
    mc "Thank you!"
    show hareka closed_eyes talking
    hareka "You always thank me. Just take it."
    show hareka smile_mouth
    mc "Oh, okay..."
    "I eat gladly."
    "When finished, she bins the plate, and we go back to our separate activities for a while, and then the darkness of night sets in."
    scene bg bedroom night
    show hareka hair_band ribbon smile_mouth at left
    with fade
    show hareka at bounceUp
    "Hareka stands up, closing down her laptop and heading over to me. I look up."
    mc "Oh, good evening."
    show hareka talking
    hareka "Good evening. Well, it's basically night now..."
    show hareka smile_mouth
    "I look out of the window in slight surprise."
    mc "Oh yeah... It is, haha."
    show hareka closed_eyes
    "She chuckles slightly."
    show hareka talking
    hareka "Concentration sure does make time go fast, doesn't it?"
    show hareka smile_mouth
    mc "Yeah it does..."
    show hareka at center with move
    "I put my book away and we both begin getting ready for bed."
    show hareka blinking talking
    hareka "What's the book about, anyways?"
    show hareka smile_mouth
    mc "Oh, peaked your interest?"
    show hareka talking
    hareka "I want to know why you're so concentrated on it."
    show hareka smile_mouth
    mc "Well, for one thing, I just generally enjoy reading. But separate from that, this story in particular is very compelling."
    show hareka talking at bounceUp
    hareka "Oh? How so?"
    show hareka smile_mouth
    "She stops for a moment, glancing at me, her eyes sparkling with curiosity. I smile."
    mc "Well..."
    "I tell her about the plot and the characters, my opinions on them and how that opinion changed further into the story, and my general thoughts on the story structure and execution. "
    "She listens intently to everything I say, asking a couple of questions but otherwise keeping quiet while I rant."
    "When I finish, she seems totally hooked."
    show hareka closed_eyes talking
    hareka "It's been a long time since I've read anything. The way you explained things almost makes me want to try again..."
    show hareka smile_mouth
    mc "What's stopping you? Reading is so fun, and soothes the soul, in my opinion!"
    show hareka talking
    hareka "Well..."
    show hareka sad_mouth
    "She frowns."
    show hareka talking
    hareka "I just don't want to be caught slacking at work, I suppose."
    show hareka sad_mouth
    mc "Hm."
    "I can tell that isn't the only reason, but I won't pressure her if she doesn't want to talk just yet. We're basically strangers, after all."
    show hareka sad_blinking talking
    hareka "I was told off before. This is my job, to monitor you under strict conditions, in order to alleviate any possible threat from you. I can't treat this like leisure time, no matter how slow-paced it is."
    show hareka sad_mouth
    mc "Oh..."
    show hareka talking
    hareka "It's bedtime."
    show hareka sad_mouth
    mc "Oh, right..."
    hide hareka with moveoutleft
    "She swiftly exits to the bathroom. I sigh. I shouldn't feel bad for her..."
    "She's right, actually."
    "She's just my kidnapper, and I'm just her captive."
    show hareka pajamas sad_closed_eyes sad_mouth with moveinleft
    "She soon returns, and we both get into bed."
    mc "Well, goodnight, Hareka."
    show hareka talking
    hareka "Goodnight."
    show hareka sad_mouth
    pause 0.5
    scene black
    with fade
    "{b}Volume 1 - Chapter 1 - Day 2{/b} complete!"
    menu vol1ch1d2_endmenu:
        "Would you like to return to the selection screen, or carry onto the next chronological day?"
        "Return to the selection screen":
            jump volumeselect
        "Carry onto the next day":
            jump vol1ch1d3_start