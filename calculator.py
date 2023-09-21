import operator # A module of functions that work like standard operators.

# A table of symbols to operator functions. 
op = {'+':operator.add,
      '-':operator.sub,
      '*':operator.mul,
      '/':operator.truediv}

# Make sure to convert the input to integers.
# No error handling here.  Consider if someone doesn't type the correct input.
# This is why eval() is bad.  Someone could type a command to delete your hard disk.  Sanitize inputs!
# In the below cases you will get an exception if a non-integer or
# invalid symbol is entered.  You can use try/except to handle errors.
num1 = int(input('Input 1st number: '))
method = op[input('Input symbol(+,-,*,/):')]
num2 = int(input('Input 2nd number: '))

ans = method(num1,num2)

print('Answer is ', ans)
