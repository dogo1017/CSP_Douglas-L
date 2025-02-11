# Douglas London, strings notes python

# a data point that holds info sourrounded by quotationmarks

sentence = "The quick brown fox jumps over the lazy dog"

#name = input("hello, what is your name: ").strip().capitalize()

#print(f"Hello {name}")

#print("hello " + name)


#print(len(sentence))
#print(sentence[4])
start = print sentence.find("brown")
length = len("brown fox")
print(sentence[start:start+length]