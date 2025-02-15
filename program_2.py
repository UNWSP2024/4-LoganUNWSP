#Logan H's Movie Ticket Taker Program

# 1st, keep track of the amount of tickets with this, starting at zero
total = 0

# 2nd, start a loop when movie is true (movie is true to begin with)
movie = True

while movie == True:
#when the movie is true, aka when you start the program or say you want another movie, it'll start with asking the
# name and amount of tickets you want.
    question = input("What movie would you like to see today? ")
    number = int(input("Alright, how many tickets? "))
# with the total from the beginning, you add the number of tickets you just said.
    total = total + number

# then, ask if they want to see another movie, if yes, the loop stays true, looping the loop until you say anything but
# "Y" which will end the loop by making the movie = false.
    answer = input("Want to see another movie today? (Y/N) ")
    if answer == "Y":
        movie = True
    else:
        movie = False

#when the loop is over, it will display the total that it has been keeping track of.
print("Alright, that amount of tickets you bought today are: ", total)
