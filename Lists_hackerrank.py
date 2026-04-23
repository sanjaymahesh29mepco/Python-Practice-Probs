if __name__ == '__main__':
    N = int(input())
    res = []
    
    for _ in range(N):
        command = input().split()
        action = command[0]
        
        if action == "insert":
            res.insert(int(command[1]), int(command[2]))
        elif action == "print":
            print(res)
        elif action == "remove":
            res.remove(int(command[1]))
        elif action == "append":
            res.append(int(command[1]))
        elif action == "sort":
            res.sort()
        elif action == "pop":
            res.pop()
        elif action == "reverse":
            res.reverse()
