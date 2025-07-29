def checkPalindrome(userText):
    # Reverse the input string using slicing [start:stop:step]
    reverse = userText[::-1]
    
    # Compare the reversed string with the original
    if reverse == userText:
        print("It's a Palindrome!")
    else:
        print("It's not a Palindrome!")
        
# Take input from the user, convert to lowercase, and remove leading/trailing spaces
userinput = input("Enter a sentence or word: ").lower().strip()

# Call the function with the user input
checkPalindrome(userinput)
