# Day 1 - Floodgate Relief Ledger

## Unstop 30-Day POTD Challenge

**Problem:** Floodgate Relief Ledger  
**Day:** 1/30  
**Language:** Python  
**Topics:** Graphs, Disjoint Set Union (DSU), Connectivity, Offline Queries

## Problem Summary

Given districts connected by canals with different minimum water-level requirements, answer queries about the total funds and number of districts reachable from a starting district. Fund values can also be updated between queries.

## Approach

The solution uses a Kruskal Reconstruction Tree to represent connectivity at different water levels, Binary Lifting to identify reachable components, and a Fenwick Tree to maintain updated fund totals.

## Sample Output

5 1
13 2
8 2

## Complexity

- Time: O(m log m + (n + q) log n)
- Space: O(n log n + m)

## Challenge Progress

- [x] Day 1: Floodgate Relief Ledger
- [ ] Day 2
- [ ] Day 3

More solutions will be added daily as part of the 30-day Unstop POTD challenge.

Follow along for daily problem-solving practice!
