t = int(input())

def convert(s):
  answer = []
  stack = []
  for c in s:
    if 'a' <= c <= 'z':
      answer.append(c)
    elif c in '(+-*/^':
      stack.append(c)
    else:
      while stack[-1] != '(':
        answer.append(stack.pop())
      stack.pop()
  return answer















# def convert2(s):
#   k = 0
#   stack = []
#   res = []
#   for k in range(len(s)):
#     if s[k] == '(':
#       stack.append(s[k])
#     elif 'a' <= s[k] <= 'z':
#       res.append(s[k])
#     elif s[k] in "+-*/^":
#       stack.append(s[k])
#     elif s[k] == ')':
#       while stack[-1] != '(':
#         res.append(stack.pop())
#       stack.pop()
#   return res

# def convert(s):
#   k = 0
#   stack = []
#   while k <= len(s) - 1:
#     if s[k] == '(':
#       k += 1
#     elif 'a' <= s[k] <= 'z':
#       stack.append(s[k])
#       k += 1
#     else:
#       opening = 0
#       ss = ''
#       j = k
#       while True:
#         j += 1
#         if s[j] == ')':
#           opening -= 1
#         elif s[j] == '(':
#           opening += 1
        
#         if s[j] == ')' and opening == -1:
#           break
#         ss += s[j] 


#       stack.extend(convert(ss))
#       stack.append(s[k])
#       k = j + 1

#   return stack

for _ in range(t):
  s = input()
  print(''.join(convert(s)))

# print(convert(s))
# print(convert('((a+b)*(z+x))'))
# print(convert('((a+t)*((b+(a+c))^(c+d)))'))

