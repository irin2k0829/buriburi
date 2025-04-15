first_line = range(2, 6)  
second_line = range(6, 10) 

def print_gugudan(line_range):
    for i in range(1, 10): 
        for dan in line_range:
            print(f"{dan} x {i} = {dan*i:2}", end="\t")
        print()  

print_gugudan(first_line)

print()  

print_gugudan(second_line)