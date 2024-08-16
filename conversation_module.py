from transformers import pipeline

conversation_pipeline = pipeline("conversational", model="microsoft/DialoGPT-medium")

def converse(query):
    conversation = conversation_pipeline(query)
    return conversation.generated_responses
