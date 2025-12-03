# NLP – Semantic Similarity Practical Task 1

import spacy

# Load the small- and medium-sized English model
nlp_sm = spacy.load("en_core_web_sm")
nlp_md = spacy.load("en_core_web_md")

# Print similarity scores based on medium-sized model
tokens_1 = nlp_md("cat apple monkey banana ")
tokens_2 = nlp_md("banana apricot simple easy")

print("SEMANTIC COMPARISONS:")

for token1 in tokens_1:
    for token2 in tokens_1:
        print(
            f"'{token1.text}' and '{token2.text}': {token1.similarity(token2)}"
        )

for token1 in tokens_2:
    for token2 in tokens_2:
        print(
            f"For '{token1.text}' and '{token2.text}': {token1.similarity(token2)}"
        )

## Write a note on what you noticed about the similarities between “cat”, “monkey”, and 
## “banana”, and think of an example of your own.

    # The semantic similarity beween 'cat' and 'monkey' is the highest at ~0.395.
    # This is likely because the model sees these words as more related conceptually,
    # as they can be grouped together as animals, mammals, etc. The word 'monkey'
    # is also conceptually related to 'banana' in popular media because monkeys are
    # known to like this fruit. So, the similarity score is also high at ~0.374.
    # However, the words 'cat' and 'banana' have a weak semantic link and so the
    # model shows a low score for these words (~0.233).

    # For my own example, I tested 'banana' and 'apricot' together and they have
    # the strongest relationship of the words tests (~0.558). The synonyms 'simple'
    # and 'easy' are also strongly linked (0.446), although less so than the two
    # types of fruit. Words like 'banana' and 'simple' are of course weakly linked
    # in semantic terms (~0.133).


## Run the example file with the simpler language model en_core_web_sm.

# Process the words with the small NLP model
word1 = nlp_sm("cat")
word2 = nlp_sm("monkey")
word3 = nlp_sm("banana")

# Print the similarity scores
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens_3 = nlp_sm("cat apple monkey banana ")

for token1 in tokens_3:
    for token2 in tokens_3:
        print(
            f"'{token1.text}' and '{token2.text}': {token1.similarity(token2)}"
        )

sentence_to_compare = "Why is my cat on the car"

sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I've lost my car in my car",
    "I'd like my boat back",
    "I will name my dog Diana",
]

model_sentence = nlp_sm(sentence_to_compare)

for sentence in sentences:
    similarity = nlp_sm(sentence).similarity(model_sentence)
    print(sentence + "-" + str(similarity))

# Below we have two lists: one containing complaints submitted
# to a company, and another of recipes found online.
# We want to establish how spaCy's model can identify
# similarities or dissimilarities between complaints and recipes.

# Below is a list of six complaints.
complaints = [
    "We bought a house in  CA. Our mortgage was handled by a "
    "company called ki. Soon after the mortgage was sold to ABC. "
    "Shortly after that XYZ took over the mortgage. The other day "
    "we got a notice not to send our payment to them but to loi "
    "instead. This is all so frustrating and wreaks of the  "
    "mortgage nightmare.",
    "I got approved for a loan to buy a house I have submitted "
    "everything I need to for them I paid for the inspection and "
    "paid good faith check after all of that they said I did not "
    "get approved for the loan to cancel my contract because "
    "they do not want to wait for the down payments assistant "
    "said that the Sellers do not want to wait that long I feel "
    "like they are getting over on me I feel that they should "
    "have told me that I did not get approved before I spent my "
    "money and picked out a house Carrington mortgage in Ohio ",
    "As per the correspondence, I received from : The University  "
    "This is to inform you that I have recently pulled my credit "
    "report and noticed that there is a collection listing from "
    "The University  on my credit report. I WAS never notified of "
    "this collection action or that I owed the debt. This letter "
    "is to inform you that I would like a verification of the "
    "debt and juilo ability to collect this money from me.",
    "I am writing to dispute the follow information in my file."
    "ON BOTH TransUnion & . for {$15000.00}. I have contacted "
    "this agency to advise to STOP CALLING ME this case was "
    "dismissed in court  2014. Please see the attached document "
    "from  County State Court. Thanking you in advanced regarding "
    "this matter.",
    "I have not had a XXXX phone since early 2007. I have tried "
    "to resolve my bill in the past but it keeps reposting an old "
    "bill. I have no way to provide financial info from 8 years "
    "ago and they know that so they want me to prove it to them "
    "but I have no way to do that. Is there anyway to get  to "
    "find out how old it is.",
    "I posted dated a check and mailed it for 2015 for my "
    "mortgage payment as my mortgage company will only take "
    "online payments if all the late charges are paid at once "
    "( also illegal ), and the check was cashed on 2015 which "
    "cost me over {$70.00} in over draft fees with my bank.",
]

# We will now compare the similarity of the complaints to
# ascertain if spaCy's similarity model is able to distinguish
# between these long pieces of text.

print("-------------Complaints similarity---------------")
for token in complaints:
    token = nlp_sm(token)
    for token_ in complaints:
        token_ = nlp_sm(token_)
        print(token.similarity(token_))

# Below is a list of six recipe instructions.
recipes = [
    "Bake in the preheated oven, stirring every 20 minutes, "
    "until sugar mixture has baked and caramelized onto popcorn "
    "and cashews, about 1 hour. Spread cashew caramel corn onto "
    "a parchment paper-lined baking sheet to cool. If desired, "
    "form into balls while still warm.",
    "Combine brown sugar, corn syrup, butter, salt, and cream "
    "of tartar in a large saucepan. Bring to a boil, stirring "
    "constantly, until a candy thermometer inserted into the "
    "middle of the syrup, not touching the bottom, reads 260 "
    "degrees F (127 degrees C), 6 to 8 minutes.",
    "Lift marshmallow fudge out of the pan by the edges of the "
    "foil and place on a large cutting board. Dip a large knife "
    "in the remaining confectioners' sugar and slice fudge into "
    "1 1/2-inch squares, continually dipping knife in the sugar "
    "after each slice.",
    "Melt butter in a medium saucepan over medium heat; stir in "
    "condensed milk. Pour in chocolate chips; cook and stir "
    "until melted, 5 to 10 minutes.",
    "Lightly grease a cookie sheet. Deflate the dough and turn "
    "it out onto a lightly floured surface. Roll the marzipan "
    "into a rope and place it in the center of the dough. Fold "
    "the dough over to cover it; pinch the seams together to "
    "seal. Place the loaf, seam side down, on the prepared "
    "baking sheet. Cover with a damp cloth and let rise until "
    "doubled in volume, about 40 minutes. Meanwhile, preheat "
    "oven to 350 degrees F (175 degrees C)",
    "In a large bowl, cream together the butter, brown sugar, "
    "and white sugar. Beat in the instant pudding mix until "
    "blended. Stir in the eggs and vanilla. Blend in the flour "
    "mixture. Finally, stir in the chocolate chips and nuts. "
    "Drop cookies by rounded spoonfuls onto ungreased cookie "
    "sheets.",
]

# We will now compare the similarity of the recipes to ascertain
# how well spaCy's similarity model is able to distinguish
# between them.

print("-------------Recipes similarity---------------")
for token in recipes:
    token = nlp_sm(token)
    for token_ in recipes:
        token_ = nlp_sm(token_)
        print(token.similarity(token_))

# Now we want to obtain the extent of similarity between the
# complaints and the recipes. we will loop through every recipe
# instruction and compare it with a complaint.

print("-------------Recipes similarity---------------")

for token in recipes:
    token = nlp_sm(token)
    for token_ in complaints:
        token_ = nlp_sm(token_)
        print(token.similarity(token_))


## Write a note on what you notice may be different between the
## small- and medium-sized model.

    # A warning is printed before the results are displayed. The
    # message says the model "has no word vectors loaded" and "the result
    # of the Doc.similarity method will be based on the tagger, parser and
    # NER, which may not give useful similarity judgements". This is
    # because it is the small model applied here. The warning recommends
    # using a larger model instead. The small model will return a score
    # based on context from the text parsed instead of a semantic similarity
    # score based on a more extensive, pre-trained language model that makes
    # use of high-dimensional vector space.

    # The results show that the small model finds "cat" and "apple" to be
    # very similar, with a score of ~0.533. This is not a measure of semantics
    # anymore but is related to how close the words are to each other in the
    # parsed or word-level context in the sample text. When run against the
    # larger model based on vectors, the similarity score for these same words
    # was much lower, at ~0.233. This shows what each model is capable of and
    # both options have their uses to check for semantic meaning or word
    # nearness in context.


## References

# spaCy. (2025). English: Available trained pipelines for English.
# https://spacy.io/models/en

# spaCy. (2025). spaCy 101: Everything you need to know.
# https://spacy.io/usage/spacy-101

# spaCy. (2025). Vectors. https://spacy.io/api/vectors