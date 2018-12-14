def strmatch(pattern, str1):
    s_len = len(str1)
    p_len = len(pattern)
    if not pattern:
        if not str1:
            return True
        return False

    if len(pattern) in [0]:
        if len(str1) in [0]:
            return True
        return False

    lookup = [[False for i in range(p_len + 1)] for j in range(s_len + 1)]

    lookup[0][0] = True

    for j in range(1, p_len):
        if pattern[j - 1] == "*":
            lookup[0][j] = lookup[0][j - 1]

    if pattern[0] in ["*"]:
        lookup[0][1] = True

    for i in range(1, s_len + 1):
        for j in range(1, p_len + 1):

            if pattern[j - 1] in ["*"]:
                lookup[i][j] = lookup[i][j - 1] or lookup[i - 1][j]

            elif pattern[j - 1] in ['?'] or str1[i - 1] == pattern[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1]

            else:
                lookup[i][j] = False

    # print(lookup)
    return lookup[s_len][p_len]


if __name__ == '__main__':
    print(strmatch("x?y*z", "xaylmz"))
    print(strmatch("**ba*****ab", "baaabab"))
    print(strmatch("a***a", "aa"))
    print(strmatch("**ho", "ho"))
