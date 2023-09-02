# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()

count_T=(name1_lower+name2_lower).count("t")
count_R=(name1_lower+name2_lower).count("r")
count_U=(name1_lower+name2_lower).count("u")
count_E=(name1_lower+name2_lower).count("e")

count_True = count_T+ count_R+ count_U+count_E

count_L=(name1_lower+name2_lower).count("l")
count_O=(name1_lower+name2_lower).count("o")
count_V=(name1_lower+name2_lower).count("v")
count_E=(name1_lower+name2_lower).count("e")

count_LOVE = count_L+ count_O+ count_V+ count_E

score_str = str(count_True)+str(count_LOVE)
score = int(score_str)
if score<10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")