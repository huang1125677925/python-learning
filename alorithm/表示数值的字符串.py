def isNumeric(s):
    isAllowDot = True
    isAllowE = True
    for i in range(len(s)):
        # 正负只能出现第一个位置或者eE后边位置，并且需要当前位置不能是最后一个位置，无论是那个位置，都不能是最后一个位置
        if s[i] in "+-" and (i==0 or s[i-1] in "eE") and i < len(s)-1:
            continue
        #     当前点还没出现，把这个符号去掉，然后如果当前点在最后一个位置，这肯定是不对的，或者说点前面不是数字，这也是不对的
        elif isAllowDot and s[i] == ".":
            isAllowDot = False
            if i >= len(s)-1 or s[i+1] not in "0123456789":
                return False
        # 如果出现了E，后边是不允许有dot存在的，所以必须是False，E出现是能是第一次，当变成False的时候，这一段就不允许处理了
        elif isAllowE and s[i] in "Ee":
            isAllowDot = False
            isAllowE = False
            if i >= len(s)-1 or s[i+1] not in "0123456789+-":
                return False
        # 如果E存在，后边的数值就只能是0-9
        elif s[i] not in "0123456789":
            return False
    return True


print(isNumeric('12.033E012'))