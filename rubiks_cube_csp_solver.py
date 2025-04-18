import copy

# All possible Rubik's Cube face moves (clockwise and counter-clockwise)
MOVES = ['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]

# Solved cube definition (each face has 9 same-colored stickers)
SOLVED = {
    'U': ['W'] * 9,  # Up face - White
    'D': ['Y'] * 9,  # Down face - Yellow
    'L': ['O'] * 9,  # Left face - Orange
    'R': ['R'] * 9,  # Right face - Red
    'F': ['G'] * 9,  # Front face - Green
    'B': ['B'] * 9   # Back face - Blue
}

# Create a new cube (deep copy of the solved state)
def make_cube():
    return copy.deepcopy(SOLVED)

# Check if cube is solved (all stickers on each face are the same)
def is_solved(cube):
    return all(len(set(face)) == 1 for face in cube.values())

# Rotate a face 90 degrees clockwise
def rotate_face_clockwise(face):
    return [
        face[6], face[3], face[0],
        face[7], face[4], face[1],
        face[8], face[5], face[2]
    ]

# Rotate a face 90 degrees counter-clockwise
def rotate_face_counter_clockwise(face):
    return [
        face[2], face[5], face[8],
        face[1], face[4], face[7],
        face[0], face[3], face[6]
    ]

# Apply a move to the cube and return the new state
def apply_move(cube, move):
    cube = copy.deepcopy(cube)  # Avoid modifying the original cube

    # Extract all six faces
    u, d, l, r, f, b = cube['U'], cube['D'], cube['L'], cube['R'], cube['F'], cube['B']

    # Helper function to swap edge rows among four faces
    def swap(indices, faces):
        temp = [faces[0][i] for i in indices]
        for i in range(3):
            for j, idx in enumerate(indices):
                faces[i][idx] = faces[i + 1][idx]
        for j, idx in enumerate(indices):
            faces[3][idx] = temp[j]

    # Each move updates the face + adjusts adjacent face stickers
    if move == 'U':
        cube['U'] = rotate_face_clockwise(u)
        swap([0, 1, 2], [f, r, b, l])
    elif move == "U'":
        cube['U'] = rotate_face_counter_clockwise(u)
        swap([0, 1, 2], [f, l, b, r])
    elif move == 'D':
        cube['D'] = rotate_face_clockwise(d)
        swap([6, 7, 8], [f, l, b, r])
    elif move == "D'":
        cube['D'] = rotate_face_counter_clockwise(d)
        swap([6, 7, 8], [f, r, b, l])
    elif move == 'L':
        cube['L'] = rotate_face_clockwise(l)
        temp = [u[0], u[3], u[6]]
        u[0], u[3], u[6] = f[0], f[3], f[6]
        f[0], f[3], f[6] = d[0], d[3], d[6]
        d[0], d[3], d[6] = b[8], b[5], b[2]
        b[8], b[5], b[2] = temp
    elif move == "L'":
        cube['L'] = rotate_face_counter_clockwise(l)
        temp = [u[0], u[3], u[6]]
        u[0], u[3], u[6] = b[8], b[5], b[2]
        b[8], b[5], b[2] = d[0], d[3], d[6]
        d[0], d[3], d[6] = f[0], f[3], f[6]
        f[0], f[3], f[6] = temp
    elif move == 'R':
        cube['R'] = rotate_face_clockwise(r)
        temp = [u[2], u[5], u[8]]
        u[2], u[5], u[8] = b[6], b[3], b[0]
        b[6], b[3], b[0] = d[2], d[5], d[8]
        d[2], d[5], d[8] = f[2], f[5], f[8]
        f[2], f[5], f[8] = temp
    elif move == "R'":
        cube['R'] = rotate_face_counter_clockwise(r)
        temp = [u[2], u[5], u[8]]
        u[2], u[5], u[8] = f[2], f[5], f[8]
        f[2], f[5], f[8] = d[2], d[5], d[8]
        d[2], d[5], d[8] = b[6], b[3], b[0]
        b[6], b[3], b[0] = temp
    elif move == 'F':
        cube['F'] = rotate_face_clockwise(f)
        temp = [u[6], u[7], u[8]]
        u[6], u[7], u[8] = l[8], l[5], l[2]
        l[8], l[5], l[2] = d[2], d[1], d[0]
        d[2], d[1], d[0] = r[0], r[3], r[6]
        r[0], r[3], r[6] = temp
    elif move == "F'":
        cube['F'] = rotate_face_counter_clockwise(f)
        temp = [u[6], u[7], u[8]]
        u[6], u[7], u[8] = r[0], r[3], r[6]
        r[0], r[3], r[6] = d[2], d[1], d[0]
        d[2], d[1], d[0] = l[8], l[5], l[2]
        l[8], l[5], l[2] = temp
    elif move == 'B':
        cube['B'] = rotate_face_clockwise(b)
        temp = [u[0], u[1], u[2]]
        u[0], u[1], u[2] = r[2], r[5], r[8]
        r[2], r[5], r[8] = d[8], d[7], d[6]
        d[8], d[7], d[6] = l[6], l[3], l[0]
        l[6], l[3], l[0] = temp
    elif move == "B'":
        cube['B'] = rotate_face_counter_clockwise(b)
        temp = [u[0], u[1], u[2]]
        u[0], u[1], u[2] = l[6], l[3], l[0]
        l[6], l[3], l[0] = d[8], d[7], d[6]
        d[8], d[7], d[6] = r[2], r[5], r[8]
        r[2], r[5], r[8] = temp

    return cube

# Forward checking: prevent immediately undoing the last move
def is_forward_check_passed(move, path):
    if not path:
        return True
    last = path[-1]
    # Reject reverse moves like "R" followed by "R'"
    return not ((move == "U'" and last == "U") or (move == "U" and last == "U'") or
                (move == "D'" and last == "D") or (move == "D" and last == "D'") or
                (move == "L'" and last == "L") or (move == "L" and last == "L'") or
                (move == "R'" and last == "R") or (move == "R" and last == "R'") or
                (move == "F'" and last == "F") or (move == "F" and last == "F'") or
                (move == "B'" and last == "B") or (move == "B" and last == "B'"))

# CSP Solver using backtracking and forward checking
def csp_solver(cube, depth, path=[]):
    if is_solved(cube):
        return path  # Found solution!
    if depth == 0:
        return None  # Depth limit reached
    for move in MOVES:
        if not is_forward_check_passed(move, path):
            continue
        next_cube = apply_move(cube, move)
        result = csp_solver(next_cube, depth - 1, path + [move])
        if result:
            return result  # Return solution path
    return None  # No solution found at this depth

# User input to scramble the cube and solve it
scrambled = make_cube()

# Get the scramble moves from the user
scramble_moves = input("Enter scramble moves (e.g., 'U R F L' without quotes): ").split()
for move in scramble_moves:
    if move in MOVES:
        scrambled = apply_move(scrambled, move)
    else:
        print(f"Invalid move: {move}")

# Get the depth limit for the CSP solver from the user
depth = int(input("Enter the depth limit for solving the cube: "))

# Solve the scrambled cube using CSP
print("Solving scrambled cube...")
solution = csp_solver(scrambled, depth=depth)
print("Solution:", solution if solution else "No solution found")
