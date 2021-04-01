'''  Trie in python '''

class Node:
    def __init__(self):
        self.childern = [None]*26
        self.isEOF = False


class Trie:
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return Node()

    def _charToIndex(self,ch):
        return ord(ch) - ord('a')


    def insert(self,key):
        # if not present , inserts key into trie
        # if the key is prefix of trie node
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.childern[index]:
                pCrawl.childern[index] = self.getNode()
            pCrawl = pCrawl.childern[index]

        # mark last node as leaf
        pCrawl.isEOF = True


    def search(self,key):
        # search key in the trie
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.childern[index]:
                return False
            pCrawl = pCrawl.childern[index]

        return pCrawl != None and pCrawl.isEOF


# driver function
def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    main()
