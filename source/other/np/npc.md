# ${\sf NP}$

> NP: Nondeterministic Polynomial Time

- A problem $Q$ is ${\sf NP}$ if a solution can be verified in polynomial time.

- A problem $Q$ is ${\sf NPH}$ if all problems in ${\sf NP}$ can be reduced to $Q$ in polynomial time.

> NPH: NP-Hard

- A problem $Q$ is ${\sf NPC}$ if $Q$ is ${\sf NP}$ and ${\sf NPH}$.

> NPC: NP-Complete

## Table of Contents

- [Showing that L is in NPC](#showing-that)
- [NPC problems](#npc-problems)
  - [CIRCUIT-SAT](#circuit-sat)
  - [SAT](#sat)
  - [3-CNF-SAT](#3-cnf-sat)
  - [CLIQUE](#clique)
  - [VERTEX-COVER](#vertex-cover)
  - [HAM-CYCLE](#ham-cycle)
  - [TSP](#tsp)
  - [SUBSET-SUM](#subset-sum)

## Showing that $L \in {\sf NPC}$

- Show that $L \in {\sf NP}$.
  - That an answer can be validated in polynomial time.
  - co - ${\sf NP}$ is the same as ${\sf NP}$, but the answer is no.
- Choose a known ${\sf NPC}$ problem $L^\prime$.
- Show that $L^\prime$ can be reduced to $L$.

Note that TDT4120 only discusses decision problems.

# ${\sf NPC}$ problems

### CIRCUIT-SAT

**Instance**: A circuit with logical gates and one output.

**Question**: Can the output be true?

### SAT

**Instance**: A logical formula.

**Question**: Can the formula be true?

### 3-CNF-SAT

> CNF: Conjunctive Normal Form

**Instance**: A logical formula in 3-CNF-form.

**Question**: Can the formula be true?

### CLIQUE

**Instance**: An undirected graph $G$ and a positive integer $k$.

**Question**: Does $G$ have a complete subgraph with $k$ nodes?

### VERTEX-COVER

**Instance**: An undirected graph $G$ and a positive integer $k$.

**Question**: Does $G$ have a vertex-cover with $k$ nodes? In other words, $k$ nodes that in total touches all edges.

### HAM-CYCLE

> HAM: Hamilton

**Instance**: An undirected graph $G$.

**Question**: Does there exist a cycle that contains all nodes?

### TSP

> TSP: Travelling Salesman Problem

**Instance**: A complete graph with weights $w \in \mathbb{N}$ and a number $k \in \mathbb{N}$.

**Question**: Does there exist a rountrip with cost $\le k$?

### SUBSET-SUM

**Instance**: A multiset of positive integers $S$ and a positive integer $t$.

**Question**: Does there exist a subset of $S$ with sum equal to $t$?
