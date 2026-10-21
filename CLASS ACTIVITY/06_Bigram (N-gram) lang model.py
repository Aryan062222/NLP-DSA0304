import random
from collections import defaultdict, Counter

corpus = """natural language processing is a part of artificial intelligence .
language models predict the next word in a sentence .
a bigram model predicts the next word using the previous word .
natural language models learn patterns from text .
text generation uses a language model to predict the next word ."""

words = corpus.lower().split()
bigrams = defaultdict(Counter)

for w1, w2 in zip(words, words[1:]):
    bigrams[w1][w2] += 1

print("Bigram probabilities  P(next word | word)")
for w in ["language", "the", "next", "a"]:
    total = sum(bigrams[w].values())
    probs = ", ".join(f"{n}={c}/{total}" for n, c in bigrams[w].most_common())
    print(f"  {w:<9}-> {probs}")

def generate(start, length=10):
    out = [start]
    for _ in range(length - 1):
        following = bigrams[out[-1]]
        if not following:
            break
        out.append(random.choices(list(following), weights=following.values())[0])
    return " ".join(out)

random.seed(7)

print("\nGenerated text (bigram model)")
for start in ["natural", "language", "a", "text"]:
    print(f"  start='{start}': {generate(start)}")
