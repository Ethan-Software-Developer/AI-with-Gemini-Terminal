import google.generativeai as genai

GOOGLE_API_KEY = 'AIzaSyA198yswgB5isnsJGoJz5RMaQDl0dPxsEM'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.0-pro-latest')
convo = model.start_chat()

while True:
    user_input = input('Gemini Prompt: ')
    convo.send_message(user_input)
    print(convo.last.text)
