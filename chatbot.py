from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class ChatbotAI:
    def __init__(self):
        self.chatbot = ChatBot('Zap AI')
        trainer = ListTrainer(self.chatbot)
        trainer.train([
            "Hi",
            "Hello!",
            "How are you?",
            "I'm good, thank you!",
            "Do you need something?"
            "What can I do for you Master?"   
            # Add more training data here
        ])

    def respond(self, user_input):
        return self.chatbot.get_response(user_input).text
