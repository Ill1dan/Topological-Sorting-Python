def adjacencyList(v, list):
    dict = {}

    for x in range(v + 1):
        dict[x] = [[], 0]

    for z in list:
        dict[z[0]][0].append(z[1])

    return dict

def topology_bfs(graph, indegree_array, output_topology, queue):
    if len(output_topology) == len(indegree_array) - 1:
        return

    for x in range(len(indegree_array)):
        if x > 0 and indegree_array[x] == 0 and x not in output_topology:
            queue.append(x)

    for y in range(len(queue)):
        for z in graph[queue[y]][0]:
            indegree_array[z] -= 1

    for i in range(len(queue)):
        vertex = queue.pop(0)
        output_topology.append(vertex)

    topology_bfs(graph, indegree_array, output_topology, queue)


def indegree(graph, indegree_array):
    for x in range(len(indegree_array) - 1):
        for y in graph[x][0]:
            indegree_array[y] += 1

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


read_list = [["input1a.txt", "output1a_2.txt"], ["input1b.txt", "output1b_2.txt"], ["input1c.txt", "output1c_2.txt"]]

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
        indegree_array = [0 for x in range(int(first[0]) + 1)]
        indegree(store, indegree_array)
        output_topology = []
        queue = []
        topology_bfs(store, indegree_array, output_topology, queue)

        output = ""

        for y in output_topology:
            output += f"{y} "
        w.write(output)

    w.close()



