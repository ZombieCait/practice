class Solution:
    def intToRoman(self, num: int) -> str:
        int_to_roman_dict = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        result = ""

        while num != 0:
            for key, value in int_to_roman_dict.items():
                repeat = num // key
                if repeat > 0:
                    result += value * repeat
                    num = num - key * repeat
                    break

        return result


# better ?? not on leetcode tests
class Solution:
    def intToRoman(self, num: int) -> str:
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        romans = [
            "M",
            "CM",
            "D",
            "CD",
            "C",
            "XC",
            "L",
            "XL",
            "X",
            "IX",
            "V",
            "IV",
            "I",
        ]

        result = ""
        index = 0

        while num != 0:
            for i in range(index, len(numbers)):
                repeat = num // numbers[i]
                if repeat > 0:
                    result += romans[i] * repeat
                    num = num - numbers[i] * repeat
                    index = i + 1
                    break

        return result
