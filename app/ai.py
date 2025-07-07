import os
from openai import OpenAI, OpenAIError, RateLimitError
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_data_with_gpt(data):
    try:
        prompt = f"Analyze this airline data and give insights:\n{data}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a data analyst."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except RateLimitError as e:
        return f"Rate limit or quota error: {e}"
    except OpenAIError as e:
        return f"OpenAI API error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"
