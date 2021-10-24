# //Google Question
# //Given an array = [2,5,1,2,3,5,1,2,4]:
# //It should return 2

# //Given an array = [2,1,1,2,3,5,1,2,4]:
# //It should return 1

# //Given an array = [2,3,4,5]:
# //It should return undefined


# function firstRecurringCharacter(input) 
# }

# //Bonus... What if we had this:
# // [2,5,5,2,3,5,1,2,4]
# // return 5 because the pairs are before 2,2

def first_recurring_character(input):
  if len(input) == 0 or len(input)== 1:
    return "None"
  collector = {}
  for i in range(len(input)):
    if collector.get(input[i]):
      return input[i]
    collector[input[i]] = True
  return "None"

print(first_recurring_character([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))