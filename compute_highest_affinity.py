from time import localtime


def highest_affinity(site_list, user_list, time_list):
  # Returned string pair should be ordered by dictionary order
  # I.e., if the highest affinity pair is "foo" and "bar"
  # return ("bar", "foo").

  siteToUserDict = dict()
  list_of_sites = list()
  mySet = set()

  # create a dictionary with site and all users associated
  for i in range(len(site_list)):
      site = site_list[i]
      user = user_list[i]
      if site in siteToUserDict.keys():
          siteToUserDict[site].add(user)
      else:
          siteToUserDict[site] = set()
          siteToUserDict[site].add(user)

      if (site not in list_of_sites):
          list_of_sites.append(site)

  max = 0
  size = len(list_of_sites)
  site1 = ""
  site2 = ""

  for i in range(0,size):
      for j in range(0, size):
          if i != j:
            set1 = siteToUserDict[list_of_sites[i]]
            set2 = siteToUserDict[list_of_sites[j]]

            intersectionSet =set1.intersection(set2)
            count = len(intersectionSet)

            if count > max:
                max = count
                site1 = list_of_sites[i]
                site2 = list_of_sites[j]


  if site1<site2:
      return (site1, site2)
  return (site2, site1)
  
def addingCode1():
    friends = ['john', 'pat', 'gary', 'michael']
    for i, name in enumerate(friends):
        print "iteration {iteration} is {name}".format(iteration=i, name=name)
		
	parents, babies = (1, 1)
    while babies < 100:
        print 'This generation has {0} babies'.format(babies)
        parents, babies = (babies, parents + babies)
		
	prices = {'apple': 0.40, 'banana': 0.50}
    my_purchase = {
       'apple': 1,
       'banana': 6}
    grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
    print 'I owe the grocer $%.2f' % grocery_bill
	
def addCode2():
    activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting' }

    time_now = localtime()
    hour = time_now.tm_hour

    for activity_time in sorted(activities.keys()):
        if hour < activity_time:
            print activities[activity_time]
            break
        else:
            print 'Unknown, AFK or sleeping!'
			
def addCode3():
    REFRAIN = '''
       %d bottles of beer on the wall,
       %d bottles of beer,
       take one down, pass it around,
       %d bottles of beer on the wall!
    '''
    bottles_of_beer = 99
    while bottles_of_beer > 1:
        print REFRAIN % (bottles_of_beer, bottles_of_beer,
           bottles_of_beer - 1)
        bottles_of_beer -= 1
	
def addCode4():
    REFRAIN1 = '''
       %d bottles of beer on the wall,
       %d bottles of beer,
       take one down, pass it around,
       %d bottles of beer on the wall!
    '''
    bottles_of_beer1 = 199
    while bottles_of_beer1 > 1:
        print REFRAIN1 % (bottles_of_beer1, bottles_of_beer1,
           bottles_of_beer1 - 1)
        bottles_of_beer1 -= 1
		
def addCode5():
    num1 = 1.5
    num2 = 6.3

    # Add two numbers
    sum = float(num1) + float(num2)

    # Display the sum
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
	
def addCode6():
	# Store input numbers
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')

    # Add two numbers
    sum = float(num1) + float(num2)

    # Display the sum
    print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
	
def computeHCF(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            
    return hcf

def addCode7():
    num1 = 54 
    num2 = 24

# take input from the user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

    print("The H.C.F. of", num1,"and", num2,"is", computeHCF(num1, num2))
	
def computeHCF1(x, y):

   # This function implements the Euclidian algorithm to find H.C.F. of two numbers
   while(y):
       x, y = y, x % y

   return x
   

def addCode8():
    num1 = 54 
    num2 = 24

# take input from the user
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

    print("The H.C.F. of", num1,"and", num2,"is", computeHCF1(num1, num2))


	

	
