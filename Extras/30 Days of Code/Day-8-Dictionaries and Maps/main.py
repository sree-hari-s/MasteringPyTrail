# Input the number of entries in the phonebook
n = int(input())

# Initialize an empty dictionary to store phonebook entries
phonebook = {}

# Input phonebook entries
for _ in range(n):
    entry = input().split()
    name, phone_number = entry[0], entry[1]
    phonebook[name] = phone_number

while True:
    try:
        query_name = input()
        if query_name in phonebook:
            print(f"{query_name}={phonebook[query_name]}")
        else:
            print("Not found")
    except EOFError:
        break
