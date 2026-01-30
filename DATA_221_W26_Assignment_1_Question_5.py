'''
Question 5

Write a function that takes the radii of two circles and performs the following:
• Validates that both radii are positive integers.
• Computes the area of each circle.
• Returns the percentage of the larger circle’s area that can be covered by the smaller circle.
If invalid input is provided, return a meaningful message instead of performing the calculation.

'''

def circle_area_coverage(radius_of_circle1, radius_of_circle2):

    #Input conditions.
    if not isinstance(radius_of_circle1, int) or not isinstance(radius_of_circle2, int):
        return "Radii must be an integer"
    elif radius_of_circle1 <= 0 or radius_of_circle2 <= 0:
        return "Radii must be positive."

    #Formula.
    pi = 3.14159

    area_of_circle1 = pi * radius_of_circle1 ** 2
    area_of_circle2 = pi * radius_of_circle2 ** 2

    area_covered_by_smaller_circle = 0

    #Checks the circle sizes.
    if area_of_circle1 < area_of_circle2:
        area_covered_by_smaller_circle = area_of_circle1 / area_of_circle2
    elif area_of_circle2 < area_of_circle1:
        area_covered_by_smaller_circle = area_of_circle2 / area_of_circle1

    return area_covered_by_smaller_circle

#All possible output messages.
print(circle_area_coverage(5, 3))
print(circle_area_coverage(7, 14))
print(circle_area_coverage(-7, 14))
print(circle_area_coverage(7, -14))
print(circle_area_coverage(-7, -14))
print(circle_area_coverage(7.1, 14))
print(circle_area_coverage(7, 14.1))
print(circle_area_coverage(7.1, 14.1))

