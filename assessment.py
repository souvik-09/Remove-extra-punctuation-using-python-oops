class NoYelling:
    # The __init__() method is a constructor that takes one parameter phrase,
    # which is stored in the class variable self.phrase.
    def __init__(self, phrase):
        self.phrase = phrase
    
    # The remove_excess_punctuation() method removes any excess exclamation 
    # or question marks from the end of the self.phrase.
    def remove_excess_punctuation(self):
        while self.phrase.endswith(("??", "!!")):
            self.phrase = self.phrase[:-1]
            
            
    # The get_phrase() method simply returns the self.phrase.
    def get_phrase(self):
        return self.phrase


# Usage
no_yelling = NoYelling("What went wrong?????????")
no_yelling.remove_excess_punctuation()
print(no_yelling.get_phrase())  # Output: "What went wrong?"

no_yelling = NoYelling("Oh my goodness!!!")
no_yelling.remove_excess_punctuation()
print(no_yelling.get_phrase())  # Output: "Oh my goodness!"

no_yelling = NoYelling("I just!!! can!!! not!!! believe!!! it!!!")
no_yelling.remove_excess_punctuation()
print(no_yelling.get_phrase())  # Output: "I just!!! can!!! not!!! believe!!! it!"

no_yelling = NoYelling("Oh my goodness!")
no_yelling.remove_excess_punctuation()
print(no_yelling.get_phrase())  # Output: "Oh my goodness!"

no_yelling = NoYelling("I just cannot believe it.")
no_yelling.remove_excess_punctuation()
print(no_yelling.get_phrase())  # Output: "I just cannot believe it."
