class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end_of_word = True

    def search(self, word):
        node = self.root

        for char in word.lower():
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end_of_word


if __name__ == "__main__":
    trie = Trie()

    trie.insert("Arun")
    trie.insert("Arjun")
    trie.insert("Anu")

    print("Search Arun:", trie.search("Arun"))
    print("Search Anu:", trie.search("Anu"))
    print("Search Rahul:", trie.search("Rahul"))
