# 给定一个字符串，找到最长子字符串的长度而不重复字符。
# 例1：
# 输入：“abcabcbb” 
# 输出：3 
#  说明：答案是"abc"，长度为3。 
# 例2：
# 输入：“BBBBB” 
# 输出：1
#  说明：他的回答是"b"，与1的长度。
# 例3：
# 输入：“pwwkew” 
# 输出：3
#  说明：答案是"wke"，长度为3。
# 请注意，答案必须是子字符串，"pwke"是子序列而不是子字符串。

#思路：
#借助hashmap来存放字符串，创建一个头指针指向第一个字符，再创建一个遍历指针；
#遍历指针的字符与头指针的字符进行比较，如果不相等的话，更新maxLength,如果相等的话，更新头指针的指向位置(头指针与map中的字符的下一个位置比较)
#无论是否相等，更新字符的最近的出现位置

#abcdeade
class Solution:
    def lengthOfLongestSubstring(self, string):
        dic = {} #创建hashmap
        start = 0
        maxLength = 0
        for i in range(len(string)):
            if string[i] in dic and start <= dic[string[i]]: #进行比较和位置偏移
                start = dic[string[i]]+1
            else:
                maxLength = max(maxLength, i-start+1)    #记录最大的长度
            dic[string[i]] = i
        return maxLength

test = Solution()
maxLength = test.lengthOfLongestSubstring("abcabcbb")
print(maxLength)
