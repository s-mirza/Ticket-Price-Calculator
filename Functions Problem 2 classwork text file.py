#problem #2

#define a function that will take class type and number of tickes per

def get_number_tickets(ticket_type, num_tickets):
    if (ticket_type == 'A'):
        return num_tickets *  20.00
    elif(ticket_type == 'B'):
        return num_tickets * 15.00
    elif(ticket_type == 'C'):
        return num_tickets * 10.00
    else:
        return -1 
    
def main():
    #number of tickets for class A
    num_a = int(input("How many class A tickets do you need: "))
    num_b = int(input("How many class B tickets do you need: "))
    num_c = int(input("How many class C tickets do you need: "))

    #class type is "hard-coded"
    price_a = get_number_tickets('A', num_a)
    price_b = get_number_tickets('B', num_b)
    price_c = get_number_tickets('C', num_c)

    #print
    print("-"*30)
    print(f"{'Receipt':^30}") 
    print("-"*30) 
    print(f"Class A      x{num_a}     ${price_a}")
    print(f"Class B      x{num_b}     ${price_b}")
    print(f"Class C      x{num_c}     ${price_c}")
    print("-"*30)
    print(f"    Total       ${price_a + price_b + price_c:>5.2f}")
    print("-"*30)

main()