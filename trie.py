class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.original_word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a contact while preserving its original capitalization
    # Time Complexity: O(L)
    # Space Complexity: O(L) worst case for newly created nodes
    def insert(self, word):
        original_word = word.strip()

        if not original_word:
            return

        word = original_word.lower()
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        if node.is_end_of_word:
            return

        node.is_end_of_word = True
        node.original_word = original_word
    # Search for a complete contact (case-insensitive)
    # Time Complexity: O(L)
    # Auxiliary Space: O(1)
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

    # Collect contacts while preserving original capitalization
    # Time Complexity: O(S), excluding string-construction costs
    # Auxiliary Space: O(H) for recursion
    def collect_words(self, node, prefix, results):
        if node.is_end_of_word:
            results.append(node.original_word)

        for char, child in sorted(node.children.items()):
            self.collect_words(child, prefix + char, results)

# Generate autocomplete suggestions
# Time Complexity: O(P + S + K log K)
# Auxiliary Space: O(K + H), excluding returned string construction
# P = prefix length, S = nodes explored, K = suggestions, H = recursion depth
def autocomplete(self, prefix):
    prefix = prefix.strip().lower()

    if not prefix:
        return sorted(self.display_all(), key=str.lower)

    node = self.find_prefix_node(prefix)

    if node is None:
        return []

    results = []
    self.collect_words(node, prefix, results)

    return sorted(results, key=str.lower)

    # Delete a contact safely (case-insensitive)
    # Time Complexity: O(L)
    # Auxiliary Space: O(L) due to recursion
    # L = length of the contact name
    def delete(self, word):
        if not isinstance(word, str):
            return False

        word = word.strip().lower()

        if not word or not self.search(word):
            return False

        def remove(node, depth):
            if depth == len(word):
                node.is_end_of_word = False
                node.original_word = None
                return len(node.children) == 0

            char = word[depth]
            child = node.children[char]

            should_remove = remove(child, depth + 1)

            if should_remove:
                del node.children[char]

            return (
                not node.is_end_of_word
                and len(node.children) == 0
            )

        remove(self.root, 0)
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
