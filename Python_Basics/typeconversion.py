# explicit type conversion
a="10"
print(type(a))
b=int(a)
print(type(b))

# Implicit type casting
s="Hello"
print(type(s))
s=int(s)
print(type(s))


# coercion type casting

# String to Integer
num_str = "42"
num_int = int(num_str)   # converts string "42" → integer 42
print(num_int, type(num_int))   # Output: 42 <class 'int'>

# String to Float
num_str2 = "3.14"
num_float = float(num_str2)   # converts string "3.14" → float 3.14
print(num_float, type(num_float))   # Output: 3.14 <class 'float'>

# Integer to String
num = 100
num_str3 = str(num)   # converts integer 100 → string "100"
print(num_str3, type(num_str3))   # Output: "100" <class 'str'>

# Boolean to Integer
flag = True
flag_int = int(flag)   # True → 1, False → 0
print(flag_int, type(flag_int))   # Output: 1 <class 'int'>

# Integer to Boolean
zero = 0
non_zero = 5
print(bool(zero))      # Output: False
print(bool(non_zero))  # Output: True

# Float to Integer (truncates decimal part)
pi = 3.99
pi_int = int(pi)   # 3.99 → 3
print(pi_int, type(pi_int))   # Output: 3 <class 'int'>
