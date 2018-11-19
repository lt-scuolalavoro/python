class phraseClass:
  phrase = ""
  def invert(self):
    return self.phrase[::-1]
  def wordCount(self):
    return len(self.phrase.split())

phrase1 = phraseClass()
phrase1.phrase = "Hello World!"
print(phrase1.invert())
print(phrase1.wordCount())

phrase2 = phraseClass()
phrase2.phrase = "All good things come to an end"
print(phrase2.invert())
print(phrase2.wordCount())
