class Solution:
    def convert(self, s: str, numRows: int) -> str:
        result = [''] * numRows

        index, step = 0, 1

        for s_i in s:
            result[index] += s_i
            if index == numRows-1:
                step = -1
            elif index == 0:
                step = 1

            if numRows >1 :
                index += step

        return ''.join(result)
        
print(Solution().convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR')
print(Solution().convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI')
print(Solution().convert('ABC', 1) == 'ABC')
print(Solution().convert('A', 1) == 'A')