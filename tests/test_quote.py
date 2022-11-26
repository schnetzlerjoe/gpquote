from ward import test
from model.quote import Quote, get_metrics

# Define test data here
test_prompt = "Two households, both alike in dignity, In fair Verona, where we lay our scene, From ancient grudge break to new mutiny, Where civil blood makes civil hands unclean. From forth the fatal loins of these two foes A pair of star-cross’d lovers take their life; Whose misadventured piteous overthrows Do with their death bury their parents’ strife. The fearful passage of their death-mark’d love, And the continuance of their parents’ rage, Which, but their children’s end, nought could remove, Is now the two hours’ traffic of our stage; The which if you with patient ears attend, What here shall miss, our toil shall strive to mend.\n\nQuery: What city does this take place in?\nQuote: Two households, both alike in dignity, In fair Verona, where we lay our scene\n\nQuery: How many households?\nQuote: Two households, both alike in dignity, In fair Verona\n\nQuery: How many foes?\nQuote: From forth the fatal loins of these two foes A pair of star-cross’d lovers take their life"
test_text = "When a subject was accused of a crime of sufficient importance to interest the king, public notice was given that on an appointed day the fate of the accused person would be decided in the king's arena, a structure which well deserved its name, for, although its form and plan were borrowed from afar, its purpose emanated solely from the brain of this man, who, every barleycorn a king, knew no tradition to which he owed more allegiance than pleased his fancy, and who ingrafted on every adopted form of human thought and action the rich growth of his barbaric idealism."
test_query= "Who was accused of the crime?"

@test("check quote class can be created")
def _():
    q = Quote(test_text, test_query, 1000)
    assert q.page_size == 1000

@test("test get_supporting_quotes. should return list")
def _():
    q = Quote(test_text, test_query, 1000)
    res = q.get_supporting_quotes(prompt=test_prompt)
    print(res)
    assert type(res) == list

@test("test get_metrics. should return metrics")
def _():
    get_metrics("./tests/test.json")