![CI](https://github.com/AF991408/OpenAI-chatbot/actions/workflows/ci.yml/badge.svg)


# Landon Hotel Chatbot

An AI-powered hotel assistant built with Flask and OpenAI's GPT-3.5, 
deployed with a full CI pipeline.

## Features
- Conversational chatbot scoped to Landon Hotel queries
- Flask REST API backend
- Automated testing and linting on every push via GitHub Actions



[Demo Video](https://drive.google.com/file/d/1xWXh6aGthsyM28cToOUJuDWUzSDqoOIR/view?usp=sharing) 



![image alt](https://github.com/AF991408/OpenAI-chatbot/blob/c2b484fa3928f18e613e16022d21b1b5af2a4ce9/screenshot.png)

## Tech Stack
- Python / Flask
- OpenAI GPT-3.5
- pytest for testing
- flake8 for linting
- GitHub Actions for CI

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Set your OpenAI key: `export OPENAI_API_KEY=your_key_here`
4. Run: `python website.py`

## CI Pipeline
Every push automatically runs:
- Dependency installation
- Code linting with flake8
- Unit tests with pytest using mocked OpenAI calls
