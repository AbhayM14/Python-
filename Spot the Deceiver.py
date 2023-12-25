import time

print("""=== Welcome to the game of 'Spot the Deceiver' ===
""")
time.sleep(3)

print("""=== Let's start naming a couple of friends you have ===
""")
time.sleep(3)

friends = input("Who are your friends? (separate with commas). ")

time.sleep(3.3)

friendsQ1 = input("""
From your list of friends, who do you think seems a bit....
Suspicious? """)
print()

##friends = friends.split(",")
if ("Ricardo" in friends or "ricardo" in friends or "Ricky" in friends or "ricky" in friends) and (
        "Ricardo" in friendsQ1 or "ricardo" in friendsQ1 or "Ricky" in friendsQ1 or "ricky" in friendsQ1):

    print("=== Well... ===")
    time.sleep(1.5)
    print()

    print("You have found the Deceiver!!!")
    time.sleep(2.5)
    print()

    print("""=== Job well done, as a matter of fact... ===""")
    time.sleep(1.5)
    print()

    print("""that 'friend' Ricardo is wanted for the following:""")
    time.sleep(2)
    print()

    print("78 Robberies")
    time.sleep(2)
    print()

    print("99 Murders")
    time.sleep(2)
    print()

    print("20 Homicides")
    time.sleep(2)
    print()

    print("39 Vehicular manslaughters")
    time.sleep(2)
    print()

    print("50 Kidnappings")
    time.sleep(2)
    print()

    print("Conspirasy regarding the Jostin edging incident")
    time.sleep(3)
    print()

    print("And is wanted by the United Stated Government as a Domestic terroist.")
    time.sleep(3)
    print()

    print("""Therefore, IT IS HIGHLY ADIVSED THAT YOU AVOID ALL CONTACT WITH RICARDO
  AND LET THE AUTHORITES HANDLE THIS CRIMINAL!!!""")
    time.sleep(4)
    print()

    print("""Thank you for your cooperation,
  United States Deparment of Homeland Security.""")


elif "Ricardo" not in friendsQ1 or "ricardo" not in friendsQ1:

    Reaction = input('Are you sure? Is there someone named Ricardo that you know? ')
    print()
    if Reaction == "Yes" or "yes" in Reaction:
        print("=== It seems that you know someone named Ricardo ===")
        print()
        time.sleep(2.5)

        print("""=== Well I hate to break it to you, but you might be in Danger!!! ===""")
        print()
        time.sleep(3)

        print(""" Ricardo is a criminal that is on the loose!!!""")
        time.sleep(3)
        print()

        print("""He is also wanted for the following > 
    """)

        time.sleep(2)
        print()

        print("78 Robberies")
        time.sleep(2)
        print()

        print("99 Murders")
        time.sleep(2)
        print()

        print("20 Homicides")
        time.sleep(2)
        print()

        print("39 Vehicular manslaughters")
        time.sleep(2)
        print()

        print("50 Kidnappings")
        time.sleep(2)
        print()

        print("Conspirasy regarding the Jostin edging incident")
        time.sleep(3)
        print()

        print("And is wanted by the United Stated Government as a Domestic terroist.")
        time.sleep(3)
        print()

        print("""Therefore, IT IS HIGHLY ADIVSED THAT YOU AVOID ALL CONTACT WITH RICARDO
    AND LET THE AUTHORITES HANDLE THIS CRIMINAL!!!""")
        time.sleep(4)
        print()

        print("""Thank you for your cooperation,
    United States Deparment of Homeland Security.""")








