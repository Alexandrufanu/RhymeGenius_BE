import markovify

# # Load the dataset
# from markovify import Text
#
# with open('generator/nlp/poems.txt') as f:
#     text = f.read()
#
# #
# # # Create a Markov Chain model
# # model = markovify.Text(text)
# #
# # # Generate a new poem
# # poem = model.make_sentence()
# #
# # print(poem)
# # Build the model.
# # Text.
# text_model = markovify.Text(text, well_formed=False)
# # text_model.test_sentence_input("test")
#
# # Print five randomly-generated sentences
# for i in range(5):
#     print(text_model.make_sentence(strict=False), )
#
# # Print three randomly-generated sentences of no more than 280 characters
# # for i in range(3):
# #     print(text_model.make_short_sentence(280))


# using the Markov chain generator

# source of the text:
# https://towardsdatascience.com/text-generation-with-markov-chains-an-introduction-to-using-markovify-742e6680dc33
with open('generator/nlp/poems.txt', encoding="utf8") as f:
    sherlock_text = f.read()
    sherlock_model = markovify.Text(sherlock_text)



text_model = sherlock_model
sent = text_model.make_sentence()
print(sent)

# assert len(sent) != 0



