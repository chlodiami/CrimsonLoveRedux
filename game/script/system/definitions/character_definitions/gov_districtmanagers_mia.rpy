define mia = Character("Mia", image="mia", who_prefix="District Manager - ", who_color="#b44e4b")

### LAYERED IMAGES ###
image blinking_mia:
    "images/characters/gov/district_managers/mia/layeredimage/assets/opened_eyes_mia.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/characters/gov/district_managers/mia/layeredimage/assets/closed_eyes_mia.png"
    .15
    repeat

image sad_blinking_mia:
    "images/characters/gov/district_managers/mia/layeredimage/assets/sad_opened_eyes_mia.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/characters/gov/district_managers/mia/layeredimage/assets/sad_closed_eyes_mia.png"
    .15
    repeat

layeredimage mia:
    zoom 1.75
    always:
        "images/characters/gov/district_managers/mia/layeredimage/base/mia_base.png"

    group shirts:
        attribute dress default:
            "images/characters/gov/district_managers/mia/layeredimage/base/shirts/dress_mia.png"
    
    group pants:
        attribute socks default:
            "images/characters/gov/district_managers/mia/layeredimage/base/pants/socks_mia.png"
    
    group eyes:
        attribute blinking default:
            "blinking_mia"
        attribute sad_blinking:
            "sad_blinking_mia"
        
        attribute opened_eyes:
            "images/characters/gov/district_managers/mia/layeredimage/assets/opened_eyes_mia.png"
        attribute closed_eyes:
            "images/characters/gov/district_managers/mia/layeredimage/assets/closed_eyes_mia.png"
        
        attribute sad_opened_eyes:
            "images/characters/gov/district_managers/mia/layeredimage/assets/sad_opened_eyes_mia.png"
        attribute sad_closed_eyes:
            "images/characters/gov/district_managers/mia/layeredimage/assets/sad_closed_eyes_mia.png"
    
    group mouth:
        attribute neutral_mouth default:
            "images/characters/gov/district_managers/mia/layeredimage/assets/neutral_mia.png"
        attribute smile_mouth:
            "images/characters/gov/district_managers/mia/layeredimage/assets/smile_closed_mia.png"
        attribute sad_mouth:
            "images/characters/gov/district_managers/mia/layeredimage/assets/sad_closed_mia.png"
        attribute talking:
            "images/characters/gov/district_managers/mia/layeredimage/assets/talking_mia.png"
        attribute pouty_mouth:
            "images/characters/gov/district_managers/mia/layeredimage/assets/pout_mouth.png"
    
    group facial_feature:
        attribute blush:
            "images/characters/gov/district_managers/mia/layeredimage/assets/blush_mia.png"

    group hair_decoration:
        attribute ribbon:
            "images/characters/gov/district_managers/mia/layeredimage/assets/ribbon_mia.png"

image side mia = "images/characters/gov/district_managers/mia/side.png"