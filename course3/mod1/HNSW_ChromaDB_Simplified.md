# Similarity Search and HNSW in ChromaDB (Simplified Notes)

## Core Problem

Suppose we have:

- 1,000,000 document embeddings
- 1 query embedding

Naive similarity search:

1. Compare query with every document.
2. Compute cosine similarity for all.
3. Return highest scores.

Problem:

- Accurate
- Extremely slow at scale

---

## Solution: Vector Index

A vector index organizes embeddings so we do not need to compare against every vector.

Instead of:

Query → 1,000,000 comparisons

We do:

Query → Few hundred/thousand promising candidates

Result:

- Faster retrieval
- Scales to millions or billions of vectors

---

## What is HNSW?

HNSW = Hierarchical Navigable Small World

It is the vector index used by ChromaDB.

HNSW is a graph-based Approximate Nearest Neighbor (ANN) algorithm.

Instead of scanning all vectors, it navigates through a graph of connected vectors.

---

## HNSW Intuition

Imagine finding a house in a city.

Bad approach:

- Check every house

Good approach:

City → Area → Street → House

HNSW works similarly.

It searches from broad regions to more detailed regions.

---

## HNSW Layers

Layer 3 (Overview)

↓

Layer 2

↓

Layer 1

↓

Layer 0 (All Vectors)

Search starts at the top and gradually moves down to the most relevant vectors.

---

## Why is it called Small World?

Similar vectors are connected together.

Example:

Vector A → Vector B → Vector C

A search can jump through nearby vectors quickly rather than checking everything.

---

## ANN (Approximate Nearest Neighbor)

HNSW does not always guarantee the exact nearest vector.

Instead:

- Very close to exact result
- Much faster

Trade-off:

| Method | Accuracy | Speed |
|----------|----------|----------|
| Brute Force | Highest | Slow |
| HNSW (ANN) | Near Exact | Very Fast |

---

## HNSW Parameters

### 1. space

Distance metric used.

| Value | Meaning |
|---------|---------|
| l2 | Euclidean Distance |
| cosine | Cosine Distance |
| ip | Inner Product / Dot Product |

Most embedding applications use cosine.

---

### 2. ef_search

Controls search quality during querying.

Small value:

- Faster
- Lower recall

Large value:

- Slower
- Better accuracy

Memory Trick:

ef_search = Search Time Quality

---

### 3. ef_construction

Controls how carefully the graph is built.

Small value:

- Faster indexing
- Lower quality graph

Large value:

- Slower indexing
- Better graph

Memory Trick:

ef_construction = Build Time Quality

---

### 4. max_neighbors

Maximum number of neighbors each node can connect to.

Small value:

- Less memory
- Faster construction

Large value:

- Better navigation
- Higher memory usage

---

## Example Dataset

Documents:

id1 → pandas animal

id2 → pandas library

id3 → pandas animal

id4 → pandas library

---

## Semantic Search Example

Query:

cats

Result:

id3 → pandas are cute animals

id1 → pandas are bears

Why?

The embedding model understands:

cats ≈ animals

instead of matching keywords only.

---

## Semantic Search Failure

Query:

polar bear

Expected:

animal document

Actual:

polars library document

Reason:

The embedding model associated:

polar ≈ polars

leading to a wrong semantic match.

---

## Fix 1: Metadata Filtering

```python
where={"topic":"animals"}
```

Only animal documents are searched.

---

## Fix 2: Document Filtering

```python
where_document={"$not_contains":"library"}
```

Library-related documents are excluded.

---

## Combining Filters

```python
collection.query(
    query_texts=["polar bear"],
    where={"topic":"animals"},
    where_document={"$not_contains":"library"}
)
```

Process:

1. Apply metadata filter.
2. Apply document filter.
3. Run HNSW similarity search.
4. Return best matches.

---

## RAG Retrieval Pipeline

User Query

↓

Metadata Filter

↓

Document Filter

↓

HNSW Similarity Search

↓

Top-k Chunks

↓

LLM

---

## Key Takeaways

| Concept | Summary |
|----------|----------|
| Vector Index | Organizes embeddings for fast retrieval |
| HNSW | Graph-based ANN index used by ChromaDB |
| ANN | Near-exact results with much faster speed |
| ef_search | Search-time accuracy vs speed |
| ef_construction | Index-building quality |
| max_neighbors | Graph density |
| Metadata Filters | Filter using structured fields |
| Document Filters | Filter using text content |
| Similarity Search | Finds semantically related documents |

---

## Interview Answer

HNSW (Hierarchical Navigable Small World) is a graph-based Approximate Nearest Neighbor (ANN) index used by ChromaDB to perform fast similarity searches by navigating through a multi-layer graph instead of comparing a query against every vector in the database.
