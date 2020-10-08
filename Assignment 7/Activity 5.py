# this will display the results as human years for a dogs age


def display_results (dog_years):
  print (str("your dogs age in dog years is ") +str (dog_years))


def get_dog_years():
  print("What is the age of your dog in human years?")
  dog_years = int(input())
  return dog_years


def get_name():
  print("What is yours dogs name?:")
  name = input()
  return name



def get_choice():
  print ("Entering 1-2 will display yours dogs age as either 10.5 or 21, but entering a number larger than 2 will consider the differnce and display anew calculated answer.")
  choice = input()
  return choice


def calculate_dog_years(dog_years): 
  dog_years = dog_years - 2
  dog_years = (dog_years * 2) + 21
  return dog_years  


# Main
def main():
  dog_years = get_dog_years()
  name = get_name()
  choice = get_choice()
  dog_years = calculate_dog_years(dog_years)
  if choice == 1:
    print("your dogs age in dog years is 10.5 years!")
  elif choice == 2:
    print("your dogs age in dog years in 21 years!")
  elif dog_years > 2:
    dog_years = calculate_dog_years(dog_years)
  
  display_results (dog_years) 
  


main()
