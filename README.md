# TDT4120 - Algorithms and Data Structures

## Table of Contents

- [Getting Started](#getting-started)
- [Course Information](#course-information)
- [Structure](#structure)

## Getting Started

- Make sure you are using Python $\ge {\sf 3.10}$.
- Download contents of the `requirements.txt`-file,
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

- Would recommend creating a `main.py`-file in the root directory,
  to be able to run the algorithms.

  ```bash
  echo 'def main() -> None:
      pass


  if __name__ == "__main__":
      main()' > main.py
  ```

> **Note:** Currently, there are no requirements for the project.

## Course Information

- **University:** Norwegian University of Science and Technology (NTNU).
- **Location:** Trondheim, Norway.
- **Faculty:** Faculty of Information Technology and Electrical Engineering (IE).
- **Department:** Department of Computer Science (IDI).
- **Study level:** Intermediate course, level $\sf II$.
- **Semester:** Autumn 2023.
- **Instructor:** Magnus Lie Hetland.
- **Language of instruction:** Norwegian.
- **Book:** Cormen, Leiserson, Rivest, Stein: Introduction to Algorithms, fourth edition.

> **Note:** The course is subject to change.
> All algorithms are based on source code from the book.
> Master's level courses are called "Second degree level".

## Structure

```bash
├── exercises
│   ├── exercise01
│   │   ├── max_permutations.py
│   │   └── take_pieces.py
│   ├── exercise02
│   │   └── sort.py
│   ├── exercise03
│   │   ├── find_maximum.py
│   │   └── largest_cuboid.py
│   ├── exercise04
│   │   ├── flexradix.py
│   │   └── k_largest.py
│   ├── exercise05
│   │   ├── build_tree.py
│   │   ├── longest_repeated_substring.py
│   │   ├── node.py
│   │   ├── search_tree.py
│   │   └── string_match.py
│   ├── exercise06
│   │   ├── f.py
│   │   └── longest_decreasing_subsequence.py
│   ├── exercise07
│   │   ├── build_decision_tree.py
│   │   ├── encode.py
│   │   └── encoding.py
│   ├── exercise08
│   │   ├── compatibility_graph.py
│   │   ├── detect_envy_cycle.py
│   │   ├── resolve_and_install.py
│   │   └── shortest_road.py
│   ├── exercise09
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
│   │   │   ├── helpers
│   │   │   │   ├── initialize_single_source.py
│   │   │   │   └── relax.py
│   │   │   └── shortest_paths.py
│   │   └── traversal
│   │       ├── bfs.py
│   │       ├── bipartite.py
│   │       ├── dfs.py
│   │       ├── edge_classification.py
│   │       └── traverse.py
│   ├── other
│   │   ├── dynamic_programming
│   │   │   ├── knapsack.py
│   │   │   ├── lcs_length.py
│   │   │   ├── matrix_chain_product.py
│   │   │   └── rod_cutting.py
│   │   ├── greed
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
> The `bipartite.py`-file,
> the `shortest_paths.py`,
> the `print_heap`-function in `heap.py`-file,
> and the `height`, `tree_preorder_walk` and `tree_postorder_walk`-methods in the `tree.py`-file are not part of the curriculum.
