# Implementation and Experimentation with the K-Core Cluster Concept

- The project aims to implement and experiment with a cluster concept called k-core.
- The lecture note outlines a simple algorithm to find the k-core.
- All nodes belong to the 1-core since they all have at least 1 neighbor among all nodes.
- The green and red nodes belong to the 2-core as they have at least 2 red or green neighbors, i.e., at least 2 neighbors in the same set.
- The red nodes form the 3-core since they have at least 3 red neighbors.
- The k-core is the largest subset of nodes where each node must have at least k neighbors from the same subset.
- Having any k neighbors is not enough; they must all be in the same subset.

