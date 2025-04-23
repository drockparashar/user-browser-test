# 🧠 AI-Powered Browser Test Agent

This project demonstrates a **LLM + Browser automation prototype** that:
- Takes a **URL**, step-by-step **test instructions**, and an **expected output**
- Uses **Google Gemini 1.5 Flash** to interpret the test case
- Executes the test steps using a **self-hosted Browser-Use agent**
- Returns a **Pass/Fail** verdict based on expected vs actual outcome

> Built as part of an AI intern evaluation task.

---

## ✨ Demo Video

[![Watch the demo](https://img.youtube.com/vi/abc123XYZ/0.jpg)](https://www.youtube.com/watch?v=TabCsGJEMiE)

---

## ✅ Features Implemented

- Accepts a structured JSON test case (`url`, `steps[]`, and `expected_output`)
- Builds a natural-language prompt from those steps
- Runs a local **Browser-Use** agent with **Gemini LLM**
- Validates result by checking if the expected output is present

---


