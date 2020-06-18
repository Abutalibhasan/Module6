"""
This function receives two parameters string parameter(str) and integer(n) and print str n times.
"""
def multiply_string(str,num):
  if num > 1 and num <9:
    return str * num
if __name__ == '__main__':
    print(multiply_string("***", 6))

