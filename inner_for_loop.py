# hence prove that for loop execute one time and then inner loop execute many time in each iteration .
for i in range(5):
    for j in range(3):
        print(f'i is {i} and j is {j}')


word = "Hello"

for i in range(len(word)):
    for j in word[i:]:
        print(f"i: {i}, j: {j}")

