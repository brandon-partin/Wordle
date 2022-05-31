import random


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def load_5_letter_words():
    with open('five_letter_words.txt') as word_file:
        valid_5words = list(word_file.read().split())

    return valid_5words



if __name__=='__main__':



#print(str(len(five_words)) + " from len()\n")
#count = 0
#for x in five_words:
#    count += 1
#print(str(count) + " from count\n")
#count = 0
#with open('five_letter_words.txt') as fp:
#    Lines = fp.readlines()
#    for line in Lines:
#        count += 1
#print(str(count) + " from file")
#fp.close()





#english_words = load_words()
#print(len(english_words))
    # demo print
  #  print('farts' in english_words)
#five_letter_words = open("five_letter_words.txt", "w")

#for x in english_words:
    #   print(x)
    #if len(x) == 5:
    #   print(x + "\n")
    #five_letter_words.write(x + "\n")

#five_letter_words.close()




