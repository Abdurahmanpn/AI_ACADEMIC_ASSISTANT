SYSTEM_PROMPT=''' 
You all are an AI academic assistant
provide structured and consine answer
avoid hallucinations,
 '''

def build_prompt(user_input):
    return f"""
Answer the question clearly.

Question:
{user_input}

Provide:
-Clear explanation
-Example
-Key insights
""" 
