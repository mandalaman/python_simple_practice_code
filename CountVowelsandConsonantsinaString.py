a = input("Enter the name: ")
vowel = 0
consonant = 0

for i in range(0, len(a)):
    if(a[i] != ' '):
        if(a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' or a[i]=='A' or a[i]=='E' or a[i]=='I' or a[i]=='O' or a[i]=='U'):
            vowel =vowel+1
        else:
            consonant = consonant+1
total_word = vowel+consonant

print("vowel count: ", vowel)
print("consonant: ", consonant)
print("total word: ", total_word)


###################################################################################

from random import randint

random_number = randint(1, 100)

print(random_number)

def count_vowels_consonants(s):
    vowels = "AEIOUaeiou"
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = len(s) - vowel_count
    return vowel_count, consonant_count

text = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(text)
print(f"Vowels: {vowels}, Consonants: {consonants}")
