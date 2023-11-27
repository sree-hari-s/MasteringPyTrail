# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
phonebook = {}
for i in range(n):
    line = input().split()
    phonebook[line[0]] = phonebook.get(line[0],line[1])

while True:
    try:
        q = input()
        if q in phonebook:
            print(f"{str(q)}={str(phonebook[q])}")
        else:
            print("Not found")
    except:
        break
