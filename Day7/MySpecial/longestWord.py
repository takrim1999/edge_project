sentence = "hello world and universe together"
length_list = []
for word in sentence.split():
    length_list.append((len(word),word))
print(sorted(length_list,reverse=True))