lexicon = {
    "i": "PRP",
    "want": "VBP",
    "to": "TO",
    "book": "NN",
    "a": "DT",
    "flight": "NN",
    "she": "PRP",
    "can": "MD",
    "run": "NN",
    "fast": "RB",
    "they": "PRP",
    "have": "VBP",
    "walked": "VBD",
    "home": "NN"
}

rules = [
    ("NN", "VB", lambda pw, pt: pt == "TO", "NN -> VB if previous tag is TO"),
    ("NN", "VB", lambda pw, pt: pt == "MD", "NN -> VB if previous tag is MD"),
    ("VBD", "VBN", lambda pw, pt: pw in ("have", "has", "had"),
     "VBD -> VBN if previous word is have/has/had"),
]

def brill_tag(sentence):
    words = sentence.split()
    tags = [lexicon[w] for w in words]

    print("Sentence :", sentence)
    print("Initial  :", " ".join(f"{w}/{t}" for w, t in zip(words, tags)))

    for frm, to, cond, name in rules:
        for i in range(1, len(words)):
            if tags[i] == frm and cond(words[i - 1], tags[i - 1]):
                print(f"  Rule applied: {name}   [{words[i]}: {frm} -> {to}]")
                tags[i] = to

    print("Final    :", " ".join(f"{w}/{t}" for w, t in zip(words, tags)), "\n")

for s in ["i want to book a flight", "she can run fast", "they have walked home"]:
    brill_tag(s)
