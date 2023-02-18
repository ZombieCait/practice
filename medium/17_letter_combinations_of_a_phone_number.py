from itertools import combinations

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def get_combinations(i, current_combination, combinations):
            if i == lenght:
                combinations.append("".join(current_combination))
                return

            chars = numbers_to_letters[digits[i]]
            for char in chars:
                current_combination.append(char)
                get_combinations(
                    i + 1, current_combination, combinations
                )
                current_combination.pop()

        numbers_to_letters = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        
        combinations = []
        lenght = len(digits)
        if lenght == 0:
            return []
        elif lenght == 1:
            return list(numbers_to_letters[digits[0]])
        
        letters = [numbers_to_letters[digit] for digit in digits]
        get_combinations(0, [], combinations)

        return combinations
