# Write code to output the arrow pattern shown below, using an if-else statement in combination with a for loop
# You are allowed to use more than one for loop. But use only one for loop if you wish to challenge yourself):

# *
# **
# ***
# ****
# *****
# ****
# ***
# **

for i in range(1, 10):  # i.e. 1 - 9 or nine times
    if i <= 5:   # repeat for each number in range from 1 to 5 and including 5 
        print("*" * i)   # print * the value of i number of times as i iterates up to 5 (print * x 1; * x 2; etc.)
    else:   # when i > 5 (from 6 to 10)
        print("*" * (10 - i))  # print * the value of i number of times subtracted from 10 as i iterates down to to 6