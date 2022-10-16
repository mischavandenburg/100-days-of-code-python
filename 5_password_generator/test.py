import random
 
# initializing list
test_list = [1, 4, 5, 6, 3]
 
# Printing original list
print ("The original list is : " + str(test_list))
 
# using random.shuffle()
# to shuffle a list
random.shuffle(test_list)
 
# Printing shuffled list
print ("The shuffled list is : " +  str(test_list))
