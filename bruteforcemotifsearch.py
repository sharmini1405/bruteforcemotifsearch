import itertools

DNA = ["tagtggtcttttgagtgtagatccgaagggaaagtatttccaccagttcggggtcacccagcagggcagggtgacttaat",
       "cgcgactcggcgctcacagttatcgcacgtttagaccaaaacggagttagatccgaaactggagtttaatcggagtcctt",
       "gttacttgtgagcctggttagatccgaaatataattgttggctgcatagcggagctgacatacgagtaggggaaatgcgt"
       ]

t = 3
l = 8
n = 80

def score(s, DNA):
    pattern = ['a', 'c', 'g', 't']
    myArr = []
    k = 0
    for d in DNA:
        temp = []
        for w in d[s[k]:s[k] + l]:
            temp.append(w)

        k += 1
        myArr.append(temp)


    countMatrix=calculateProfile(myArr,pattern)
    x = 0
    maxScore = 0
    while x < l:
        y = 0
        maximum = 0
        while y < len(countMatrix):
            if countMatrix[y][x] > maximum:
                maximum = countMatrix[y][x]
            y += 1
        maxScore += maximum
        x += 1
    return maxScore

def calculateProfile(myArr,pattern):
    countMatrix = []

    ii = 0
    i=0
    while ii < len(pattern):
        jj = 0
        tempCountMatrix = []
        while jj < l:
            tempCountMatrix.append(0)
            jj += 1
        countMatrix.append(tempCountMatrix)
        ii += 1
    while i < len(pattern):
        j = 0
        while j < l:
            k = 0
            while k < t:
                if pattern[i] == myArr[k][j]:
                    countMatrix[i][j] += 1
                k += 1
            j += 1
        i += 1
    return countMatrix

def bruteForceSearch(DNA, t, n, l):
    permutation = itertools.product(range(n - l), repeat=t)
    bestScore = 0
    bestMotif = []
    print("Calculating...")
    for s in permutation:
        scoreValue = score(s, DNA)
        if scoreValue > bestScore:
            bestMotif = s
            bestScore = scoreValue
    print("Finished")
    print("Best Score: ", bestScore)
    print("Best Motif: ", bestMotif)

    return bestMotif


bruteForceSearch(DNA, t, n, l)
