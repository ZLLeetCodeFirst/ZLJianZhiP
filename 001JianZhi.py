class Solution:
    def Find(self,target,array):
        n = len(array)
        flag = 'false'
        for i in range(n):
            if target in array[i]:
                flag = 'true'
                break
        return flag

while True:
    try:
        S = Solution()
        L = list(eval(input()))
        array = L[1]
        target = L[0]
        print(S.Find(target,array))
    except:
        break





