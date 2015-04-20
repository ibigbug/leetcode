# Link: https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        str = str.strip()
        s = []
        for i, bit in enumerate(str):
            if i == 0 and (bit == '+' or bit == '-'):
                s.append(bit)
            elif bit >= '0' and bit <= '9':
                s.append(bit)
            else:
                break

        l = len(s)
        for index, bit in enumerate(s):
            if bit >= '0' and bit <= '9':
                s[index] = int(bit) * 10 ** (l - index - 1)

        ret = 0
        for bit in s:
            if bit == '-' or bit == '+':
                continue
            ret += bit

        if l >1 and s[0] == '-':
            ret *= -1

        if ret > 2147483647:
            return 2147483647
        if ret < -2147483648:
            return -2147483648
        return ret
