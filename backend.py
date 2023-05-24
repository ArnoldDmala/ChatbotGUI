import os
import openai

# Backend

# Please provide your own API key!


class Chatbot:
    def __init__(self):
        openai.api_key = "YOUR API KEY"

# Tokens are words, 'allowing the bot to provide longer answers'
# Meaning bot cannot provide more than 3000 tokens, 4080 is the max
# A lower temp closer to zero will provide more accurate answers, but the answer will be less diverse
# A higher temp sacrifies accuracy, but answers will be more diverse
    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about being empty.")
    print(response)
