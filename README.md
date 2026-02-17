# HR Email Automation Script

This Python script automates sending personalized job application emails with your resume attached to a list of HR contacts stored in a CSV file.

## Features
- Reads HR contacts from a CSV file
- Sends personalized emails with subject and body
- Attaches your resume
- Uses Gmail SMTP with environment variables

## Requirements
- Python 3.x
- Libraries:
  - pandas
  - python-dotenv

Install dependencies using:
```bash
pip install pandas python-dotenv


# HR Email Automation Script

This Python script automates sending personalized job application emails (with resume attachments) to HR contacts listed in a CSV.

## Quickstart (macOS)

Prerequisites
- Python 3 installed. Check with:

```bash
python3 --version
```

If you don't have Python 3, install via Homebrew or from python.org:

```bash
brew install python
```

Recommended (virtual environment)

```bash
cd email-automation-script
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install pandas python-dotenv
```

Alternative (system / user install)

```bash
python3 -m pip install --user pandas python-dotenv
# or
pip3 install --user pandas python-dotenv
```

If you see a warning like "scripts ... installed in '/Users/<you>/Library/Python/3.x/bin' which is not on PATH", add that folder to your PATH:

```bash
export PATH="$HOME/Library/Python/3.9/bin:$PATH"
# (adjust the 3.9 to your Python minor version)
```

Running the script

```bash
# activate venv if you created it
source venv/bin/activate
python send_emails.py
```

Environment variables
- The project uses `python-dotenv`. Create a `.env` file in the project root with the SMTP credentials and any configuration `send_emails.py` expects (for example SMTP user, password, host, port). See `send_emails.py` for exact variable names.

Troubleshooting
- If `pip` is not found, use `pip3` or `python3 -m pip`:

```bash
python3 -m pip install pandas python-dotenv
```

- To upgrade pip (recommended inside venv):

```bash
python -m pip install --upgrade pip
```

- If you run into permission errors, prefer using `--user` or a virtual environment.

If something still fails, paste the terminal output and I will help debug.

Happy coding!
