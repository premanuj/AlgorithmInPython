"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

"""


class TrieNode:
    def __init__(self, *args, **kwargs):
        self.children = {}
        self.last = False


class Tire:
    def __init__(self, *args, **kwargs):
        self.root = TrieNode()
        self.word_list = []

    def build_tire(self, keys):
        for key in keys:
            self.insert(key)

    def insert(self, key):
        node = self.root
        for i in list(key):
            if not node.children.get(i):
                node.children[i] = TrieNode()
            node = node.children[i]
        node.last = True
        print(node.children, node.last)

    def search(self, key):
        node = self.root
        found = True
        for a in list(key):
            if not node.children.get(a):
                found = False
                break
            node = node.children[a]
        return node and node.last and found

    def suggest(self, node, word):
        if node.last:
            self.word_list.append(word)

        for a, n in node.children.items():
            self.suggest(n, word + a)

    def show_auto_suggest(self, key):
        node = self.root
        not_found = False
        temp = ""
        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break
            temp += a
            print(
                ">>",
                {
                    i: {
                        p: {a: b.children for a, b in q.children.items()}
                        for p, q in j.children.items()
                    }
                    for i, j in node.children.items()
                },
            )
            node = node.children[a]
        if not_found:
            return 0
        elif node.last and not node.children:
            return -1

        self.suggest(node, temp)

        for word in self.word_list:
            print(word)
        return 1


if __name__ == "__main__":
    keys = ["hello", "dog", "dogn", "hell", "cat", "a", "hel", "help", "helps", "helping"]
    key = "d"
    t = Tire()
    t.build_tire(keys)
    comp = t.show_auto_suggest(key)

    if comp == -1:
        print("No other strings found with this prefix\n")
    elif comp == 0:
        print("No string found with this prefix\n")

