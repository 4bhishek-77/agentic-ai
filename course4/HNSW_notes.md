# HNSW (Hierarchical Navigable Small World) — Simple Notes 🚀

## 🔥 Big Idea
HNSW ek fast indexing + search algorithm hai jo vector databases me use hota hai (ChromaDB, Qdrant, Weaviate etc.).

Goal: Millions of embeddings me se fast similar vector dhoondhna

## ❌ Problem (Without HNSW)

Agar brute force kare:
Query → compare with all vectors

Time complexity: O(N)

## 🧠 HNSW Idea

HNSW vectors ko ek multi-layer graph me arrange karta hai.

Layer 2 → High level (fast jumps)
Layer 1 → Medium level
Layer 0 → Ground level (detailed search)

## 🏙️ Analogy (City Map)

Layer 2 → Highways
Layer 1 → Main roads
Layer 0 → Local streets

## ⚙️ How Search Works

Step 1: Start at top layer
Step 2: Greedy move
Step 3: Go down layer by layer
Step 4: Bottom layer search

## ⚡ Why HNSW is Fast?

Brute force → O(N)
HNSW → ~O(log N)

## 🧱 How Graph is Built

1. Random layer assign
2. Nearest neighbors connect
3. Bidirectional links

## 📦 Important Parameters

M → neighbors count
efConstruction → build quality
efSearch → search quality

## 🧩 ChromaDB Relation

ChromaDB internally uses HNSW often

Text → Embedding → HNSW Index → Storage

## 🧠 One-Line Definition

HNSW is a hierarchical graph-based algorithm for fast approximate nearest neighbor search.

## 🚀 Final Intuition

Embedding = meaning vector
HNSW = Google Maps for vectors
Vector DB = full system
