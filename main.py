# this is a twilight cyoa game. you are going to play as a twilight fan in 2008 in highschool
# the choices you make determine your ending and there are doing to be three endings maybe

import pygame

STORY = {
    "start": {
        "text": (
            "Today is November 24th, 2008. You are about to go to school "
            "after watching Twilight on opening night. You're nervous. "
            "You have to choose Team Edward or Team Jacob..."
        ),
        "choices": [
            ("Team Edward", "edward_clothes"),
            ("Team Jacob",  "jacob_clothes"),
        ],
    },

    "edward_clothes": {
        "text": (
            "You choose Team Edward. Bella and him are meant to be together."
            "What do you wear to school?"
        ),
        "choices": [
            ("Bella inspired outfit", "bella_outfit"),
            ("Team Edward shirt", "edward_shirt"),
        ],
    },

    "bella_outfit": {
        "text": (
            "You put on a lowrise skinny jeans, beat up converses and a sweater."
            "You're so mysterious, just like Bella...",
        ),
        "choices": [
            ("Go to school", "bella_school"),
        ],
    },

    "edward_shirt": {
        "text": (
            "You put on your Team Edward shirt."
            "Team Edward for life...",
        ),
        "choices": [
            ("Head to school", "edward_school"),
        ],
    },
    
    "bella_school": {
        "text": (
            "You look so mysterious and brooding, just like Bella. You get a few compliments but also some weird looks."
            "You have your headphones in and walk striaght to class while listening to the new soundtrack."
            "There is nothing that shows your passion for this movie."
            "You just look emo..."
        ),
        "choices": [
            ("Continue", "bella_continued"),
        ],
    },

    "edward_shirt": {
        "text": (
            "You wear your Team Edward shirt."
            "He's so much better than Jacob"
        ),
        "choices": [
            ("Go to school", "edward_school"),
        ],
    },

    "edward_school": {
        "text": (
            "You go to school wearing your Team Edward shirt."
            "Some people are looking at you weird..."
            "A group of girls come up to you and start talking about the movie."
            "'I LOVE YOUR SHIRT. WHERE DID YOU GET IT?'"
            "'HAVE YOU LISTENED TO THE SOUNDTRACK???'"
        ),
        "choices": [
            ("Continue talking to them", "edward_talk"),
        ],
    },
    
    "edward_talk": {
        "text": (
            "You continue to talk about the movie and your love for edward then head to class"
            "You take your seat and have a weird feeling..."
            "Someone is staring at you..."
            "You look up and see a girl wearing a Team Jacob shirt judging you..."
        ),
        "choices": [
            ("Ignore her and continue with class", "edward_ignoring"),
            ("Stare at her back", "edward_staring"),
        ],
    },

    "edward_ignoring": {
        "text": (
            "You ignore her and continue with class."
            "You feel her eyes staring at you the whole time."
            "You feel like you need to do something"
        ),
        "choices": [
            ("Go up to her", "edward_confronting"),
            ("Ignore her and continue with class", "edward_ignoring2"),
        ],
    },

    "edward_staring": {
        "text": (
            "You stare at her back."
            "She comes up to you and says 'I see you like Twilight'"
        ),
        "choices": [
            ("I love the movie.", "edward_confronting2"),
            ("I love Edward, he's perfect for Bella", "edward_confronting3"),
        ],
    },

    "edward_confronting": {
        "text": (
            "'Hello?'"
            "'Why do you keep staring at me???'"
            "She looks at you with a disgusted look. 'Jacob is way much better.'"
            "You stand there jawdropped."
        ),
        "choices": [
            ("Continue", "edward_confronting2"),
        ],