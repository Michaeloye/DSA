# https://leetcode.com/problems/longest-common-prefix/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = TrieNode()

        def longestCommonPrefix():
            prefix = ""
            node = root

            while True:
                if len(node.children) != 1 or node.isEnd:
                    break
                # Otherwise, continue down the tree and add to the prefix
                for char, nextNode in node.children.items():
                    prefix += char
                    node = nextNode

            return prefix

        for word in strs:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.isEnd = True

        return longestCommonPrefix()
