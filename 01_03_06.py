#introduction to functions

# def greet(name, time):
#     print(f'Howdy {name}, good {time}')

# greet('uju','afternoon')

# Finding the volume of a cylinder
# def area(radius):
#     return 3.142*radius**2
# raduis = int(input('what is the radius of the circle '))

# def volume(area, lenght):
#     print(area*lenght)
# lenght = int(input('what is the length of the cylinder '))

# volume(area(raduis), lenght)

#another method
def volume(area, lenght):
    print(f'The volume of the cylinder is: {area*lenght}')
radius = int(input('what is the radius of the circle '))
lenght = int(input('what is the length of the cylinder '))
area = 3.142*radius**2
volume(area, lenght)