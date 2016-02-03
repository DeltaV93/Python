def first_letter(word):
    print "so the first letter in your password is " + word[0:1].upper()
    
print "tell me your password NOW!"

password = raw_input()

show_letter = first_letter(password)
