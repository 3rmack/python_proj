import json


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


def get_child(j_load):
    d = dict()
    for item in j_load:
        # print(item)
        d[item["name"]] = set()
        for items in j_load:
            # print("item[\"name\"] = ", item["name"])
            # print("items[\"parents\"] = ", items["parents"])
            if item["name"] in items["parents"]:
                d[item["name"]].add(items["name"])
    return d

input_str = '[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]'
j_load = json.loads(input_str)

result = get_child(j_load)
# print(result)
result_final = dict()
for graph in j_load:
    result_final[graph["name"]] = len(dfs(result, graph["name"]))
    # print("{} : {}".format(graph["name"], len(dfs(result, graph["name"]))))
for graph_name in sorted(result_final):
    print("{} : {}".format(graph_name, result_final[graph_name]))
