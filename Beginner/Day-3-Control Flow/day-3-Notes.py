print("Welcome to the Rollercoaster")
height = int(input("What is your height in cm? "))

if height >120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <12:
        bill=5
        print("Child tickets are $5")
    elif age <=18:
        bill=7
        print("Youth tickets are $7")
    elif age>=45 and age<=55:
        bill=0
        print("Have a free ride on us!")
    else:
        bill=12
        print("Adult tickets are $12")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == 'Y':
        bill+=3
    
    print(f"Your total bill is ${bill}")
else:
    print("Sorry, height must be above 120cm")
    
    
#------------------------------------------------

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