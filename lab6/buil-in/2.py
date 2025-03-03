def count_case_letters(s):
    upper_count = sum(map(str.isupper, s))  
    lower_count = sum(map(str.islower, s))  

    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)

text = input("Enter a string: ")
count_case_letters(text)
