#This is my Havel Hakimi function which first begins by checking for any empty list. After checking that the list size >= 1,
#The function then checks if there is any negative numbers, or if the list is all 0s. If neither is true, then the function
#continues to iterate through the list until reaching a conclusion. Further logic is explained below.
def Havel_Hakimi(degree_sequence):
  
  #Case 1: There is no degree sequence
  if (len(degree_sequence) < 1):
    return False
  first_value = 0
  
  #Case 2: If the sequence isn't empty, let's start the algorithm
  while (len(degree_sequence) != 0):
    
    #Keep track of the first value in the list to know how many degrees in the sequence to subtract 1 from
    first_value = degree_sequence[0]
    
    #Before doing anything, lets check to see if the list already contains all 0s, which will end the function and return True
    if (check_zeroes(degree_sequence)):
      return True
      
    #Let's also check to see if there are any negative values, because if so, list is not a degree sequence and return False
    if (check_negs(degree_sequence)):
      return False
      
    #Since we already stored the value of the first element, remove the first element
    degree_sequence.pop(0)
    
    #Before iterating through the list and removing values, we first want to make sure the list is long enough to do so
    if (first_value > len(degree_sequence)):
      return False
      
    #Now we want to iterate through the list and subtract (for as many times as the prev first value) subtract 1 from each degree value
    for i in range(first_value):
      degree_sequence[i] -= 1
      
    #Before looping back through and rechecking the list, we sort the list in descending order
    degree_sequence.sort(reverse=True)
    

#Helper function to determine if the list contains all 0s
def check_zeroes(list):
  for item in list:
    if item != 0:
      return False
  return True

#Helper function to determine if the current list contains any negative numbers
def check_negs(list):
  for item in list:
    if item < 0:
      return True
  return False

#My test function which calls all of my test cases
def test_function():
  assert Havel_Hakimi([3,3,2,2,2,2]) == True
  assert Havel_Hakimi([3,3,3,3,3]) == False
  assert Havel_Hakimi([0,0]) == True
  assert Havel_Hakimi([4,3,2,1,1]) == False
  assert Havel_Hakimi([3,3,2,2,0]) == True
  assert Havel_Hakimi([3,3,2,2,1]) == False
  assert Havel_Hakimi([-1,2]) == False
  
test_function()
