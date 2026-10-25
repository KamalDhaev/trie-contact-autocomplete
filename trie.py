class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a contact
    # Time Complexity: O(L)
    # Space Complexity: O(L) worst-case additional space for new nodes
    # L = length of the contact name
    def insert(self, word):
        word = word.strip().lower()

        if not word:
            return

        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end_of_word = True

    # Search for a complete contact
    # Time Complexity: O(L)
    # Auxiliary Space: O(1) iterative search
    # L = length of the contact name
    def search(self, word):
        word = word.strip().lower()

        if not word:
            return False

        node = self.root

        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        return node.is_end_of_word

    # Find the node corresponding to a prefix
    # Time Complexity: O(P)
    # Auxiliary Space: O(1)
    # P = length of the prefix
    def find_prefix_node(self, prefix):
        node = self.root

        for char in prefix.strip().lower():
            if char not in node.children:
                return None

            node = node.children[char]

        return node

    # Collect complete words below a node
    # Time Complexity: O(S) for the explored subtree,
    # excluding the cost of constructing longer strings
    # Recursive auxiliary space: O(H)
    # S = number of nodes explored; H = maximum traversal depth
    def collect_words(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(prefix)

        for char, child in sorted(node.children.items()):
            self.collect_words(child, prefix + char, results)

    # Generate autocomplete suggestions
    # Time Complexity: O(P + S), excluding string-construction costs
    # P = prefix length; S = number of nodes explored
    def autocomplete(self, prefix):
        prefix = prefix.strip().lower()
        node = self.find_prefix_node(prefix)

        if node is None:
            return []

        results = []
        self.collect_words(node, prefix, results)

        return results

    # Delete a contact
    # Time Complexity: O(L)
    # Recursive auxiliary space: O(L)
    # L = length of the contact name
    def delete(self, word):
        word = word.strip().lower()

        if not word or not self.search(word):
            return False

        def remove(node, word, depth):
            if depth == len(word):
                node.is_end_of_word = False
            else:
                char = word[depth]
                child = node.children[char]

                remove(child, word, depth + 1)

                if not child.children and not child.is_end_of_word:
                    del node.children[char]

        remove(self.root, word, 0)
        return True

    # Display all contacts
    # Time Complexity: O(C), excluding string-construction costs
    # C = total number of stored characters/nodes, up to constant factors
    def display_all(self):
        results = []
        self.collect_words(self.root, "", results)
        return results


# Demonstration
if __name__ == "__main__":
    trie = Trie()

    contacts = ["Arun", "Aravind", "Arjun", "Anu", "Rahul"]

    for contact in contacts:
        trie.insert(contact)

    print("All contacts:", trie.display_all())

    print("\nSearch Arun:", trie.search("Arun"))
    print("Search Ramesh:", trie.search("Ramesh"))

    print("\nAutocomplete for 'Ar':", trie.autocomplete("Ar"))

    print("\nDeleting Arun:", trie.delete("Arun"))

    print("Search Arun after deletion:", trie.search("Arun"))
    print("Autocomplete for 'Ar':", trie.autocomplete("Ar"))

    print("\nDeleting Ramesh:", trie.delete("Ramesh"))
