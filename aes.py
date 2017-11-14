import secrets

def genKey(k):
    randomKey = []
    for i in range(0, k):
        temp = secrets.randbits(8)
        randomKey.append(temp)
    #print(sorted(randomKey), len(randomKey))

def main():
    genKey(16)
    #print(x)
if __name__ == '__main__':
    main()