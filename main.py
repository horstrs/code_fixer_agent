import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_functions import call_function
from config import MAX_TOOL_CALLS
from config import SYSTEM_PROMPT


def main():
    load_dotenv()
    
    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)
    if verbose:
        print(f"User prompt: {user_prompt}\n")
    
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)
    


def generate_content(client, initial_message, verbose):
    
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )
    messages = initial_message

    for i in range(0,MAX_TOOL_CALLS):
        if verbose:
            print(f"This is iteration #{i}")
        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=SYSTEM_PROMPT
            ),
        )
        if not response.candidates:
            break

        for candidate in response.candidates:
            messages.append(candidate.content)

        if verbose == True:
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        try:
            if response.function_calls:
                for function_call_part in response.function_calls:
                    function_call_result = call_function(function_call_part, verbose)
                    if not function_call_result.parts[0].function_response.response:
                        raise Exception(f"Error: no function response returned from {function_call_part.name}")
                    new_message = types.Content(role="user", parts=function_call_result.parts)
                    messages.append[new_message]
                    if verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
            elif response.text:
                print("Response:")
                print(response.text)
            else:
                raise Exception(f"Error: no response returned from LLM")
        except Exception as e:
            print(e)
    

if __name__ == "__main__":
    main()