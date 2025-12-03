import spacy

nlp = spacy.load('en_core_web_sm')

gardenpathSentences = ["Mary gave the child a Band-Aid.",
                       "That Jill is never here hurts.", 
                       "The cotton clothing is made of grows in Mississippi.",
                       "The panda eats shoots and leaves.",
                       "The family watches afternoon repeats."]

# Track unique entity labels
seen_labels = set()

print("=== Named Entity Recognition (NER) Results ===\n")

for i, sentence in enumerate(gardenpathSentences, 1):
    print(f"Sentence {i}: {sentence}")
    
    # Tokenise and perform NER
    doc = nlp(sentence)
    
    tokens = [token.text for token in doc]
    print(f"Tokens: {tokens}")
    
    # Extract and display entities
    if doc.ents:
        print("Named entities found:")
        for ent in doc.ents:
            print(f" '{ent.text}': {ent.label_}")
            # Add label for explanation
            seen_labels.add(ent.label_)
    else:
        print("No named entities found.")
    
    print() 

print("=== Entity Label Explanations ===")
if seen_labels:
    for label in sorted(seen_labels):
        explanation = spacy.explain(label)
        print(f"{label}: {explanation}")
else:
    print("No named entities were found in sentences.")


## What was the entity and its explanation that you looked up?

# From Sentence 1, 'Mary': PERSON, 'People, including fictional'.
# From Sentence 5, 'afternoon': TIME, 'Times smaller than a day'.

## Did the entity make sense in terms of the word associated with it?

# The word 'afternoon' is labelled as 'Times smaller than a day' and
# 'Mary' is labelled as a 'person', which are both correct descriptions
# of these words.


## References

# Geeks4Geeks. (2025). Tokenization Using Spacy.
# https://www.geeksforgeeks.org/nlp/tokenization-using-spacy-library

# HyperionDev. (2025). Natural Language Processing. Course materials.
# Private repository, GitHub.

# Montani, I. (2021). spaCy Cheat Sheet: Advanced NLP in Python. DataCamp
# https://www.datacamp.com/cheat-sheet/spacy-cheat-sheet-advanced-nlp-in-python