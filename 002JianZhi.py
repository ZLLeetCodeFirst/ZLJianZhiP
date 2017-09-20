# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        str = ''
        for c in s:
            if c.isspace():
                str = str + '%20'
            else:
                str = str + c
        return str


if __name__ == '__main__':
    str = input()
    S = Solution()
    print(S.replaceSpace(str))
