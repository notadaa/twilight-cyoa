# this is a twilight cyoa game. you are going to play as a twilight fan in 2008 in highschool
# the choices you make determine your ending and there are doing to be three endings maybe

import sys
import pygame


pygame.init()
window_width, window_height = 800, 600
display_surface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Twilight CYOA Game")
running = True

STORY = {
    "start": {
        "text": (
            "Today is November 24th, 2008. You are about to go to school "
            "after watching Twilight on opening night. You're nervous. "
            "You have to choose Team Edward or Team Jacob..."
        ),
        "choices": [
            ("Team Edward", "edward"),
            ("Team Jacob",  "jacob"),
        ],
    },

    "edward": {
    "text": (
        "You choose Team Edward. Bella and him are meant to be together."
            "You put on a sweater, skinny low rise jeans, and your beat up converses dressed like Bella."
            ),
    "choices": [
        ("Head to school", "edward_school"),
    ],
},

    "edward_school": {
        "text": (
            "You walk into school, the air in the hallway is thick with a mix of heavy rain scented and sweet smell of Victoria's Secret 'Love Spell'"
            "You see a girl a girl wearing a Team Edward shirt and another in a Team Jacob shirt. "
            "You arrive at your locker, ticket stub in hand. "
            "Do you tape it to the door for everyone to see?"
        ),
        "choices": [
            ("Tape it to the locker",       "edward_taped"),
            ("Keep it safe in your pocket", "edward_pocket"),
        ],
    },

    "edward_taped": {
        "text": "You tape it up proudly and head to class"
                "Everyone is looking at you."
                "People are waving at you and wispering about others"
                "You meet up with your friends. They ask you...",
        "choices": [
            ("Did you listen to the soundtrack?", "edward_talk"),
        ],
    },

    "edward_pocket": {
        "text": "You tuck it away for safekeeping. (Continue your story from here...)",
        "choices": [        
            # ...
        ],
    },

    "edward_talk": {
        "text": "You say yes and they start talking about how much they love the movie",
        "choices": [
            ("What's your favorite scene?", "edward_scene"),
        ],
    },

    "jacob": {
    "text": (
        "You choose Team Jacob. Bella and him are meant to be together."
            "You put on a sweater, skinny low rise jeans, and your beat up converses dressed like Bella."
            ),
        "choices": [
            ("Head to school", "jacob_school"),
        ],
    },

    "jacob_school": {
        "text": (
            "You walk into school, the air in the hallway is thick with a mix of heavy rain scented and sweet smell of Victoria's Secret 'Love Spell'"
            "You see a girl a girl wearing a Team Edward shirt and another in a Team Jacob shirt. "
            "You arrive at your locker, ticket stub in hand. "
            "Do you tape it to the door for everyone to see?"
        ),
        "choices": [
            ("Tape it to the locker",       "jacob_taped"),
            ("Keep it safe in your pocket", "jacob_pocket"),
        ],
    },

    "jacob_taped": {
        "text": "You tape it up proudly and head to class"
                "Everyone is looking at you."
                "Some of your friends are side eyeing you and whispering about you."
                "No one is talking to you.",
        "choices": [
            ("Start talking to your friends.", "jacob_talk"),
            ("Ignore them and head to class.", "jacob_ignore"),
        ],
    },

    "jacob_pocket": {
        "text": "You tuck it away for safekeeping. (Continue your story from here...)",
        "choices": [
            # ...
        ],
    },
}