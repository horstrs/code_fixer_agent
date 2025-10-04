import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    
    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    
    flag_verbose = get_verbose_flag(args)
    if flag_verbose == True:
        args.pop()
    user_prompt = " ".join(args)
    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    generate_content(client, messages, flag_verbose)


def generate_content(client, messages, flag_verbose):
    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages
    )
    
    if flag_verbose == True:
        for content in messages:
            if content.role == 'user':
                user_prompt = content.parts[0].text
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)

def get_verbose_flag(args):
    verbose = list(filter(lambda arg: arg == "--verbose", args))
    if verbose:
        return True
    return False

if __name__ == "__main__":
    main()