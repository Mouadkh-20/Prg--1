###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input ('b=')
c= input ('c=')
a =int(a)
b =int(b)
c =int(c)
# Calculate the volume: a * b * c
cuboid_volume = a * b * c
# Calculate the surface area: 2 * (ab + ac + bc)
cuboid_surface_area = 2 * (a*b + a*c + b*c)
# Print the results
print(f'The volume of a cuboid with sides {a}, {b}, and {c} is {cuboid_volume}')
