from together import Together
from dotenv import load_dotenv

load_dotenv()
client = Together()
# client = Together(api_key=TOGETHER_API_KEY)

response = client.chat.completions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    messages=[
      {
        "role": "user",
        "content": "what are the best 5 movies in imdb history?"
      }
    ]
)
print(response.choices[0].message.content)



