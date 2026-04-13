from collections import deque

def topological_sort(graph: dict[str, list[str]]) -> list[str]:
    """
    Kahn's algorithm for topological sort.
    Handles graphs where neighbors may not appear as keys.

    Time Complexity: O(V + E) where V = vertices, E = edges
    Space Complexity: O(V) for in_degree dict, queue, and result list
    """
    in_degree = {node: 0 for node in graph}

    # Calculate in-degrees, handling nodes that only appear as neighbors
    for node in graph:
        for neighbour in graph[node]:
            if neighbour not in in_degree:
                in_degree[neighbour] = 0
            in_degree[neighbour] += 1

    queue = deque([node for node, count in in_degree.items() if count == 0])

    res = []
    while queue:
        node = queue.popleft()
        res.append(node)
        # Use .get() to handle nodes that only appear as neighbors
        for n in graph.get(node, []):
            in_degree[n] -= 1
            if in_degree[n] == 0:
                queue.append(n)
    
    # Check against all nodes (in_degree includes neighbors too)
    if len(res) != len(in_degree):
        raise Exception("cyclical deps")

    return res


if __name__ == "__main__":
    # Example: course prerequisites
    graph = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": [],
        "E": ["A"]
    }

    res = topological_sort(graph)
    print("Topological order:", res)
    expected = ["E", "A", "B", "C", "D"]
    assert all(a == b for a, b in zip(res, expected)) and (len(res) == len(expected))

    # Example with cycle
    graph_with_cycle = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"]
    }

    try:
        res_cycle = topological_sort(graph_with_cycle)
    except Exception as e:
        print(e)

    # Edge case: neighbor not in graph keys
    graph_incomplete = {
        "A": ["B", "C"],
        "B": ["D"]
        # C and D don't appear as keys
    }
    res_incomplete = topological_sort(graph_incomplete)
    print(f"Incomplete graph order: {res_incomplete}")

    print("All good")

