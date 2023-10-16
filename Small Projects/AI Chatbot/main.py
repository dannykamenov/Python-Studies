import openai

openai.api_key = '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'

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        message=[{'role': 'user', 'content': prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == '__main__':
    while True:
        user_input = input('You: ')
        if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
            break
        response = chat_with_gpt(user_input)
        print('ChatBot:', response)