# GPT-3 Quote Semantics

Repository for utilizing GPT-3 to get quote semantics based on queries.

## Install
```bash
pip3 install -r requirements.txt
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
Auto Training takes in various promps from a file and then tests against the text and query wanted. The `<file_name>.json` format is:

```json
{
    "prompts": [
        "Two households, both alike in dignity, In fair Verona, where we lay our scene, From ancient grudge break to new mutiny, Where civil blood makes civil hands unclean. From forth the fatal loins of these two foes A pair of star-cross’d lovers take their life; Whose misadventured piteous overthrows Do with their death bury their parents’ strife. The fearful passage of their death-mark’d love, And the continuance of their parents’ rage, Which, but their children’s end, nought could remove, Is now the two hours’ traffic of our stage; The which if you with patient ears attend, What here shall miss, our toil shall strive to mend.\n\nQuery: What city does this take place in?\nQuote: Two households, both alike in dignity, In fair Verona, where we lay our scene\n\nQuery: How many households?\nQuote: Two households, both alike in dignity, In fair Verona\n\nQuery: How many foes?\nQuote: From forth the fatal loins of these two foes A pair of star-cross’d lovers take their life"
    ],
    "text": "When a subject was accused of a crime of sufficient importance to interest the king, public notice was given that on an appointed day the fate of the accused person would be decided in the king's arena, a structure which well deserved its name, for, although its form and plan were borrowed from afar, its purpose emanated solely from the brain of this man, who, every barleycorn a king, knew no tradition to which he owed more allegiance than pleased his fancy, and who ingrafted on every adopted form of human thought and action the rich growth of his barbaric idealism.",
    "query": "Who was accused of the crime?"
}
```