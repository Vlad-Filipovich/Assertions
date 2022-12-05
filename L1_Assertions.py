# Testing is writing the test code that checks bugs in our code

# assert 2 + 2 == 4
# assert 2 + 2 == 5, '2 + 4 must equals 4'

# def divide(a, b):
#     assert b != 0, 'b must not equals zero'
#     return a / b
#
#
# print(divide(2, 0))

# def multiply_positive_numbers(a, b):
#     assert a > 0 and b > 0, 'a and b must be positive'
#     print(a * b)
#
#
# multiply_positive_numbers(2, 2)

def get_access(password):
    password_list = [111, 123, 321,]
    assert int(password) in password_list, 'Password is invalid'
    print('You can dangerous stuff!')


password_1 = input('Please input the password: ')
get_access(password_1)
