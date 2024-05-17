import os

try:
    from g4f.client import Client
except ModuleNotFoundError:
    os.system('pip install g4f')

client = Client()

def respond(prompt):

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": str(prompt)}],
    )

    return response.choices[0].message.content