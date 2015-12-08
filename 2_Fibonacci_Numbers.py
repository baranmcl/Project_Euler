#Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#find the sum of the even-valued terms.
def fibSum(fibLimit):
  answer = 0
  prevFib = 1
  fibNumbers = [0, 1]
  while fibNumbers[-1] <= fibLimit:
    prevFib = fibNumbers[-1] + fibNumbers[-2]
    fibNumbers.append(prevFib)
  
  for i in fibNumbers:
    if i % 2 == 0:
      answer += i
  
  return answer


if __name__ == '__main__':
  print(fibSum(4000000))
