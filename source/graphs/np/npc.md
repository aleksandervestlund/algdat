# NP

> Nondeterministic Polynomial Time

## Table of Contents

- [Showing that $L \in NPC$](#showing-that)
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
- Choose a known NPC problem $L'$.
- Show that $L'$ can be reduced to $L$.

Note that TDT4120 only talks about decision problems.

# NPC problems

> NP-Complete

### CIRCUIT-SAT

**Instance**: A circuit with logical gates and one output.

**Question**: Can the output be true?

### SAT

**Instance**: A logical formula.

**Question**: Can the formula be true?

### 3-CNF-SAT

> Conjunctive Normal Form

**Instance**: A logical formula in 3-CNF-form.

**Question**: Can the formula be true?

### CLIQUE

**Instance**: An undirected graph $G$ and a positive integer $k$.

**Question**: Does $G$ have a complete subgraph with $k$ nodes?

### VERTEX-COVER

**Instance**: An undirected graph $G$ and a positive integer $k$.

**Question**: Does $G$ have a vertex-cover with $k$ nodes? In other words, $k$ nodes that in total touches all edges.

### HAM-CYCLE

> Hamilton-cycle

**Instance**: An undirected graph $G$.

**Question**: Does there exist a cycle that contains all nodes?

### TSP

> Travelling Salesman Problem

**Instance**: A complete graph with weights $w \in \mathbb{N}$ and a number $k \in \mathbb{N}$.

**Question**: Does there exist a rountrip with cost $c \le k$?

### SUBSET-SUM

**Instance**: A set og positive integers $S$ and a positive integer $t$.

**Question**: Does there exist a subset of $S$ with sum $t$?
