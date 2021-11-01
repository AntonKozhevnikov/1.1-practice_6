word1 = input('1st word: ')
word2 = input('2nd word: ')
def is_anagram(word1, word2):
    a=word1.replace(' ','')
    b=a.lower()
    word1 = sorted(b)
    i=word2.replace(' ','')
    j=i.lower()
    word2 = sorted(j)
    if word1 == word2:
        print("Слова являются анаграмами")
    else:
        print("Слова не являются анаграмами")
is_anagram(word1, word2)
