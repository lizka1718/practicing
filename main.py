def func(a):
    if len(a) <= 1:
        return a
    else:
        return a[-1] + func(a[:-1])
    
text = "abc"
print(func(text))


print("hello world")
