#计算一个字符串中的回文
# 给定一个字符串小号，发现最长的回文子小号。您可以假设s的最大长度为1000。
# 例1：
# 输入： “babad”
#  输出： “bab”
#  注意： “aba”也是一个有效的答案。
# 例2：
# 输入： “cbbd”
# 输出： “bb”
#思路： 遍历字符串，从指向的字符串开始向两侧扩散


def findString(string):
    #奇数，偶数两种情况
    res = ''
    for i in range(len(string)):
        tmp = strString(string, i , i) #总长为奇树的情况
        if len(tmp) > len(res): #求最长的回文
            res = tmp 
        tmp = strString(string, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    if len(res) == 1:
        res = ''
    return res

def strString(string, l, r): #从某个字母的中间开始向两侧扩散
    while l >= 0 and r < len(string) and string[l] == string[r]:
        l -= 1
        r += 1

    return string[l+1:r]
    
string = "abcdefB"
result = findString(string)
print(result)