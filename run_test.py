import os
import json
import asyncio
import argparse
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent

load_dotenv()  
def build_prompt(url, steps):
    prompt = f"Go to {url}.\n"
    prompt += "\n".join([f"{i+1}) {step}" for i, step in enumerate(steps)])
    return prompt

async def run_test(task_prompt):
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.0,
        convert_system_message_to_human=True
    )
    agent = Agent(task=task_prompt, llm=llm)
    history = await agent.run()
    try:
        final_output = history.history[-1].result[-1].extracted_content or ""
    except:
        final_output = ""
    return final_output

def validate_output(actual, expected):
    if expected.lower() in actual.lower():
        return "Pass", "Expected text found"
    return "Fail", "Expected text not found"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test-file", "-f", required=True)
    args = parser.parse_args()

    with open(args.test_file) as f:
        data = json.load(f)

    url = data["url"]
    steps = data["test_case"]["steps"]
    expected = data["test_case"]["expected_output"]

    prompt = build_prompt(url, steps)
    actual_output = asyncio.run(run_test(prompt))
    status, notes = validate_output(actual_output, expected)

    result = {
        "status": status,
        "expected": expected,
        "actual": actual_output,
        "notes": notes
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
