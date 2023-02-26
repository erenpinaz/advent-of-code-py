def get_input(n, v):
    with open('input.txt') as f:
        input = [int(x.strip()) for x in f.read().split(',')]
    
    input[1] = n
    input[2] = v
        
    return input

def calculate_output(n, v):
    input = get_input(n, v)
    
    for i in range(0, len(input), 4):        
        if input[i] == 99:
            break

        if input[i] == 1:
            input[input[i + 3]] = input[input[i + 1]] + input[input[i + 2]]
        if input[i] == 2:
            input[input[i + 3]] = input[input[i + 1]] * input[input[i + 2]]
    
    return input[0]

def find_output(output):
    for i in range (0, 100):
        for j in range (0, 100):
            result = calculate_output(i, j)
            
            if(result == output):
                print((100 * i) + j)
                break

# Part 1
# ==========

print(calculate_output(12, 2))

# Part 2
# ==========
find_output(19690720)