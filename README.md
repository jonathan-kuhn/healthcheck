# healthcheck

A python script that checks if your websites are running fine and are reachable.

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
