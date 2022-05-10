side_a = float(input("Please enter side A: "))
side_b = float(input("Please enter side B: "))
side_c = float(input("Please enter side C: "))

half_perimeter = (side_a + side_b + side_c) / 2
triangle_area = (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) * (half_perimeter - side_c)) * 0.5

print(triangle_area)


