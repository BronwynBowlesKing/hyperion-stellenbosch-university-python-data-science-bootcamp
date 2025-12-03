# Write a program that displays a logical error 

# This program prints a false conclusion because it is based on a comparison of raw data and percentages, which should not be compared in this way

num_boys = 29
num_girls = 27
num_other = 1

total_students = num_boys + num_girls + num_other

percent_boys = round(num_boys / total_students * 100)
percent_girls = round(num_girls / total_students * 100)
percent_other = round(num_other / total_students * 100)

print(f'The number of boys in the class is',  num_boys, 'but there are', percent_girls, 'girls and', percent_other,'are neither. So there are more girls than boys and others in the class.')

# percent_girls and percent_other should be changed to num_girls and num_other. The statement should read that there "are more boys than girls and others in the class". Rounding off the percentages also means that the statement says there are two non-binary people, but there is in fact one. 

# A new print() statement is needed to present the percentages accurately, such as:

print(f'The percentage of boys in the class is',  percent_boys, '%, there are', percent_girls, '% girls, and', percent_other,'% are neither. So there are more boys than girls and others in the class.')