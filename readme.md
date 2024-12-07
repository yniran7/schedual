# This is the Parser for the Schedule project 
still need some work

## Setup
```bash
pip install -r requirements.txt
```

## Run locally (for testing)
```bash
fastapi dev main.py
```
then you can access the documentation at http://127.0.0.1:8000/docs

to run locally you need to run an llm model on your machine, else you can use chatGPT.
What ever way you choose, you need to setup the setting in the config file (src/setting/config.py)


## Plan for the future
- add logger
- error handling
- better responses
- tests
- cleaner code
- publish common models in a lib