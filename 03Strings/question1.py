# Take a sentence as input and reverse each word but keep the word order the same.

sentence = input("Enter a sentence: ")
words = sentence.split()  # Split the sentence into words
reversed_words = [word[::-1] for word in words]  # Reverse each word
output = ' '.join(reversed_words)  # Join the reversed words back into a sentence
print(output)