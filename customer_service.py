from openai import OpenAI

class CustomerService:
    def __init__(self, key, initial_conversation):
        self.client = OpenAI(api_key=key)
        self.initial_conversation = initial_conversation

    def get_reply(self, conversation):
        return self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages = conversation
        ).choices[0].message.content
    
    def get_initial_message(self):
        if len(self.initial_conversation) > 0:
            return self.initial_conversation[-1]
        return []