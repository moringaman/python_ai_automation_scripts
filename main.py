import os
import requests
import argparse

API_KEY = os.environ.get('OPEN_AI_KEY')
print(API_KEY)

parser = argparse.ArgumentParser()
parser.add_argument('prompt', type=str, help='prompt to send to OPEN AI')
parser.add_argument('--model', type=str, help='model to use')
parser.add_argument('--max_tokens', type=int, help='max tokens to return')
parser.add_argument('--file', type=str, help='file to be created by model')

args = parser.parse_args()

request_headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + API_KEY
}

request_data = {
    "model": "text-davinci-003",
    # request_prompt,
    "prompt": f"write a python script to {args.prompt}, \
            provide only the code no text",
    "max_tokens": 2000,
    "temperature": 0.5,
}

BASE_URL = "https://api.openai.com/v1/completions"
response = requests.post(BASE_URL,
                         headers=request_headers,
                         json=request_data)


def writeFile(file_name="output.py", text="# Script goes here"):
    with open(file_name, "w") as f:
        f.write(text)
        print(f"{file_name} created")


if (response.status_code == 200):
    print(response.json()['choices'][0]['text'])
    script = response.json()['choices'][0]['text']
    if (args.file):
        writeFile(file_name=args.file, text=script)
    else:
        file_name = input("Enter file name: ")
        writeFile(file_name=file_name, text=script)
else:
    print(response.status_code)
