import random
print("The game will start in some time but first you need to make some important choice")
print("Following is a menu as to how would you prefer entering your choice in the game while playing")
print("Enter 1 if you want to enter numbers to tell us about your choice (here 1 will represent rock, 2 will represent paper and 3 will represent scissors ")
print("Enter 2 if you want to enter only the first letter of the words as your choice, you need not worry about whether it is capital or small letters")
print("Enter 3 if you wamt to enter the complete words (keelp in mind that only max of 2 errors in the spelling will be accpeted)")
choice = input("Enter your choice : ")
arr = ['rock','paper','scissors']
if len(choice) != 1 or (ord(choice)!= 49 and ord(choice)!=50 and ord(choice)!=51) :
  print("INVALID CHOICE : you need to rerun the program as you entered an invalid value ")
elif ord(choice)== 49 :
  print("Accepted Representation : 1=Rock, 2=Paper, 3=Scissors")
  answer = input("Enter your answer if you want rock paper or scissors based on numbering : ")
  if len(answer) != 1 or (ord(answer)!=49 and ord(answer)!=50 and ord(answer)!=51 ) :
    print("Invalid entry : You've entered a value which was not an actual representation")
  else :
    answer = int(answer)
    #ca = computer choice
    ca = random.randint(1,3)
    compans = arr[ca-1]
    userans = arr[answer - 1]
    print("You chose",userans)
    print("Computer chose",compans)
    if (ca==1  and answer ==2) or (ca == 2 and answer == 3) or (ca ==3 and answer ==1) :
      print("You  won!! congratualation!!")
    elif (ca==answer) :
      print("It was a tie...")
    else :
      print("The computer won!! Better luck next time!!")
elif ord(choice)== 50 :
  print("Acceptable representations :  r or R for rock, p or P for paper and s or S for scissors ")
  #a = user answer
  a = input("Enter your choice based on the accpetable representation provided to you : ")
  if len(a)!=1 or (ord(a)!=114 and ord(a)!=112 and ord(a)!=115 and ord(a)!=83 and ord(a)!=80 and ord(a)!=82) :
    print("Invalid entry : You've entered a value which was not an actual representation")
  else :
    a=a.lower()
    ca = random.randint(1,3)
    compans = arr[ca-1]
    if ord(a) == 114 :
      userans = 'rock'
      na = 1
    elif ord(a) == 112 :
      userans = 'paper'
      na = 2
    else :
      userans = 'scissors'
      na = 3
    print("You chose",userans)
    print("Computer chose",compans)
    if (ca==1  and na ==2) or (ca == 2 and na == 3) or (ca ==3 and na ==1) :
      print("You  won!! congratualation!!")
    elif (ca==na) :
      print("It was a tie...")
    else :
      print("The computer won!! Better luck next time!!")
else :
  print("Acceptable Representation : Rock, Paper and Scissors (whether characters are lower or upper case is not a problem)")
  ans = input("Enter your answer : ")
  ans = ans.lower()
  if ans in arr :
    ca = random.randint(1,3)
    compans = arr[ca-1]
    print("You chose",ans)
    print("Computer chose",compans)
    ua = arr.index(ans) + 1
    if (ca==1 and ua ==2) or (ca == 2 and ua == 3) or (ca ==3 and ua ==1) :
      print("You  won!! congratualation!!")
    elif (ca==ua) :
      print("It was a tie...")
    else :
      print("The computer won!! Better luck next time!!")
  else :
    print("Invalid entry : The value you entered is not an acceptable representation")
