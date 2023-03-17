class Trie:        
    def __init__(self):
        self.children = {}

    def insert(self, word: str) -> None:
        if word == "":
            self.children["."] = True
            return
        if word[0] not in self.children:
            self.children[word[0]] = Trie()
        self.children[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if word == "":
            return "." in self.children
        if word[0] not in self.children:
            return False
        return self.children[word[0]].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if prefix == "":
            return True
        if prefix[0] not in self.children:
            return False
        return self.children[prefix[0]].startsWith(prefix[1:])