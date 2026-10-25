# Mobile Contact Search and Auto-Complete System Using Trie

## 1. Project Overview

The Mobile Contact Search and Auto-Complete System is a Python application that uses a Trie (Prefix Tree) data structure to manage and search contact names efficiently.

The system supports inserting contacts, searching for a contact, generating autocomplete suggestions, deleting contacts, and displaying all stored contacts.

## 2. Problem Statement

Searching for a particular contact among a large number of names can be inconvenient. A Trie provides an efficient way to organize contact names character by character and retrieve contacts matching a given prefix.

Our project demonstrates how a Trie can be used to implement contact searching and autocomplete functionality.

## 3. Objectives

* Implement a Trie data structure using Python.
* Insert and search for contact names.
* Generate autocomplete suggestions using prefixes.
* Delete contacts without affecting other contacts that share prefixes.
* Display all stored contacts.
* Analyse the time and space complexity of the operations.

## 4. Data Structure Used

### Trie (Prefix Tree)

A Trie is a tree-like data structure that stores strings character by character.

Each node contains:

* A dictionary of child nodes.
* A Boolean flag indicating whether a complete word ends at that node.

The root node represents the starting point of the Trie.

### Why Trie?

* Supports efficient prefix-based searching.
* Allows autocomplete suggestions to be generated from a prefix.
* Shares nodes among contacts with common prefixes.
* Provides insertion and exact-search operations whose time depends on the length of the contact name.

## 5. Features

1. **Add Contact:** Inserts a contact into the Trie.
2. **Search Contact:** Checks whether a complete contact exists.
3. **Autocomplete:** Displays contacts matching the entered prefix.
4. **Delete Contact:** Removes a contact while preserving shared prefixes.
5. **Display All Contacts:** Lists the contacts stored in the Trie.
6. **Interactive Menu:** Allows users to select operations.

## 6. Algorithms

### Insertion

1. Start at the root node.
2. Process each character in the contact name.
3. Create a child node if the character path does not exist.
4. Move to the corresponding child node.
5. Mark the final node as the end of a complete word.

### Searching

1. Start at the root.
2. Follow the child corresponding to each character.
3. If a required character is missing, return false.
4. After processing all characters, check the end-of-word flag.

### Autocomplete

1. Traverse the Trie using the characters of the prefix.
2. If the prefix path does not exist, return an empty list.
3. Otherwise, explore the subtree rooted at the prefix node.
4. Collect all complete words found in that subtree.

### Deletion

1. Check whether the complete contact exists.
2. Follow its character path recursively.
3. Unmark the end-of-word flag.
4. Remove nodes only when they are not needed by another contact.

## 7. Time Complexity Analysis

Let:

* L = length of a contact name.
* P = length of the search prefix.
* S = number of Trie nodes explored during autocomplete.
* C = total number of characters stored across all contacts.

| Operation            | Time Complexity | Explanation                                                |
| -------------------- | --------------- | ---------------------------------------------------------- |
| Insert Contact       | O(L)            | Processes each character once.                             |
| Search Contact       | O(L)            | Follows the characters of the contact name.                |
| Find Prefix Node     | O(P)            | Processes each prefix character.                           |
| Autocomplete         | O(P + S)        | Finds the prefix node and explores its subtree.            |
| Delete Contact       | O(L)            | Searches for the contact and processes its character path. |
| Display All Contacts | O(C)            | Traverses the Trie and collects all stored contacts.       |

These bounds assume dictionary operations take O(1) time on average. For autocomplete, S represents the number of nodes explored, including the work needed to collect the matching names.

## 8. Space Complexity Analysis

The Trie requires O(C) space, where C is the total number of characters across all stored contacts.

Each distinct character position may require a node. Contacts with common prefixes can share nodes, reducing the number of nodes required.

Autocomplete also requires additional space for the result list and traversal recursion. The recursive traversal can use stack space proportional to the depth explored.

## 9. Testing

The following test cases are used to verify the program:

| Test Case                              | Expected Result                  |
| -------------------------------------- | -------------------------------- |
| Search for an existing contact         | Contact found                    |
| Search for a nonexistent contact       | Contact not found                |
| Autocomplete using prefix `Ar`         | Matching contacts displayed      |
| Autocomplete using an unmatched prefix | No matching contacts             |
| Delete an existing contact             | Contact deleted successfully     |
| Search for a deleted contact           | Contact not found                |
| Delete a nonexistent contact           | Contact not found                |
| Display all contacts                   | All remaining contacts displayed |

## 10. Technologies Used

* Programming Language: Python
* Data Structure: Trie (Prefix Tree)
* Development Environment: Python IDLE
* Version Control: GitHub

## 11. How to Run the Project

1. Download `main.py` and `trie.py` from the GitHub repository.
2. Save both files in the same folder.
3. Open `main.py` using Python IDLE.
4. Select **Run → Run Module** or press F5.
5. Choose an operation from the menu and follow the prompts.

## 12. Limitations

* The current implementation stores contact names rather than complete phone numbers and contact details.
* A Trie can consume more memory than some alternative data structures.
* Contacts are stored in memory and are not permanently saved between program executions.
* The current implementation converts names to lowercase.

## 13. Future Enhancements

* Store phone numbers and additional contact details.
* Add permanent storage using a file or database.
* Develop a graphical user interface.
* Support more character sets and Unicode names.
* Rank autocomplete suggestions based on contact frequency.

## 14. Conclusion

This project demonstrates the practical use of a Trie for contact management and prefix-based searching. It implements insertion, exact searching, autocomplete, deletion, and contact display operations.

The project also analyses the time and space complexity of these operations, showing how data structures can improve the efficiency of real-world applications.

## 15. Repository

GitHub: https://github.com/naziyaa16/trie-contact-autocomplete
