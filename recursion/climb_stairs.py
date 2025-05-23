def climb_stairs(final_state):
    if final_state < 0:
        return 0
    if final_state == 0:
        return 1
    l = climb_stairs(final_state-1)
    r = climb_stairs(final_state-2)
    return  l+r 

if __name__ == '__main__':
    n = int(input("enter number of stairs: "))
    print(f"Number of ways to climb: {climb_stairs(n)}")