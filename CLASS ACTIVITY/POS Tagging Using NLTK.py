import nltk
from collections import Counter
from nltk import word_tokenize, pos_tag

for pkg in ["punkt_tab", "averaged_perceptron_tagger_eng"]:
    nltk.download(pkg, quiet=True)

text = "The quick brown fox jumps over the lazy dog while Priya is reading a good book."
tokens = word_tokenize(text)
tagged = pos_tag(tokens)

meaning = {
    "DT": "determiner",
    "JJ": "adjective",
    "NN": "noun (singular)",
    "NNS": "noun (plural)",
    "NNP": "proper noun",
    "VBZ": "verb, 3rd person singular",
    "VBG": "verb, -ing form",
    "IN": "preposition / conjunction",
    ".": "punctuation",
    "VBD": "verb, past tense"
}

print("Text:", text, "\n")
print(f"{'Word':<10}{'Tag':<6}Meaning")
print("-" * 44)

for word, tag in tagged:
    print(f"{word:<10}{tag:<6}{meaning.get(tag, '')}")

print("\nTag frequency:", dict(Counter(tag for _, tag in tagged)))
