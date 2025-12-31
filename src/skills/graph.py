def build_cooccurrence_graph(df, skills_col="skills"):
    graph = {}

    for skills in df[skills_col]:
        if not skills:
            continue

        n = len(skills)
        for i in range(n):
            for j in range(i + 1, n):
                skill_a = skills[i]
                skill_b = skills[j]

                # Ensure skill_a -> skill_b exists
                if skill_a not in graph:
                    graph[skill_a] = {}
                if skill_b not in graph[skill_a]:
                    graph[skill_a][skill_b] = 0
                graph[skill_a][skill_b] += 1

                # Ensure skill_b -> skill_a exists (symmetric)
                if skill_b not in graph:
                    graph[skill_b] = {}
                if skill_a not in graph[skill_b]:
                    graph[skill_b][skill_a] = 0
                graph[skill_b][skill_a] += 1

    return graph
def top_neighbors(graph, skill, k=10):
    """
    Return the top k skills that most frequently co-occur with `skill`.

    graph format:
      {
        "python": {"sql": 52, "pandas": 40},
        "sql": {"python": 52}
      }

    Returns:
      List of tuples: [("sql", 52), ("pandas", 40), ...]
    """
    if skill not in graph:
        return []

    neighbors = graph[skill]  # dict: neighbor_skill -> count

    # Sort by count descending, then by skill name for stable output
    sorted_neighbors = sorted(neighbors.items(), key=lambda x: (-x[1], x[0]))

    return sorted_neighbors[:k]
