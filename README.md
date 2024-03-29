# GPT-3 Quote Semantics

Repository for utilizing GPT-3 to get quote semantics based on queries.

You will need Python 3.9+ installed.

## Install
```bash
pip3 install -r requirements.txt

python3 -m spacy download en_core_web_lg
```

## Setup
```bash
export OPENAI_API_KEY="<your api key>"
```

## Test
```bash
# run unit tests
ward
```

## Usage
```bash
python3 main.py
```

## Auto Train Config
See ---> [Example File](https://github.com/schnetzlerjoe/gpquote/blob/master/tests/test.json)

Auto Training takes in various promps (and configuration settings) from a JSON file and then tests against the text and query wanted. The `<file_name>.json` format is:

```json
{
    "model": "text-davinci-002",
    "temperature": 0,
    "max_tokens": 100,
    "top_p": 1.0,
    "best_of": 1,
    "frequency_penalty": 0.0,
    "presence_penalty": 2.0,
    "prompts": [
        "<promp_text>"
    ],
    "text": "<text>",
    "query": "<query question>"
}
```