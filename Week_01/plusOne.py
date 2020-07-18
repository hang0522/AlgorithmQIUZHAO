class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1]+=1
            return digits
        elif len(digits)==1:
            return [1,0]
        elif digits[-1]==9:
            digits[-1]=0
            i=len(digits)-2
            while i>=0:
                if digits[i]!=9:
                    digits[i]+=1
                    return digits
                else:
                    digits[i]=0
                    i=i-1
            if digits[0]==0:
                new_digits = [1]
                new_digits = new_digits+digits
                return new_digits
            