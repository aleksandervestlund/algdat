# TDT4120 - Algorithms and Data Structures

> Written by: _Aleksander Thornes Vestlund_.

## Table of Contents

- [Getting Started](#getting-started)
- [Structure](#structure)

## Getting Started

- Make sure you are using Pytohn $\ge {\sf 3.10}$.
- Download contents of the `requirements.txt` file,
  either in a virtual environment or locally.

  ```bash
  pip install -r requirements.txt
  ```

  - To create a virtual environment, run the following command:

    ```bash
    python -m venv venv
    ```

  - To activate the virtual environment, run the following command:

    ```bash
    source venv/bin/activate
    ```

  - To deactivate the virtual environment, run the following command:

    ```bash
    deactivate
    ```

- Would recommend creating a `main.py` file in the root directory,
  to be able to run the algorithms.

  ```bash
  echo 'def main() -> None:
      pass


  if __name__ == "__main__":
      main()' > main.py
  ```

> **Note:** Currently, there are no requirements for the project.

### Structure

```bash
├── exercises
│   ├── exercise1
│   │   └── take_pieces.py
│   ├── exercise2
│   │   └── sort.py
│   ├── exercise3
│   │   ├── find_maximum.py
│   │   └── largest_cuboid.py
│   ├── exercise4
│   │   ├── flexradix.py
│   │   └── k_largest.py
│   ├── exercise5
│   │   ├── build_tree.py
│   │   ├── longest_repeated_substring.py
│   │   ├── node.py
│   │   ├── search_tree.py
│   │   └── string_match.py
│   ├── exercise6
│   │   ├── f.py
│   │   └── longest_decreasing_subsequence.py
│   ├── exercise7
│   │   ├── build_decision_tree.py
│   │   ├── encode.py
│   │   └── encoding.py
│   ├── exercise8
│   │   ├── compatibility_graph.py
│   │   ├── detect_envy_cycle.py
│   │   ├── resolve_and_install.py
│   │   └── shortest_road.py
│   ├── exercise9
│   │   ├── check.py
│   │   ├── find_animal_groups.py
│   │   ├── higher_ed_solver.py
│   │   ├── power_grid.py
│   │   └── set.py
│   ├── exercise10
│   │   ├── building_time.py
│   │   ├── earliest_arrival.py
│   │   └── least_energy.py
│   ├── exercise11
│   │   ├── general_floyd_warshall.py
│   │   ├── schulze_method.py
│   │   └── transitive_closure.py
│   ├── exercise12
│   │   ├── allocate.py
│   │   └── max_flow.py
│   └── exercise13
│       └── verify_tsp.py
├── source
│   ├── datastructures
│   │   ├── chained_hash_table.py
│   │   ├── graph.py
│   │   ├── heap.py
│   │   ├── helpers
│   │   │   └── underflow.py
│   │   ├── huffman_node.py
│   │   ├── linked_list.py
│   │   ├── priority_queue.py
│   │   ├── queue.py
│   │   ├── set.py
│   │   ├── stack.py
│   │   ├── table.py
│   │   └── tree.py
│   ├── graphs
│   │   ├── all_pairs_shortest_paths
│   │   │   ├── extend_shortest_paths.py
│   │   │   ├── faster_apsp.py
│   │   │   ├── floyd_warshall.py
│   │   │   ├── johnson.py
│   │   │   ├── print_all_pairs_shortest_paths.py
│   │   │   ├── slow_apsp.py
│   │   │   └── transitive_closure.py
│   │   ├── flow
│   │   │   ├── edmond_karp.py
│   │   │   ├── ford_fulkerson.py
│   │   │   └── helpers
│   │   │       └── bfs_labelling.py
│   │   ├── minimal_spanning_tree
│   │   │   ├── components.py
│   │   │   ├── mst_kruskal.py
│   │   │   └── mst_prim.py
│   │   ├── single_source_shortest_paths
│   │   │   ├── bellman_ford.py
│   │   │   ├── dag_shortest_paths.py
│   │   │   ├── dijkstra.py
│   │   │   └── helpers
│   │   │       ├── initialize_single_source.py
│   │   │       └── relax.py
│   │   └── traversal
│   │       ├── bfs.py
│   │       ├── bipartite.py
│   │       ├── dfs.py
│   │       ├── edge_classification.py
│   │       └── traverse.py
│   ├── other
│   │   ├── dynamic
│   │   │   ├── knapsack.py
│   │   │   ├── lcs_length.py
│   │   │   ├── matrix_chain_product.py
│   │   │   └── rod_cutting.py
│   │   ├── greedy
│   │   │   ├── activity_selector.py
│   │   │   ├── gale_shapley.py
│   │   │   └── huffman.py
│   │   └── np
│   │       ├── has_short_path.py
│   │       ├── npc.md
│   │       └── verify_short_path.py
│   └── sorting
│       ├── bucket_sort.py
│       ├── counting_sort.py
│       ├── helpers
│       │   ├── bisect.py
│       │   ├── merge.py
│       │   ├── partition.py
│       │   └── select.py
│       ├── insertion_sort.py
│       ├── merge_sort.py
│       ├── quicksort.py
│       └── radix_sort.py
└── tests
```

> **Note:** Generated using the `tree` command.
> The structure is subject to change.
> The `exercises` directory is no longer part of the git repository.
> The `tests` directory is empty.
> The `bipartite.py` file is not part of the curriculum.
