#KMP String Matching: Given a text txt[0..n-1] and a pattern pat[0..m-1], #
#write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. 
#You may assume that n > m. Text: A A B A A C A A D A A B A A B A Pattern: A A B A.
def compute_lps_array(pat, m):
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pat[i] == pat[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(pat, txt):
    n = len(txt)
    m = len(pat)

    lps = compute_lps_array(pat, m)

    i = 0
    j = 0
    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1
        if j == m:
            print("Pattern found at index", i - j)
            j = lps[j - 1]
        elif i < n and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

# Example usage:
txt = "AABAACAADAAABAAABAA"
pat = "AAB"
kmp_search(pat, txt)