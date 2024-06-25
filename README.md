[![CodeQL](https://github.com/samuel-kuhn/healthcheck/actions/workflows/github-code-scanning/codeql/badge.svg)](https://github.com/samuel-kuhn/healthcheck/actions/workflows/github-code-scanning/codeql)

# Healthcheck

A python script that checks if your websites are running fine and are reachable.

It uses the [Textbelt](https://textbelt.com) API to send reports to your phone via sms.

You can put your API key in the ```settings.py``` file or use the default key ```textbelt``` to send one free SMS per day. 

**Note**: Free SMS sending with textbelt is not available in every country. See https://docs.textbelt.com/supported-countries


## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/samuel-kuhn/healthcheck.git
   cd healthcheck
   ```

2. Install the requests module:
   ```sh
   pip install requests
   ```

3. Create your own `settings.py` file by copying `settings.py.example`:
   ```sh
   cp settings.py.example settings.py
   ```

4. Open `settings.py` and add your API key, phone number, and the list of domains you want to check.
   

## Usage

Run the script:
```sh
python3 healthcheck.py
```


