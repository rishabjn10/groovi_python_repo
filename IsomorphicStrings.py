def isIsomorphic(self, str1, str2):
        charCount = dict()
        #initially setting c to "a"
        c = "a"
        #iterating over str1 and str2
        for i in range(len(str1)):
            #if str1[i] is a key in charCount
            if str1[i] in charCount:
                c = charCount[str1[i]]
                if c != str2[i]:
                    return False
            #if str2[i] is not a value in charCount
            elif str2[i] not in charCount.values():
                charCount[str1[i]] = str2[i]
            else:
                return False
        return True
