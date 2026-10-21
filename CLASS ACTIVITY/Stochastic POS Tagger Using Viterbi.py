from collections import defaultdict, Counter

train = [
    [("i", "PRON"), ("read", "VERB"), ("the", "DET"), ("book", "NOUN")],
    [("the", "DET"), ("book", "NOUN"), ("is", "VERB"), ("good", "ADJ")],
    [("she", "PRON"), ("likes", "VERB"), ("a", "DET"), ("good", "ADJ"), ("book", "NOUN")],
    [("i", "PRON"), ("book", "VERB"), ("a", "DET"), ("flight", "NOUN")],
    [("they", "PRON"), ("book", "VERB"), ("tickets", "NOUN")],
    [("the", "DET"), ("dog", "NOUN"), ("runs", "VERB")],
    [("we", "PRON"), ("read", "VERB"), ("a", "DET"), ("good", "ADJ"), ("book", "NOUN")],
]

emit, trans, tagcount = defaultdict(Counter), defaultdict(Counter), Counter()

for sent in train:
    prev = "<s>"
    for word, tag in sent:
        emit[tag][word] += 1
        trans[prev][tag] += 1
        tagcount[tag] += 1
        prev = tag

TAGS = list(tagcount)

p_emit = lambda w, t: (emit[t][w] + 0.01) / (tagcount[t] + 0.5)
p_trans = lambda a, b: (trans[a][b] + 0.01) / (sum(trans[a].values()) + 0.01 * len(TAGS))

def unigram(words):
    return [max(TAGS, key=lambda t: emit[t][w]) for w in words]

def viterbi(words):
    V = [{t: (p_trans("<s>", t) * p_emit(words[0], t), None) for t in TAGS}]

    for w in words[1:]:
        V.append({
            t: max(
                (V[-1][p][0] * p_trans(p, t) * p_emit(w, t), p)
                for p in TAGS
            )
            for t in TAGS
        })

    tag = max(TAGS, key=lambda t: V[-1][t][0])
    path = [tag]

    for col in reversed(V[1:]):
        tag = col[tag][1]
        path.append(tag)

    return path[::-1]

n_book = {t: emit[t]["book"] for t in TAGS if emit[t]["book"]}
print("Counts of 'book' in training data:", n_book)

total = sum(n_book.values())
print(f"P(NOUN|book) = {n_book['NOUN'] / total:.2f}   P(VERB|book) = {n_book['VERB'] / total:.2f}\n")

for s in ["i book a flight", "the book is good", "they read the book"]:
    w = s.split()
    print(f"Sentence: {s}")
    print("  Unigram :", " ".join(f"{a}/{b}" for a, b in zip(w, unigram(w))))
    print("  Viterbi :", " ".join(f"{a}/{b}" for a, b in zip(w, viterbi(w))), "\n")
