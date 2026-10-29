# Lead Qualifier

A command-line tool that reads a sales lead's message, asks Google's Gemini model to label it Hot, Warm or Cold, and drafts a short reply. Every result is saved to a log file.

## How it works
1. You type in a lead's message.
2. The script sends it to the Gemini API and asks for a JSON answer with a label and a reply.
3. It prints both and adds them to `leads_log.txt`.

## Setup
Requires Python 3 and a Gemini API key.

```
pip install requests python-dotenv
```

Create a file named `.env` in the project folder with one line:

```
GEMINI_API_KEY=your-key-here
```

## Run
```
python lead_qualifier.py
```

## Notes
- `.env` and `leads_log.txt` are not included in this repository, so your key stays on your machine.
- If the model name in `lead_qualifier.py` is retired or busy, switch to another current Gemini model.