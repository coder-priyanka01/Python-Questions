# Take a sentence as input and count the frequency of each word.
s = input("Enter a sentence: ")
words = s.split()  # Split the sentence into words
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1  

for k, v in freq.items():
    print(k, ":", v)