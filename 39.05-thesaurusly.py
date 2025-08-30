"""
# Thesaurusly

Given a non-empty string, `sentence`, and a non-empty map, `synonyms`, where each key is a single word in the sentence, and its value is a non-empty list of synonyms, return all possible sentences that can be created by replacing the words in the sentence with their synonyms. Words without synonyms should remain unchanged.

The input `sentence` only contains lowercase letters and spaces, while the words in `synonyms` only contain lowercase letters. The order of the generated sentences in the output does not matter.

Constraints:

- sentence consists of lowercase letters and spaces.
- The length of sentence is at most 500 characters.
- sentence contains at most 100 words.
- The synonyms map contains at most 8 entries.
- The length of each synonym list is at most 6.
- Each word in sentence or in the synonym lists is at most 10 characters.
"""


def thesaurusify(sentence, synonyms):
    words = sentence.split()
    cur = list()

    def visit(index):
        if index == len(words):
            print(" ".join(cur.copy()))
            return

        if words[index] in synonyms:
            for synonym in synonyms[words[index]]:
                cur.append(synonym)
                visit(index + 1)
                cur.pop()
        else:
            cur.append(words[index])
            visit(index + 1)
            cur.pop()

    visit(0)
    return


sentence = "one does not simply walk into mordor"
synonyms = {
    "walk": ["stroll", "hike", "wander"],
    "simply": ["just", "merely"],
}

thesaurusify(sentence, synonyms)

# res = [
#     "one does not just stroll into mordor",
#     "one does not just hike into mordor",
#     "one does not just wander into mordor",
#     "one does not merely stroll into mordor",
#     "one does not merely hike into mordor",
#     "one does not merely wander into mordor",
# ]
