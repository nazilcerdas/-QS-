# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
# print(reminder)

# i = 10

# def f(arg=i):
#     print(arg)
# f(56)

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))









