num = int(input("Enter a number "))
temp = num
count = 0
while temp>0:
  temp = temp//10
  count+=1
print("Number of digits :",count)
temp = num
total =0
while temp>0:
  digit = temp%10
  total+=digit**count
  temp = temp//10
if total==num:
  print(num,"is an armstrong number")
else:
  print(num,"is not an armstrong number")