def long_sub_str(str1, str2):
    len1, len2 = len(str1), len(str2)
    res = 0
    val = ""
    for i in range(len1):
        for j in range(len2):
            width = 0
            while (
                i + width < len1
                and j + width < len2
                and str1[i + width] == str2[j + width]
            ):
                width += 1
            if width > res:
                res = width
                val = str1[i : i + width]
    return res, val


assert (4, "abcd") == long_sub_str("abdabcdddee", "efeffseabcdss")
