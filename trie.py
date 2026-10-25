class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a contact
    def insert(self, word):
        node = self.root

        for char in word.lower():
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end_of_word = True

    # Search for a complete contact
    def search(self, word):
        node = self.root

        for char in word.lower():
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end_of_word

    # Find the node corresponding to a prefix
    def find_prefix_node(self, prefix):
        node = self.root

        for char in prefix.lower():
            if char not in node.children:
                return None

            node = node.children[char]

        return node

    # Collect all complete words below a node
    def collect_words(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)

        for char, child in node.children.items():
            self.collect_words(child, prefix + char, results)

    # Generate autocomplete suggestions
    def autocomplete(self, prefix):
        node = self.find_prefix_node(prefix)

        if node is None:
            return []

        results = []
        self.collect_words(node, prefix.lower(), results)

        return results


if __name__ == "__main__":
    trie = Trie()

    contacts = ["Arun", "Aravind", "Arjun", "Anu", "Rahul"]

    for contact in contacts:
        trie.insert(contact)

    print("Search Arun:", trie.search("Arun"))
    print("Search Rahul:", trie.search("Rahul"))
    print("Search Ramesh:", trie.search("Ramesh"))

    print("\nAutocomplete for 'Ar':")
    print(trie.autocomplete("Ar"))

    print("\nAutocomplete for 'Ra':")
    print(trie.autocomplete("Ra"))

    print("\nAutocomplete for 'Z':")
    print(trie.autocomplete("Z"))
