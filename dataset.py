"""
Shared data for the Mood Machine lab.

This file defines:
  - POSITIVE_WORDS: starter list of positive words
  - NEGATIVE_WORDS: starter list of negative words
  - SAMPLE_POSTS: short example posts for evaluation and training
  - TRUE_LABELS: human labels for each post in SAMPLE_POSTS
"""

# ---------------------------------------------------------------------
# Starter word lists
# ---------------------------------------------------------------------

POSITIVE_WORDS = [
    "happy",
    "great",
    "good",
    "love",
    "excited",
    "awesome",
    "fun",
    "chill",
    "relaxed",
    "amazing",

    # Additional positive words - Added using co-pilot
    "hopeful",
    "proud",
    "best",
    "fire",
    "wicked"
]

NEGATIVE_WORDS = [
    "sad",
    "bad",
    "terrible",
    "awful",
    "angry",
    "upset",
    "tired",
    "stressed",
    "hate",
    "boring",

    # Additional negative words - Added using co-pilot
    "stressed",
    "exhausted",
    "meh"
]

breakers = [
    "I love getting stuck in traffic",
    "This song is sick 🔥",
    "I'm fine 🙂",
    "I'm exhausted but proud of myself",
    "That was wicked fun",
]

# At first wicked was coming up as mixed but was fixed to be positive!

# ---------------------------------------------------------------------
# Starter labeled dataset
# ---------------------------------------------------------------------

# Short example posts written as if they were social media updates or messages.
SAMPLE_POSTS = [
    "I love this class so much",
    "Today was a terrible day",
    "Feeling tired but kind of hopeful",
    "This is fine",
    "So excited for the weekend",
    "I am not happy about this",

    # Additional posts - Added using co-pilot
    "Lowkey stressed about exams but I think I'll be okay",
    "That movie was so bad 💀",
    "I'm fine... just tired I guess",
    "Best day ever 😂",
    "I love getting ignored, it's awesome",
    "Kinda happy kinda confused rn",
    "This weather got me in a good mood :)",
    "ugh everything is just meh today"
]

# Human labels for each post above.
# Allowed labels in the starter:
#   - "positive"
#   - "negative"
#   - "neutral"
#   - "mixed"
TRUE_LABELS = [
    "positive",  # "I love this class so much"
    "negative",  # "Today was a terrible day"
    "mixed",     # "Feeling tired but kind of hopeful"
    "neutral",   # "This is fine"
    "positive",  # "So excited for the weekend"
    "negative",  # "I am not happy about this"

    # Additional labels for the new posts - Added using co-pilot
    "mixed",     # "Lowkey stressed about exams but I think I'll be okay"
    "negative",  # "That movie was so bad 💀"
    "neutral",   # "I'm fine... just tired I guess"
    "positive",  # "Best day ever 😂"
    "negative",  # "I love getting ignored, it's awesome"
    "mixed",     # "Kinda happy kinda confused rn"
    "positive",  # "This weather got me in a good mood :)"
    "neutral"    # "ugh everything is just meh today"
]

len(SAMPLE_POSTS) == len(TRUE_LABELS) # This should always be True - make sure to keep the lists aligned! - Added from Instructions.

# TODO: Add 5-10 more posts and labels.
#
# Requirements:
#   - For every new post you add to SAMPLE_POSTS, you must add one
#     matching label to TRUE_LABELS.
#   - SAMPLE_POSTS and TRUE_LABELS must always have the same length.
#   - Include a variety of language styles, such as:
#       * Slang ("lowkey", "highkey", "no cap")
#       * Emojis (":)", ":(", "🥲", "😂", "💀")
#       * Sarcasm ("I absolutely love getting stuck in traffic")
#       * Ambiguous or mixed feelings
#
# Tips:
#   - Try to create some examples that are hard to label even for you.
#   - Make a note of any examples that you and a friend might disagree on.
#     Those "edge cases" are interesting to inspect for both the rule based
#     and ML models.
#
# Example of how you might extend the lists:
#
# SAMPLE_POSTS.append("Lowkey stressed but kind of proud of myself")
# TRUE_LABELS.append("mixed")
#
# Remember to keep them aligned:
#   len(SAMPLE_POSTS) == len(TRUE_LABELS)
