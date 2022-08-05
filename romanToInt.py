# roman numeral to int
class Solution(object):
    def romanToInt(self, s):
        chars = []
        result = 0
        for e in s: # s is input string
            chars.append(e)
        index = 0
        for char in chars:
            # I
            if char == "I":
                if index < (len(chars)-1): # if this is the first character
                    if chars[index + 1] == "V" or chars[index + 1] == "X":
                        print(chars[index + 1]) # pass over and don't count
                    else:
                        result += 1
                else:
                    result += 1
            # V
            if char == "V":
                if index > 0:
                    if chars[index - 1] == "I":
                        result += 4
                    else:
                        result += 5
                else:
                    result += 5
            # X
            if char == "X":
                if index > 0:
                    if chars[index - 1] == "I":
                        result += 9
                    else:
                        result += 10
                else:
                    result += 10
            # L
            if char == "L":
                if index > 0:
                    if chars[index - 1] == "X":
                        result += 30
                    else:
                        #print(i)
                        result += 50
                else:
                    result += 50              
            # C
            if char == "C":
                if index > 0:
                    if chars[index - 1] == "X":
                        result += 80
                    else:
                        result += 100
                else:
                    result += 100  
            # D
            if char == "D":
                if index > 0:
                    if chars[index - 1] == "C":
                        result += 300
                    else:
                        result += 500
                else:
                    result += 500          
            # M
            if char == "M":
                if index > 0:
                    if chars[index - 1] == "C":
                        result += 800
                    else:
                        result += 1000
                else:
                    result += 1000                       
            index+=1
        return result