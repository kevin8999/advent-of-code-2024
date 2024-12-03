import os

def main():
    file = open("input.txt")
    contents = file.readlines()
    
    contents = [line.split() for line in contents]
    
    l1, l2 = [], []
    for i, j in contents:
        l1.append(int(i))
        l2.append(int(j))
    
    l1 = sorted(l1)
    l2 = sorted(l2)

    distance = []
    for i, x in enumerate(l1):
        distance.append(abs(l1[i] - l2[i]))

    print(sum(distance))

if __name__ == '__main__':
    main()
