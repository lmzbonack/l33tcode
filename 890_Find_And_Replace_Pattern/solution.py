class Solution:
    def checkMatch(self, word, pattern):
        mapping = {}
        for idx, item in enumerate(pattern):
            # Do not override the values that already exist
            if item in mapping.keys():
                pass
            # Do not allow a value that exists already to be entered
            elif word[idx] in mapping.values():
                return False
            else:
                # add it to the dictionary
                mapping[item] = word[idx]
        
        for idx, item in enumerate(pattern):
            if mapping[item] != word[idx]:
                return False
        return True
                      
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        new = []
        for word in words:
            if(self.checkMatch(word, pattern)):
                new.append(word)  
        return new
                

    

        