def part_1():
    # Order data in columns 1 and 2 of input.txt and output the sum of the distances between them
    file = open("input.txt")
    contents = file.readlines()
    file.close()
    
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

    return l1, l2

def part_2(l1, l2):
    # Calculate a similarity score in input.txt
    similarity_score = 0

    for i, x in enumerate(l1):
        similarity_score += x * l2.count(x)

    print(similarity_score)

if __name__ == '__main__':
    l1, l2 = part_1()
    part_2(l1, l2)