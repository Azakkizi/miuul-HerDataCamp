# Amaç: Çift indexli harfleri büyüt, tek indexli harfleri küçült.

text = "Mummy don't know Daddy's getting hot At the body shop Doing something UNHOLY"


def alternating(string):
    new_text = ""
    for i in range(len(string)):
        if i % 2 == 0:
            new_text += string[i].upper()
        else:
            new_text += string[i].lower()
    return new_text


print(alternating(text))
