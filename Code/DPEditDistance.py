# Reduce the problem to subproblems
def computeEditDistance(s, t):
    
    memo = {}
    def recurse(m, n):
        """
        Return the minimum eidt distance between
        - First m letters of s
        - First n letters of t
        """

        #To put key into dic it must be immutable, so we use tuple instead of list
        if (m,n) in memo:
            return memo[(m,n)]

        if m == 0:
            return n
        if n == 0:
            return m
        
        if s[m - 1] == t[n - 1]:
            return recurse(m - 1, n - 1)
        else:
            # The idea is to make the list shorter, since del from s is equal to add to t, 
            # then we'll select delete to make the list shorter
            subCost = 1 + recurse(m - 1, n - 1)
            delCost = 1 + recurse(m - 1, n)
            insertCost = 1 + recurse(m, n - 1)

            result = min(subCost, delCost, insertCost)

            memo[(m,n)] = result
            return result
        
    return recurse(len(s), len(t))
        

result = computeEditDistance("a casdatasdasdasd123asdasdaawd", "a cawd12312312213123ccadsdas1awdaw")
print(result)

