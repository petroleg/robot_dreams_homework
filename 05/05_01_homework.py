user_input = input("Enter something: ")
for element in user_input:
 if element.isdigit():
     if int(element) % 2 == 0:
         print(f'The number "{element}" is even.')
     else:
         print(f'The number "{element}" is odd.')
 elif element.isalpha():
     if element.isupper():
         print(f'The letter "{element}" is capital.')
     else:
         print(f'The letter "{element}" isn\'t capital.')
 else:
     print(f'"{element}" is a symbol')