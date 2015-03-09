import string
def main():
    sentence = input("Please enter the sentence:")
    word = input("Please enter the word")

    spliting = sentence.split()

    for word1 in spliting:
        if (word1 == word):
            print (word1)

main()
