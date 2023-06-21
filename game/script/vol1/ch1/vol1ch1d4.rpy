label vol1ch1d4_start:
    scene bg bedroom day
    with fade
    "I wake up before Hareka, this time."
    "I stand up, stretching and yawning. Why am I always so stiff in the mornings...?"
    "I grab my clothes and sniff them. I think they'll be okay for another day, but tomorrow they'll definitely need washing..."
    "I get dressed and tidy up my appearance a bit, then make the bed."
    "After that, I grab the book box from the shelf and pull out the book I was reading yesterday, deciding to continue while waiting for Hareka to wake up."
    window hide
    pause 1.0
    "An hour later, Hareka awakens."
    show hareka pajamas closed_eyes neutral_mouth with moveinbottom
    pause 0.15
    show hareka blinking at bounceUp
    pause 0.8
    show hareka talking
    hareka "Good morning..."
    show hareka neutral_mouth
    mc "Good morning! Did you sleep well?"
    show hareka talking
    hareka "I think so."
    show hareka neutral_mouth
    "She sits up and rubs her eyes."
    mc "Good!"
    "She gets up, making her bed, and I put the bookmark back in place in the book, placing it carefully back in the box."
    show hareka talking
    hareka "Would you like breakfast now?"
    show hareka neutral_mouth
    mc "Yes please!"
    show hareka talking
    hareka "Okay then. What would you like today?"
    show hareka neutral_mouth
    menu vol1ch1d4_breakfastchoice:
        "Chocolate cereal":
            $ vol1ch1d4_breakfastchoice_v = "chocolate cereal"
        "Toast":
            $ vol1ch1d4_breakfastchoice_v = "toast"
    hide hareka with moveoutleft
    "She leaves to the kitchen to make my [vol1ch1d4_breakfastchoice_v]."
    "I wait for her return."
    window hide
    pause 1.0
    show hareka pajamas smile_mouth with moveinleft
    pause 0.5
    show hareka talking
    hareka "Here you go."
    show hareka smile_mouth
    "She hands me the [vol1ch1d4_breakfastchoice_v], and I take it gratefully."
    mc "Thanks again!"
    show hareka talking
    hareka "You're welcome."
    show hareka smile_mouth
    pause 0.5
    hide hareka with dissolve
    "While I'm eating, she goes to the corner to get dressed."
    "I don't look, for I know she's a bit squeamish about naked bodies, haha."
    window hide
    pause 1.0
    show hareka hair_band ribbon smile_mouth with dissolve
    "After I finish breakfast, and she's done tidying herself up, we go about our daily activities."
    menu vol1ch1d4_activitychoice:
        "What activity should I do today?"
        "Reading":
            $ vol1ch1d4_activitychoice_v = "reading"
            "I find the book I was reading yesterday, and continue it."
            show hareka at left with move
            "Hareka returns to her desk to continue her work."
        "Playing more games":
            $ vol1ch1d4_activitychoice_v = "board game"
            "We get out the games box, and decide on playing Uno."
            show hareka talking
            hareka "I've never played this game before."
            show hareka smile_mouth
            mc "Oh! I can teach you!"
            "I explain the rules to her."
            show hareka closed_eyes
            "She sighs in relief."
            show hareka talking
            hareka "I thought it would be a complicated game..."
            show hareka smile_mouth
            mc "Oh, no! Uno is pretty simple!"
            show hareka blinking talking
            hareka "Well, let's play then!"
            show hareka smile_mouth
            mc "Yes, let's!"
            "We get started on our first round."