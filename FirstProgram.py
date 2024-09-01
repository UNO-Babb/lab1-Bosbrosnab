#FirstProgram.py
#Name: Alex Bowes
#Date: 9/1/24
#Assignment: Lab 1

def main():
  print("First Program")
  #Say hello
  print("hello")
  #Ask for the user's name
  name = input("Put your name here: ")
  #Use the user's name in the program.
  print("hello", name)
  #Ask the user for their age.
  age = int(input("Put your age here: "))
  #Tell the user what year they were born in.
  print("you were born in", 2024-age)
  #Assume that they have not had their birthday yet this year.


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()

