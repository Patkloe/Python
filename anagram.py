def isAnagram(str1, str2):
    str1_list = list(str1) # define a list on the first argument
    str1_list.sort()    # sort the list
    str2_list = list(str2) # define a list on the second argument
    str2_list.sort()    # sort the list
    print(str1_list)
    return (str1_list == str2_list)  # return comparison of two list
    
print(isAnagram("paypal1","palpy1"))
val = "Decouvrir un travail"
val_list = list(val)
#print(str1_list)
