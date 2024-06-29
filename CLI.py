#pip install google-generativeai


import os

import google.generativeai as genai

genai.configure(api_key="Enter API-Key")

generation_config = {
  "temperature": 1,
  "top_p": 0.90,
  "top_k": 64,
  "max_output_tokens": 8190,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)
print("Hii,I am your Math Solving bot")
choice="True"
while choice:
	Ques=input("enter your question::")+"if given question is not math question then simply say This is not math question.Please enter a math question. not more then it else solve and explain."
	response = chat_session.send_message(Ques)
	print(response.text)
	try:
		choice=input("Press ctrl+c to exit or Spacebar to use again::")
	except:
		break
	
print("\nCome Again")
