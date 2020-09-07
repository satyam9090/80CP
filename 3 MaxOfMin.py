arr = [10, 20, 30, 50, 10, 70, 30]

n = len(arr)

left = [-1]*(n+1)
right = [n]*(n+1)

stack = []
for i in range(n):
  while(len(stack) != 0 and arr[stack[-1]] >= arr[i]):
    stack.pop()
  
  if(len(stack) != 0):
    left[i] = stack[-1]
  
  stack.append(i)

stack = []
for i in range(n-1,-1,-1):
  while(len(stack) != 0 and arr[stack[-1]] >= arr[i]):
    stack.pop()
  
  if(len(stack) != 0):
    right[i] = stack[-1]
  
  stack.append(i)

lenArray = [0]*(n+1)
for i in range(n):
  lenArray[right[i] - left[i] - 1] = max(arr[i], lenArray[right[i] - left[i] - 1])

for i in range(n-1, 0, -1):
  lenArray[i] = max(lenArray[i], lenArray[i+1])

print(lenArray)
