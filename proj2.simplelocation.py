from math import hypot

# Initialising the city of GRIDBOURNE
GRIDBOURNE = []
letter = list(map(chr, range(65, 75)))
number = list(num for num in range(1, 11))
for i in letter:
    row = []
    for j in number:
        row.append('{}{}'.format(i, j))
    GRIDBOURNE.append(row)

def cord_of_restraunts(x, y):
    ''' Takes input x,y coordintaes of users location, finds the coordinates of
   restraunts in neighbourhood returning list float coordinates(HELPER FUNC)'''

    cr_rest_cord = [float((str(abs(x)))[0]), float((str(abs(y)))[0])]
    mr_rest_cord = [float((str(abs(x)))[0] + '.5'),
                    float((str(abs(y)))[0] + '.5')]

    return [cr_rest_cord, mr_rest_cord]

def dist_rest(x, y, a, b):
    ''' Takes user location (a, b) and neighbourhood to be tested:(x, y) and
    finds user distance restraunts returning a list (HELPER FUNC)'''

    # Finding coordinates of the middle and corner restraunts in neighbourhood
    rest_cord = cord_of_restraunts(x, y)

    # Finding user location with origin as CR followed by origin as MR
    relative_xcr = a - rest_cord[0][0]
    relative_ycr = b - rest_cord[0][1]
    relative_xmr = a - rest_cord[1][0]
    relative_ymr = b - rest_cord[1][1]

    # Assuming CR,MR cords as origin to calculate eucl distance using hypot
    dist_cr = hypot(relative_xcr, relative_ycr)
    dist_mr = hypot(relative_xmr, relative_ymr)

    return [dist_cr, dist_mr]

def find_my_neighbourhood(x, y):
    ''' Takes an x and y coordinate as input to find the location of user in
    terms of neighbourhood returning a list'''

    #  Checking row and column user is located in and assigning respectively
    y = str(abs(y))
    x = str(abs(x))
    col = (int(x[0]))
    row = (int(y[0]))

    return GRIDBOURNE[row][col]

def find_all_restaurants_in_neighbourhood(x, y):
    ''' Calls find_my_neighbourhood to check location of user and returns the 2
    restraunts in acsending alphabetical order as a list'''

    nhood = find_my_neighbourhood(x, y)
    nhood_rest = [nhood + 'CR', nhood + 'MR']

    return nhood_rest
