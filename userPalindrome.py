def userPalindrome():
    print("Please provide a palindrome: ")
    string = input()
    string = str(string).lower()
    reverse_str = string[::-1]
    if string == reverse_str:
        print(string + " is a palindrome, congrats!")
    else: 
        print("That's not a palindrome!")