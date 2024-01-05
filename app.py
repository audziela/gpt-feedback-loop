%%writefile app.py
import streamlit as st
import openai as ai

API_ENDPOINT = "https://api.openai.com/v1/chat/completions"
## Use your own API key: https://platform.openai.com/account/api-keys

try:
  ai.api_key = "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"
except:
  st.text('Add API Key')

def chatgpt_call(prompt, model, temperature):
  completion = ai.ChatCompletion.create(
    model=model,
    messages=[{"role": "user", "content": prompt}],
    temperature=temperature
  )
  return completion['choices'][0]['message']['content']

st.header('Bias Eliminator')
topic = st.text_input('Topic you want to learn')
model = 'gpt-3.5-turbo' # "gpt-3.5-turbo"
temperature = 1
st.sidebar.markdown("This app uses OpenAI's generative AI. Please use it carefully and check any output as it could be biased or wrong. ")

prompt = f"{topic}"

explanation = chatgpt_call(prompt, model, temperature)
check = chatgpt_call("Analyze the bias of this response and explain how it could be less biased: "+str(explanation), model, 0)

generate = st.button('Generate Response')

if generate:
  st.markdown(explanation)
  st.markdown("---------------")
  st.markdown(check)
