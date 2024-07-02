def adjacencyList(v, list):
    dict = {}

    for x in range(v + 1):
        dict[x] = [[], 0]

    for z in list:
        dict[z[0]][0].append(z[1])

    return dict

def topology_dfs(graph, source, stack):
    if source not in stack:
        for x in graph[source][0]:
            topology_dfs(graph, x, stack)
        stack.append(source)

def cycle_detect(graph, source):
    if graph[source][1] == 1:
        return True

    graph[source][1] = 1
    for x in graph[source][0]:
        store = cycle_detect(graph, x)
        if store is True:
            return store
    graph[source][1] = 0

    return False


read_list = [["input1a.txt", "output1a_1.txt"], ["input1b.txt", "output1b_1.txt"], ["input1c.txt", "output1c_1.txt"]]

for num in read_list:
    r = open(num[0], 'r')
    w = open(num[1], 'w')

    first = r.readline().split()
    list = []

    for x in range(int(first[1])):
        second = r.readline().split()
        second = [int(x) for x in second]
        list.append(second)

    store = adjacencyList(int(first[0]), list)
    stack = []
    flag = False
    for y in range(1, int(first[0]) + 1):
        store2 = cycle_detect(store, y)
        if store2 is True:
            flag = True
            break
    if flag == True:
        output = "IMPOSSIBLE"
        w.write(output)
    else:
        for y in range(1, int(first[0]) + 1):
            topology_dfs(store, y, stack)
        stack = stack[::-1]
        output = ""
        for z in stack:
            output += f"{z} "

        w.write(output)

    w.close()



