class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result=""
        carry=0
        length=min(len(a),len(b))
        for x in range(1,length+1):
            if a[-x] == "1" and b[-x] == "1" and carry == 1:
                carry = 1
                result = "1" + result
            elif a[-x] == "1" and b[-x] == "1" and carry == 0:
                carry = 1
                result = "0" + result
            elif (a[-x] == "1" or b[-x] == "1") and carry ==1:
                carry = 1
                result = "0" + result
            elif (a[-x] == "1" or b[-x] == "1") and carry ==0:
                carry = 0
                result = "1" + result
            elif a[-x] == "0" and b[-x] == "0" and carry == 1:
                carry = 0
                result = "1" + result
            elif a[-x] == "0" and b[-x] == "0" and carry == 0:
                carry = 0
                result = "0" + result
        if x == len(a) and x == len(b):
            pass
        else:
            longer = a if len(a) > len(b) else b
            for i in range(x+1, len(longer) + 1):
                if carry == 1:
                    if longer[-i] == "1":
                        carry = 1
                        result = "0" + result
                    else:
                        carry = 0
                        result = "1" + result
                else:
                    result = longer[-i] + result
        if carry == 1:
            result = "1" + result
        return result
    


# class Solution(object):
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         return bin(int(a, 2) + int(b, 2))[2:]   