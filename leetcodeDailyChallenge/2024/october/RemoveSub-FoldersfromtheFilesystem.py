# https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folderSet = set(folder)
        res = []

        for f in folder:
            res.append(f)
            for i in range(len(f)):
                if f[i] == "/" and f[:i] in folderSet:
                    # meaning that folder exist thus f is a subfolder
                    res.pop()
                    break
        return res


# Trie Solution
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path):
        cur = self.root

        for p in path.split('/'):
            if p not in cur.children:
                cur.children[p] = TrieNode()
            cur = cur.children[p]
        cur.end = True

    def checkIfSubfolder(self, path):
        cur = self.root
        pathSplit = path.split("/")

        for i in range(len(pathSplit) - 1):
            cur = cur.children[pathSplit[i]]
            if cur.end:
                return True
        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Trie()
        res = []

        for f in folder:
            trie.insert(f)
        
        for f in folder:
            if not trie.checkIfSubfolder(f):
                res.append(f)
        
        return res