class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0 or digits is None:
            return []
        
        self.letter_map = {
            "2":["a","b","c"],"3":["d","e","f"],
            "4":["g","h","i"],"5":["j","k","l"],
            "6":["m","n","o"],"7":["p","q","r","s"],
            "8":["t","u","v"],"9":["w","x","y","z"],
        }
        self.result = []
        self.helper("",digits,0)
        return self.result
    def helper(self,cur,digits,level):
        if level==len(digits):
            self.result.append(cur)
            return
        
        for letter in self.letter_map[digits[level]]:
            self.helper(cur+letter,digits,level+1)