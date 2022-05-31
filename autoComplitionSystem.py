# Implement an autocomplete system. 
# That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

class TreeNode:
    def __init__(self):
        self.end = False
        self.children = {}

    def all_words(self, prefix):
        if self.end:
            yield prefix

        for letter, child in self.children.items():
            yield from child.all_words(prefix + letter)

class Tree:
    # existing methods here
    def all_words_beginning_with_prefix(self, prefix):
        cur = self.root
        for c in prefix:
            cur = cur.children.get(c)
            if cur is None:
                return  # No words with given prefix

        yield from cur.all_words(prefix)

tree = Tree()
for i in ['dog', 'deer', 'deal']:
    tree.insert(i)
input = 'de'
print(list(tree.all_words_beginning_with_prefix(input)))