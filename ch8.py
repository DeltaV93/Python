#num = raw_input("pick a number: " )
#num = int(num)

#if num < 10:
#    print  "is  less than 10"
#elif num > 10:
#    print  "is greater than 10"
#else:
#    print  " is the same as  10"

user_word = raw_input("Type in a word: ")

if len(user_word) < 5:
    print "it has less than 5 letters"
elif len(user_word) > 5:
    print "it has more than 5 letters"
else:
    print "it has excatly 5 letters" 
    
