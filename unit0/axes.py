Web VPython 3.2


# Axis parameters
axis_length = 5
thickness = 1

# x
box(pos=vector(axis_length/2, 0, 0), size=vector(axis_length, thickness, thickness), color=color.red)
cone(pos=vector(axis_length, 0, 0), axis=vector(axis_length*0.1, 0, 0), radius=thickness*0.75, color=color.red)

# y
box(pos=vector(0, axis_length/2, 0), size=vector(thickness, axis_length, thickness), color=color.green)
cone(pos=vector(0, axis_length, 0), axis=vector(0, axis_length*0.1, 0), radius=thickness*0.75, color=color.green)

# z
box(pos=vector(0, 0, axis_length/2), size=vector(thickness, thickness, axis_length), color=color.blue)
cone(pos=vector(0, 0, axis_length), axis=vector(0, 0, axis_length*0.1), radius=thickness*0.75, color=color.blue)
