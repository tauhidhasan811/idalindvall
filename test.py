import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic()

try:
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",  # ← from your available models list
        max_tokens=1024,
        messages=[
            {"role": "user", "content": "Hello, Claude! Are you working?"}
        ]
    )
    print("Success! Response from Claude:")
    print(message.content[0].text)

except anthropic.AuthenticationError:
    print("Error: Your API key is invalid.")
except anthropic.RateLimitError:
    print("Error: You have hit your rate limit.")
except Exception as e:
    print(f"An error occurred: {e}")