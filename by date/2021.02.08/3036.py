import math

N = int(input())
rings = []
first_ring = 0

def set_rings():
    global rings, first_ring

    rings = list(map(int, input().split()))
    first_ring = rings[0]
    rings = rings[1:]

def init():
    set_rings()
    return

def print_result():
    for r in rings:
        gcd = math.gcd(first_ring, r)
        print("{}/{}".format(first_ring // gcd, r // gcd))

def main():
    print_result()
    return

if(__name__=="__main__"):
    init()
    main()
