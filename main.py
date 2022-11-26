from model.quote import get_metrics, Quote

while True:

    use_file = input("Use JSON file as input? (yes or no)\n")

    if use_file == "yes" or use_file == "y":
        path = input("What is the path of the config file?\n")
        res = get_metrics(path)
        print(res)
    else:
        text = input("What text would you like to test against?\n")
        query = input("What query would you like to use?\n")
        prompt = input("what is the prompt you would like to train with?\n")
        q = Quote(text, query)
        res = q.get_supporting_quotes(prompt=prompt)
        print(res)

    c = input("Would you like to train again?\n")
    if c == "no" or c == "n":
        break