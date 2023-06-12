import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="gpt-3.5-turbo",
  prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: I'd like to cancel my subscription.\nAI:",
  temperature=1,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)

print(response.choices[0].message.content)