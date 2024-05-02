# Roman to Integer
# 解題思路；數字比後面大相加，數字比後面小相減

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        i = 0
        # 直到 跑的次數小於字長度 就回傳總值
        while i < len(s):
            print(roman_map[s[i]], end=" ")
            # 次數加一小於字串長度 並且 前面得數字小於後面得數字 相減
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
            i += 1
        return total

result = Solution()

# Output: 3
print(" |測試1", result.romanToInt("III"))
# Output: 58
print(" |測試2", result.romanToInt("LVIII"))
# Output: 1994
print(" |測試3", result.romanToInt("MCMXCIV"))

# 羅馬規則
# I 可以重複最多三次，如 III 表示 3。
# X（10）可以重複最多三次，如 XXX 表示 30。
# C（100）可以重複最多三次，如 CCC 表示 300。
# M（1000）可以重複無限次，但通常情況下，按傳統格式也不會超過三次或四次。
#  V、L、D 只會顯示一次