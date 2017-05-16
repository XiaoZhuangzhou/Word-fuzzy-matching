def load_word(filename="word.txt"):
    words = open(filename)
    word_list=[]
    for i in words:
        word_list.append(i.strip("\n"))
    return word_list


def soundex(name, len=4):
    digits = '01230120022455012623010202'
    sndx = ''
    fc = ''

    for c in name.upper():
        if c.isalpha():
            if not fc:
                fc = c
            d = digits[ord(c) - ord('A')]
            if not sndx or (d != sndx[-1]):
                sndx += d
    sndx = fc + sndx[1:]
    sndx = sndx.replace('0', '')
    return (sndx + (len * '0'))[:len]


def levenshtein(s, t):
    if len(s) > len(t):
        s, t = t, s
    n = len(s)
    m = len(t)
    if not m:
        return n
    if not n:
        return m
    v0 = [i for i in range(0, m + 1)]
    v1 = [0] * (m + 1)
    cost = 0
    for i in range(1, n + 1):
        v1[0] = i
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            a = v0[j] + 1
            b = v1[j - 1] + 1
            c = v0[j - 1] + cost
            v1[j] = min(a, b, c)
        v0 = v1[:]
    return v1[m]


def correct(w):
    for i in w:
        if i not in "qwertyuiopasdlfghjkzxcvbnm":
            print("error input")
            return
    word_list=load_word()
    w_soundex=soundex(w)
    sim_list=[]
    for word in word_list:
        if w_soundex == soundex(word):
            sim_list.append(word)
    #print(sim_list)
    minn=10000
    for word in sim_list:
        if minn > levenshtein(w,word):
            minn= levenshtein(w,word)
            most_sim=word
    print(most_sim)

correct("aditonal")