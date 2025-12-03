"""Random Joke Generator"""

import random

jokes = {"Why do bees have sticky hair?": "Because they use honeycombs!", 
         "What do you call a bee that can’t make up its mind?": "A maybee", 
         "Where do bees catch the bus?": "At the buzz stop!"}

question, answer = random.choice(list(jokes.items()))

print(f"{question} {answer}")