import re
import nltk
from nltk.corpus import treebank

patterns = [
    (r"^-?\d+(\.\d+)?$", "CD"),
    (r"(?i)^(the|a|an)$", "DT"),
    (r"(?i)^(in|on|at|of|with|to|from|by)$", "IN"),
    (r"(?i)^(is|are|was|were|am|be)$", "VB"),
    (r".*ing$", "VBG"),
    (r".*ed$", "VBD"),
    (r".*ly$", "RB"),
    (r".*(ness|ment|tion|ity)$", "NN"),
    (r".*(able|ous|ful|ive)$", "JJ"),
    (r".*'s$", "POS"),
    (r"^[A-Z][a-z]+$", "NNP"),
    (r".*s$", "NNS"),
    (r".*", "NN"),
]

def tag(words):
    result = []
    for w in words:
        for pattern, t in patterns:
            if re.match(pattern, w):
                result.append((w, t, pattern))
                break
    return result

sentence = "The talented programmer quickly completed 3 amazing projects in Chennai".split()

print(f"{'Word':<12}{'Tag':<6}Rule applied")

for w, t, p in tag(sentence):
    print(f"{w:<12}{t:<6}{p}")

nltk.download("treebank", quiet=True)

gold = [pair for sent in treebank.tagged_sents()[:300] for pair in sent]
words = [w for w, _ in gold]

rule_acc = sum(t == g for (_, t, _), (_, g) in zip(tag(words), gold)) / len(gold)
base_acc = sum(g == "NN" for _, g in gold) / len(gold)

print(f"\nAccuracy on {len(gold)} Treebank tokens:")
print(f"  regex rules = {rule_acc:.1%}    always-NN baseline = {base_acc:.1%}")
