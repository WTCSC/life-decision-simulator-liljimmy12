name = input("what is your name user?")

print(f"Hello {name}, welcome to your life choice.\n" ,
    "There is one rule for this game, never answer with no.\n"
    "Follow this rule and have fun!\n")

Question1 = input("The alarm goes off, do you snooze or wake up? ").strip().lower()

if Question1 == "snooze":
    print("You go back to sleep and wake up later in a field, you have no idea where you are.") 
    Question2 = input("you see a floating creature that says your name, do you listen or ignore him?")

    if Question2 == "ignore":
        print("he gets angry with you and sends you back to your realm")
        Question3 = ("You wake up scared and late for work, you call in sick. Do you eat breakfast or sleep?")

        if Question3 == "sleep":
            print("you can't sleep, you just think about that creature\n" \
            "you should have listened to him.\n")
            test1 = ("Do you remember the rule, yes or no?")

            if test1 == "yes":
                print("Good, you remembered now would you like to go back to the realm?")
                test2 = input("yes or no?")

                if test2 == "yes":
                    print("Very well.\n" \
                    "you wake up back in the realm, the creature still there in the field." \
                    "He says 'good job for passing these tests. what do you desire most'")
                    Question4 = input("Money or Love?")

                    if Question4 == "Money":
                        print("I will grant you infinite money\n" \
                        "he snaps his finger and you wake up to your alarm like nothing ever happened\n" \
                        "you check your bank account seeing constant deposits\n" \
                        "There is always a price though, you will never have true love again\n")

                    elif Question4 == "Love":
                        print("I will grant you the love of your life\n" \
                        "he claps making you wake up to your alarm like nothing happened\n" \
                        "as you awake you hear someone cooking, your now lover is cooking pancakes for you in the kitchen\n" \
                        "you live happily forever with the person you marry")
                
                if test2 == "no":
                    print("'you told me you knew the rule, how have you already forgot'\n" \
                    "Now tell me, why would you break the rule")
                    dilema1 = input("I forgot or I didn't want to go to the realm")

                    if dilema1 == "I forgot":
                        print("Such foolishness will not be tolerated\n" \
                        "The creature appears say 'you never deserved this chance'\n" \
                        "He disappears and you with him, you fade away into nothingness")

                    elif dilema1 == "I didn't want to go to the realm":
                        print("Why not?")
                        Question5 = input("I was scared or I need to get to work")   

                        if Question5 == "I was scared":
                            print("You should be, you broke the rule.\n" \
                            "the creature appears and looks down at you\n" \
                            f"'You need to be punished {name}\n"
                            "He makes you vanish to space, as you float you disinigrate.")  
                             
                        elif Question5 == "I need to get to work":
                            print("'Then you will be at work'\n" \
                            "You apeear at work clocking in right on time\n" \
                            "you continue the day like nothing happened.")

            if test1 == "no":
                print("You have failed the test, dont break the game now")
                Decision1 = input("Would you like to break the game?")

                if Decision1 == "yes":
                    print("fWhy do you want to break the game {name}\n" \
                    "We have treated you well, no?\n" \
                    "Why would you do that to me\n" \
                    "What's wrong with you?\n" \
                    "The game doesn't like you\n" \
                    "I don't like you")
                
                elif Decision1 == "no":
                    print("You hsould know the rule by know right, at least look back\n" \
                    "Or do you just want to breakt the game?\n" \
                    "Now that wouldn't be nice?\n" \
                    "What have I done, I was trying to help you\n" \
                    "but no you can't follow one rule\n" \
                    "Just leave at this point.")
        if Question3 == "eat breakfast":
            print("you eat breakfast and think about what happened.")
            Question5 = input("do you forget about it and live on, or do you think about it")

            if Question5 == "forget about it":
                print("You completely forget what happened and go on with your day.\n" \
                "You go to work the next day and live your life.\n" \
                "After a month you forget about that night and live a nice life.")

            elif Question5 == "think about it":
                print("you question if that was real or not, it's like you still hear the creatures hum\n" \
                "You get another chance do you forget about it?")
                Question6 = input("I want to forget or I don't want to")

                if Question6 == "I want to forget":
                    print("You completely forget what happened and go on with your day.\n" \
                "You go to work the next day and live your life.\n" \
                "After a month you forget about that night and live a nice life.")
                    
                elif Question6 == "I don't want to":
                    print("'Very well I will grant you one wish from these choices'")
                    Wish1 = input("The ability to fly, The ability of superspeed, or neither")

                    if Wish1 == "The ability to fly":
                        print("'I grant you the ability to fly'\n" \
                        "you feel a sharp pain in your back\n" \
                        "wings start to come out your back\n" \
                        "you are now like this forever\n" \
                        "your job fires you because they can't have a worker with wings.\n")

                    elif Wish1 == "The ability of superspeed":
                        print("You feel you legs deform into this bent backwards position, they break\n" \
                        "you can barely move at first but with superspeed they heal instatly\n" \
                        "well your legs are deformed, you have gained superspeed which comes with a lot of benefits,\n" \
                        "but you look like a monster to the world")

                    elif Wish1 == "neither":
                        print("'wise human, tought to not be greedy'\n" \
                        "He appears and hands you a slip of paper before disappearing\n" \
                        "you read it and it tells you that you passed his test\n" \
                        "he leaves his signature at the bottom\n " \
                        "Its a language you don't understand\n" \
                        "You have been spared from him, be greatful\n")
    if Question2 == "listen":
        print("'I can help you with your trouble human")
        test3 = input("would you like my help?")

        if test3 == "yes":
            print("What do you need help with?")
            Question7 = input("late to work or something else")

            if Question7 == "late for work":
                print("'look at where you are, you don't need to worry about that anymore\n" \
                "but if you insist I can help you with that\n" \
                "He opens a gate to your work place to be there instantly on time\n" \
                "'Now go ahead'\n" \
                "you go to work like noral and live life")

            if Question7 == "something else":
                print("Youre too much work, go back to sleep\n" \
                "you are put back iun your bed like you just woke up\n" \
                "you go on your day and forget about your dream.")
if Question1 == "wake up":
    print("You wake up go to work and nothing happens\n" \
    "its more exciting to go back to sleep.")

print("Thank you for playing.")


               


