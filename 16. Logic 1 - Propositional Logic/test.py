from typing import List


class Solution:

    

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        for i in range(0, len(s), 1):
            print("now i is : " + str(i))
            j = i
            while s[j] != "#":
                print("now j is : " + str(j))
                j += 1
            

            length = int(s[i:j])
            string = s[j + 1: j + 1 + length]
            res.append(string)
            i = j + 1 + length

        return res

# Solution.decode(Solution,"4#Halo")

for i in range(10):
    print(i)
    # This assignment will be override with for loop!
    i = 9