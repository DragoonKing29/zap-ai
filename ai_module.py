from transformers import pipeline

nlp_pipeline = pipeline("text-generation", model="gpt-2")

def ai_response(query):
    generated_text = nlp_pipeline(query, max_length=50, num_return_sequences=1)
    return generated_text[0]['generated_text']
