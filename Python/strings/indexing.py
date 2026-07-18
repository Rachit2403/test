#indexing = accessing the specified/restricted contents of a sequence using []
# [start : end : step]
#The 'end' digit is exclusive.
cred_num = input("Enter your card number: ")
true_num = cred_num.replace("-", "")
#print(true_num [0 : 5]) = gives the first 4 digits
#print(true_num [0 : : 2]) = gives every 2nd digit
#print(true_num [4 : : -1]) = gives digits in the reverse order from the 4th digit.
#print(true_num [-4 : ]) = gives the last 4 digits.
#Negative indexes reverse the order.