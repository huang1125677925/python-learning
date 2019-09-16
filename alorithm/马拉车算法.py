def manacher(self):
    s = '#' + '#'.join(self) + '#'  # 字符串处理，用特殊字符隔离字符串，方便处理偶数子串
    lens = len(s)
    p = [0] * lens  # p[i]表示i作中心的最长回文子串的半径，初始化p[i]
    mx = 0  # 之前最长回文子串的右边界
    id = 0  # 之前最长回文子串的中心位置
    for i in range(lens):  # 遍历字符串
        if mx > i:
            p[i] = min(mx - i, p[int(2 * id - i)])  # 由理论分析得到
        else:  # mx <= i
            p[i] = 1
        while i - p[i] >= 0 and i + p[i] < lens and s[i - p[i]] == s[i + p[i]]:  # 满足回文条件的情况下
            p[i] += 1  # 两边扩展
        if (i + p[i]) > mx:  # 新子串右边界超过了之前最长子串右边界
            mx, id = i + p[i], i  # 移动之前最长回文子串的中心位置和边界，继续向右匹配
    i_res = p.index(max(p))  # 获取最终最长子串中心位置
    s_res = s[i_res - (p[i_res] - 1):i_res + p[i_res]]  # 获取最终最长子串，带"#"
    return s_res.replace('#', ''), max(p) - 1  # 返回最长回文子串（去掉"#"）和它的长度


print(manacher(''))
print(manacher(' '))
print(manacher('babad'))
print(manacher('cbbd'))
print(manacher('nw'))
print(manacher('bbbb'))
print(manacher(
    'civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'))





