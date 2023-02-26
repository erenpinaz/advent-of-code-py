def get_input():
    with open('input.txt') as f:
        input = [x.split(',') for x in f.read().split('\n')]
        
    return input

input = get_input()

# Part 1
# ==========

def manhattan(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_intersections(input):
    coords = set()
    intersections = []
    
    for i, w in enumerate(input):
        x, y = 0, 0
        
        for d in w:
            for j in range(0, int(d[1:])):
                if(d[0] == 'R'):
                    x = x + 1
                    y = y
                    
                if(d[0] == 'L'):
                    x = x - 1
                    y = y
                    
                if(d[0] == 'U'):
                    x = x
                    y = y + 1
                    
                if(d[0] == 'D'):
                    x = x
                    y = y - 1
                    
                coord = (x, y)
                
                if(i == 0):
                    coords.add(coord)
                else:
                    if(coord in coords):
                        intersections.append(manhattan(coord[0], 0, coord[1], 0))
            
    return min(intersections)

intersections = find_intersections(input)
print(intersections)

# Part 2
# ==========

def find_set_intersections(d1, d2):
    return list(set(d1.keys()) & set(d2.keys()))

def intersection_min_combined_steps(intrs, d1, d2):
    return min([d1[i] + d2[i] for i in intrs])

def generate_coordinates(wire):
    x, y, step = 0, 0, 0    
    coords = {}
    
    for d in wire:
        for j in range(0, int(d[1:])):
            if(d[0] == 'R'):
                x = x + 1
                y = y
                
            if(d[0] == 'L'):
                x = x - 1
                y = y
                
            if(d[0] == 'U'):
                x = x
                y = y + 1
                
            if(d[0] == 'D'):
                x = x
                y = y - 1
                
            step = step + 1
            coords[(x, y)] = step
            
    return coords

w1_coords = generate_coordinates(input[0])
w2_coords = generate_coordinates(input[1])
intersections = find_set_intersections(w1_coords, w2_coords)

print(intersection_min_combined_steps(intersections, w1_coords, w2_coords))
