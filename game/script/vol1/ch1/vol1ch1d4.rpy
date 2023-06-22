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
    scene bg bedroom day
    if vol1ch1d4_activitychoice_v == "reading":
        show hareka hair_band ribbon smile_mouth at left
    else:
        show hareka hair_band ribbon smile_mouth
    with fade
    "A few hours later, it's lunchtime."
    hide hareka with moveoutleft
    "Hareka leaves to make me my lunch."
    "Then, suddenly, the doorbell rings."
    "I wonder who that could be... Someone from her work, maybe...?"
    "She answers it, but they're too far away for me to hear what they're saying, and the bedroom door is locked, unfortunately. I have to just wait for her to finish."
    window hide
    pause 1.5
    show hareka hair_band ribbon neutral_mouth at left with moveinleft
    "I've been waiting for about 10 minutes before she finally returns."
    mc "Who was that?"
    show hareka talking
    hareka "Oh, it's someone from my work."
    show hareka neutral_mouth
    "Just like I thought."
    mc "What are they doing here?"
    show hareka closed_eyes talking
    hareka "You really are nosey."
    show hareka neutral_mouth
    mc "I'm just curious. I haven't seen anyone other than you for, what, 3 days now?"
    show hareka talking
    hareka "You're on your 4th day."
    show hareka neutral_mouth
    mc "Exactly! Don't you know how much I crave social interaction?"
    show hareka sad_blinking talking
    hareka "Am I not good enough for you?"
    show hareka sad_mouth
    mc "No, I didn't mean it like that!"
    "She sighs."
    show hareka talking
    hareka "Look, they aren't here for chit-chat. It's my maintenance."
    show hareka sad_mouth
    mc "Your... What?"
    show hareka sad_closed_eyes talking
    hareka "Look, just wait here please."
    show hareka sad_mouth
    mc "Huh- What about my monitoring??"
    "Not that I'd mind being left alone for a while, I'm just so confused right now..."
    show hareka sad_blinking talking
    hareka "Oh, you're not being left alone."
    show hareka sad_mouth
    hide hareka with moveoutleft
    pause 0.1
    show mia smile_mouth at left with moveinleft
    "She exits, and as she does, a new figure enters."
    show mia talking
    "???" "Good morning."
    show mia smile_mouth
    mc "Ah, good morning... Who are you?"
    show mia at center with move
    "The person approaches me, holding out their hand."
    "I look at it, confused for a moment."
    show mia closed_eyes neutral_mouth
    "They sigh."
    show mia blinking talking
    "???" "I'm asking for a handshake. Do you not know how to shake my hand?"
    show mia neutral_mouth
    "They comment in a snarky tone."
    mc "Of course I do!"
    "How rude..."
    "I reluctantly shake their hand."
    show mia closed_eyes
    pause 0.3
    show mia smile_mouth
    pause 0.3
    show mia blinking
    pause 0.3
    show mia talking
    mia "My name is Mia. What is your name?"
    show mia smile_mouth
    mc "Do you not know?"
    show mia closed_eyes talking
    mia "I do, of course. However, it is courtesy to introduce yourself at the first meeting, no?"
    show mia smile_mouth
    mc "Huh... Fine. My name is Alex."
    show mia blinking talking
    mia "It's a pleasure to finally meet you, Alex."
    show mia smile_mouth
    mc "...Same..."
    "I'm a lot less enthusiastic than this person."
    "I don't think I've ever met anyone so posh..."
    "The way she acts is one thing, but her appearance tells me straight away she's rich as hell."
    "Mainly her outfit. I'm very familiar with this uniform..."
    "A sneaking feeling of hatred rises inside of me."
    "Those damn District Managers... She must be one, she's wearing their uniform..."
    "I sit down on the bed, grabbing my book from yesterday, and begin reading. Mainly as a distraction from her watchful gaze."
    "I hoped she'd leave me alone, but..."
    show mia talking
    mia "What book are you reading?"
    show mia smile_mouth
    "I look up with a slightly annoyed expression."
    mc "Why do you care?"
    show mia talking
    mia "Awe, there's no need to be so fiesty dear."
    show mia smile_mouth
    "I scoff. She really is just like the others."
    mc "Shut up. I don't associate myself with your kind."
    show mia closed_eyes at bounceUp
    "She giggles, which makes me more ticked off. She really thinks my anger is funny..."
    show mia blinking talking
    mia "Well then, you'd better stop becoming close to my dear Hareka, hm?"
    show mia smile_mouth
    mc "What do you mean...?"
    show mia closed_eyes neutral_mouth
    pause 0.6
    show mia talking
    mia "God you're freaking slow... Let me say it so you understand then."
    show mia blinking
    mia "She works for me! I'm her manager!"
    show mia smile_mouth
    ".{w} .{w} ."
    "No way. This... No way."
    mc "Oh... So... She's actually a government worker...?"
    show mia talking
    mia "Of course! Why would she lie about that?"
    show mia smile_mouth
    mc "I thought she was using it as an excuse for kidnapping me..."
    show mia closed_eyes talking
    mia "Huhu. You're so funny."
    show mia smile_mouth
    "I clench my fists."
    mc "{i}Shut. Up.{/i}"
    show mia blinking talking
    mia "Okay~!"
    show mia smile_mouth
    hide mia with dissolve
    "Thank goodness, she actually listened."
    "I try to continue reading, but I can't concentrate at all now. I can't stop thinking about what she said."
    "Hareka's really... not lying..."
    "..."
    "But at least Hareka isn't a rich brat like all the District Managers seem to be. Mia is no exception to that."
    scene black
    with fade
    "Everything around me was on fire. Everything was burning. Everything was destroyed."
    "No one died, luckily, but the damage was severe."
    "Who started this war? Why was my little district targeted? We did nothing to deserve this!"
    "It's... their fault..."
    "If the sparkly people didn't get involved..."
    "I thought they were sparkly. I aspired to be like them one day."
    "Oh, anything, I'd have done anything, to be a District Manager... At the very top of the local council chain... The money, the splendour..."
    "{b}{i}I realise now, they were anything but idols.{/i}{/b}"
    window hide
    pause 1.5
    hareka "Alex?"
    scene bg bedroom day
    show hareka hair_band ribbon sad_mouth sad_blinking
    with hpunch
    "I open my eyes in surprise."
    mc "Did I fall asleep??"
    show hareka talking
    hareka "It seems so. Are you alright?"
    show hareka sad_mouth
    mc "Yeah, I'm fine..."
    show hareka blinking smile_mouth
    pause 0.3
    show hareka talking
    hareka "Good. Mia's gone now, by the way."
    show hareka smile_mouth
    mc "Oh..."
    show hareka talking
    hareka "We didn't want to wake you, but she told me to say goodbye to you for her."
    show hareka smile_mouth
    mc "Oh. Thanks..."
    "I stand up, stretching out."
    show hareka talking
    hareka "Would you like your lunch now? I made it earlier but didn't have chance to give it to you."
    show hareka smile_mouth
    mc "Yes please..."
    show hareka talking
    hareka "Alright."
    show hareka smile_mouth
    hide hareka with moveoutleft
    "Hareka leaves to fetch my food."
    "I sit back down, putting my head in my hands."
    "I do remember the dream..."
    "It was horrible..."
    "I shake my head. I need to forget about it, for now. I'll talk to Hareka later, about her job."
    show hareka hair_band ribbon smile_mouth with moveinleft
    "She returns a few minutes later with a tuna and sweetcorn sandwich and water."
    mc "Thanks."
    show hareka talking
    hareka "You're welcome."
    show hareka smile_mouth
    "I eat it quietly."
    show hareka sad_closed_eyes
    pause 0.3
    show hareka sad_mouth
    pause 0.3
    "Hareka frowns."
    show hareka sad_blinking talking
    hareka "Are you sure you're alright? You're oddly quiet."
    show hareka sad_mouth
    mc "Yeah, I'm fine... Just tired."
    show hareka talking
    hareka "Aw, okay. If you need anything, just ask, yeah?"
    show hareka smile_mouth
    mc "Okay... Thanks..."
    show hareka talking
    hareka "You're welcome. I'm gonna do some more work for a bit."
    show hareka smile_mouth
    mc "Alright. I'll read more when I finish my food."
    show hareka blinking talking
    hareka "Okay!"
    show hareka smile_mouth
    pause 0.3
    show hareka at left with move
    "She moves to her desk and boots up the laptop."
    "I find myself wondering what she does on there, but I'm too scared to ask, for now."
    "I finish my lunch, bin the plate, and then grab the book, finally calm enough to concentrate on reading."
    scene bg bedroom evening
    show hareka hair_band ribbon smile_mouth at left
    with fade
    "A few hours pass. I'd finished the book, and started a new one in that time."
    show hareka at bounceUp
    "Hareka stands up."
    show hareka talking
    hareka "Would you like dinner now?"
    show hareka smile_mouth
    mc "Yes please..."
    hide hareka with moveoutleft
    "She leaves to make my dinner. I continue reading while waiting for her to return."
    window hide
    pause 1.0
    show hareka hair_band ribbon smile_mouth with moveinleft
    "She returns soon, with a vegetable soup."
    show hareka talking
    hareka "I made it myself a few days ago. It should still be pretty fresh though, since I kept it sealed in the fridge."
    show hareka smile_mouth
    mc "Thank you!"
    show hareka talking
    hareka "You're welcome. Enjoy."
    show hareka smile_mouth at left with move
    "I eat the soup. It's delicious, as is all of her cooking."
    window hide
    pause 1.0
    "When I'm done, I turn to her."
    mc "Hey, I think I'm gonna go to bed a bit earlier tonight. I'm... really tired..."
    show hareka talking
    hareka "Oh? Okay then. I'll try to be quiet with my work."
    show hareka smile_mouth
    mc "Thank you..."
    "She focuses on her laptop while I get changed and ready for bed."
    mc "Goodnight, Hareka."
    show hareka talking
    hareka "Goodnight. I hope you feel better tomorrow."
    show hareka smile_mouth
    mc "Thanks..."
    "I climb into bed, sinking into the warm sheets."
    "I close my eyes, succumbing to sleepiness."
    scene black
    with fade
    "{b}Volume 1 - Chapter 1 - Day 4{/b} complete!"
    menu vol1ch1d4_endmenu:
        "Would you like to return to the selection screen, or carry onto the next chronological day?"
        "Return to the selection screen":
            jump volumeselect
        "Carry onto the next day":
            jump vol1ch1d5_start