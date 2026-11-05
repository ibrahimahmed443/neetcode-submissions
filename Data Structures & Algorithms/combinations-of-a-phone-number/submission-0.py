class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digits_to_char = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(i, curr_string):
            if len(curr_string) == len(digits):
                res.append(curr_string)
                return
            
            for char in digits_to_char[digits[i]]:
                backtrack(i + 1, curr_string + char)
        
        if digits:
            backtrack(0, "")
        
        return res