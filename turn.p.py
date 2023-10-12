n = int(input())

for i in range(n):
    if 6 != int(input()):
        print("NO")
    else:
        print("YES")

    arr = [int(x) for x in input().split()]
    print(arr[0]-arr[1])
    if arr[2]>=arr[0] and arr[2]<arr[1]:
        print("YES")
    else:
        print("NO")

