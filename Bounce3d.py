import vpython as vp

marble_radius = 2
room_height = 14
room_width = 12
room_depth = 40
wall_thickness = 0.5
box_opacity = 0.6

bottom_wall = vp.box(
    pos=vp.vector(0, -room_height / 2, 0),
    size=vp.vector(room_width, wall_thickness, room_depth),
    color=vp.color.red,
    opacity=box_opacity,
)
top_wall = vp.box(
    pos=vp.vector(0, room_height / 2, 0),
    size=vp.vector(room_width, wall_thickness, room_depth),
    color=vp.color.red,
    opacity=box_opacity,
)
left_wall = vp.box(
    pos=vp.vector(-room_width / 2, 0, 0),
    size=vp.vector(wall_thickness, room_height, room_depth),
    color=vp.color.red,
    opacity=box_opacity,
)
right_wall = vp.box(
    pos=vp.vector(room_width / 2, 0, 0),
    size=vp.vector(wall_thickness, room_height, room_depth),
    color=vp.color.red,
    opacity=box_opacity,
)
back_wall = vp.box(
    pos=vp.vector(0, 0, -room_depth / 2),
    size=vp.vector(room_width, room_height, wall_thickness),
    color=vp.color.red,
    opacity=box_opacity,
)
marble = vp.sphere(radius=marble_radius, color=vp.color.blue)
x_pos = 0
x_delta = 0.1
y_pos = 0
y_delta = 0.1
z_pos = 0
z_delta = 0.1


while True:
    # Visual pyhton funtion that regulates the rate
    vp.rate(20)
    # adding movement in all axis
    x_pos += x_delta
    y_pos += y_delta
    z_pos += z_delta

    # defining the edges of the ball
    marble_right_edge = x_pos + marble_radius
    marble_left_edge = x_pos - marble_radius
    marble_top_edge = y_pos + marble_radius
    marble_bottom_edge = y_pos - marble_radius
    marble_front_edge = z_pos + marble_radius
    marble_back_edge = z_pos - marble_radius

    # defining the edges of the room
    right_wall_edge = room_width / 2 - wall_thickness / 2
    left_wall_edge = -room_width / 2 + wall_thickness / 2
    top_wall_edge = room_height / 2 - wall_thickness / 2
    bottom_wall_edge = -room_height / 2 + wall_thickness / 2
    back_wall_edge = -room_depth / 2 + wall_thickness / 2
    front_wall_edge = room_depth / 2 - wall_thickness / 2

    # updating the object's position
    marble.pos = vp.vector(x_pos, y_pos, z_pos)

    # Detecting collisions and reversing direction
    if marble_right_edge >= right_wall_edge or marble_left_edge <= left_wall_edge:
        x_delta = -x_delta
    if marble_top_edge >= top_wall_edge or marble_bottom_edge <= bottom_wall_edge:
        y_delta = -y_delta
    if marble_front_edge >= front_wall_edge or marble_back_edge <= back_wall_edge:
        z_delta = -z_delta
