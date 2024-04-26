while True :
  x = input("Enter your factorial number:\n")
  if x == "exit" :
    break
  def factorial_finder(n):
    if(n==1 or n==0):
      return 1
    return factorial_finder(n-1) * n
  def factorial_traling_zero(number):
    count=0
    i=5
    while (number//i != 0):
      count += int(number/i)
      i *= 5
      return count
  try:
    x = int(x)
    print(f"{x}! = {factorial_finder(x)}")
    print(f"{factorial_traling_zero(x)} zeros in the factorial.")
  except:
    print("Please enter a number or a small number!!")
