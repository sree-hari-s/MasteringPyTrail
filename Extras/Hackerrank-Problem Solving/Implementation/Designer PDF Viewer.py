import os


def designerPdfViewer(h, word):
    maximum = 0
    for i in range(len(word)):
        if maximum < h[ord(word[i]) - 97]:
            maximum = h[ord(word[i]) - 97]
    return maximum * len(word)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + "\n")

    fptr.close()
