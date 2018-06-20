class Dictionary():
    def __init__(self, words=list()):
        self.words = set()
        self.prefixes = set()
        for word in words:
            self.add(word)

    def add(self, word):
        if word in self.words:
            return
        self.words.add(word)
        for i in range(1, len(word) + 1):
            self.prefixes.add(word[0:i])

    def is_prefix(self, prefix):
        return prefix in self.prefixes

    def is_word(self, word):
        return word in self.words
