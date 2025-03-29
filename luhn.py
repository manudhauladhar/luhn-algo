#Python comes with built-in classes that can help us with string manipulation. One of them is the str class. It has a method called maketrans that can help us create a translation table. This table can be used to replace characters in a string:
#Example Code
#str.maketrans({'t': 'c', 'l': 'b'})
#The above, when called on a string, will replace all t characters with c and all l characters with b.
#Create a variable called card_translation and assign it a translation table to replace all - and   characters with an empty string.
#The Luhn algorithm is as follows:
#From the right to left, double the value of every second digit; if the product is greater than 9, sum the digits of the products.
#Take the sum of all the digits.
#If the sum of all the digits is a multiple of 10, then the number is valid; else it is not valid.
#Assume an example of an account number "7992739871" that will have a check digit added, making it of the form 7992739871x:
#Example Code
#Account number      7   9  9  2  7  3  9   8  7  1  x
#Double every other  7  18  9  4  7  6  9  16  7  2  x
#Sum 2-char digits   7   9  9  4  7  6  9   7  7  2  x
#Replace the pass statement with a variable sum_of_odd_digits and a value of 0.


def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    print(card_number_reversed)
    odd_digits = card_number_reversed[::2]
    print(odd_digits)
    
def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    print(translated_card_number)

    verify_card_number(translated_card_number)

main()
    
#Defining the translation does not in itself translate the string. The translate method must be called on the string to be translated with the translation table as an argument:
#Example Code
#my_string = "tamperlot"
#translation_table = str.maketrans({'t': 'c', 'l': 'b'})
#translated_string = my_string.translate(translation_table)
#Create a variable called translated_card_number and assign it the result of calling the translate method on card_number with card_translation as an argument.    
#Reverse the order of the digits in the last four digits of card_number, by using a slice with a step of -1. You can use either negative or positive indices for the start and end indices.
#Within the verify_card_number function, create a variable odd_digits that contains every other digit of the card_number_reversed string.