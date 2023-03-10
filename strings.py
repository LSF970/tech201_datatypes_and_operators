# Strings

# Single_quotes = 'Look! single quotes'
# Double_quotes = "Look! double quotes"
#
# print(Single_quotes)
# print(Double_quotes)
#
# # string_failure = 'I said 'Wow!''
#
# escape_example = 'I said \'Wow\''
# print(escape_example)
# quote_in_quote = 'I said "Wow!"'
# print(quote_in_quote)
#
#
# reverse_quote = "I said 'Wow!'"
# print(reverse_quote)

# String slicing

# Everything in code starts with 0 not 1
# H e l l o   W o r l d  !
# 0 1 2 3 4 5 6 7 8 9 10 11
#
# Hw = "Hello world!"
#
# print(Hw[7:]) # orld!
# print(Hw[-5:]) # orld!
# print(Hw[:5]) # Hello
# print(Hw[0:5]) # Hello
#
# # String methods
#
# # strip()
#
# white_space = "lot's of space at the end                                             "
# print(len(white_space)) # 70
# print(len(white_space.strip())) # 25
#
# # A few more
#
# example_text = "here's some text with lot's of text"
#
# # Count a substring within a string
# print(example_text.count("text")) # 2
#
# # Make everything lowercase
# print(example_text.lower())
#
# # Make everything uppercase
# print(example_text.upper())
#
# # Capitalise things
# print(example_text.capitalize())
#
# # Replace characters/text
# print(example_text.replace("with" , ","))
#
# # Concatenation
#
# a = "here "
# b = "more "
# c = "much more"
#
# print(a + b + c)
#
# # Casting
#
x = 2
y = 5.4
z = " there's a number 25.4 unless we put a space!"
#
# # print(x + y + z)
#
print(str(x) + ", " + str(y) + z)
#
# # string to numeric
#
# int_string = "6"
#
# print(float(int_string))
# print(type(float(int_string)))

# F-strings

# name = "Lassie"
# years = 7
# height_cm = 60.2
#
# print(f"{name} is {years} years old and {height_cm}cm tall")

# F-strings allow us to use methods/evaulations too

name = "Snoopy"
years = 52

print(f"{name.upper()} IS {years * 7} YEARS OLD IN DOG YEARS!!!!")

# F-strings to specify precsion in rounding and decimals

pi = 3.14159265359

print(f"Pi to 3 decimal places: {pi:.3f}") # Pi to 3 decimal places
print(f"Pi to 3 decimal places: {pi:.5f}") # Pi to 5 decimal places

score = 16
max_score = 26

print(f"You scored {score/max_score}") # 0.6153846153846154
print(f"You scored {score/max_score:%}") # 61.538462%
print(f"You scored {score/max_score:.2%}") # 61.54%
print(f"You scored {score/max_score:.0%}")

