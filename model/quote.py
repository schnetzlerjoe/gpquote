import os
import sys
import openai
import json

class Quote:
    # set api key from system variable
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # initializes the class to be used for training/testing
    def __init__(self, text: str, query: str, page_size: int = 10000) -> list:
        self.text = text
        self.query = query
        self.page_size = page_size
        self.current_page = 0
        self.total_pages = max(1, page_size/len(text))

    # is the main function for training. Allows for changing the class prompt to play around with different prompts.
    def get_supporting_quotes(self, model: str = "text-davinci-002", page: int = 0, prompt: str = None, temperature: int = 0, max_tokens: int = 100, top_p: float = 1.0, best_of: int = 1, frequency_penalty: float = 0.0, presence_penalty: float = 2.0) -> list:
        # make sure prompt is not empty
        if prompt == None:
            sys.exit("empty prompt")
        # run it through gpt-3
        resRaw = openai.Completion.create(
            model=model,
            prompt=prompt + "\n\n" + self.text + "\n\nQuery" + ": " + self.query,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            best_of=best_of,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )

        res: str = resRaw['choices'][0]['text']

        if res == "":
            sys.exit("GPT-3 response is empty")
        else:
            # backout of the quote format to get the raw quote text
            res = res.split("\nQuote: ")[1]
            # get rid of any extra space or further generation beyond query
            res = res.split("\n")[0]

        return self.verify_quote(res)
    
    # checks if the quote is within text (by lowercasing all text to compare).
    # returns a list in [quote, [start_index, end_index]] format if so otherwise returns None
    def verify_quote(self, quote: str) -> list:
        if quote.lower() in self.text.lower():
            # lets find the beginning position of sentence
            start_index = self.text.lower().find(quote.lower())
            # add the length of the sentence to start_index to get end position
            end_index = start_index + len(quote.lower())
            # build response
            res = [quote, [start_index, end_index]]
            return res
        else:
            return None

# takes in a file that has a list of prompts and runs through each prompt testing them against
# class set text and query. Returns verify quote for each prompt.
def get_metrics(file_path: str) -> None:
    # reads a json file with test format
    file = open(file_path)
    # convert to json dict
    data = json.load(file)
    # get list of prompts
    prompts = data["prompts"]
    # init class
    q = Quote(data["text"], data["query"], 1000)

    # iterate over prompts
    for p in prompts:
        res = q.get_supporting_quotes(model=data["model"], prompt=p, temperature=data["temperature"], max_tokens=data["max_tokens"], top_p=data["top_p"], best_of=data["best_of"], frequency_penalty=data["frequency_penalty"], presence_penalty=data["presence_penalty"])
        print(res, "\n")