# Explore Advanced Retrievers in LlamaIndex — Simplified Notes (Hinglish)

## Overview
Ye lab LlamaIndex ke advanced retrievers ko IBM watsonx.ai ke saath use karke RAG (Retrieval Augmented Generation) systems banana sikhata hai.

**Estimated Time:** 60 min

---

# Objectives

Is lab ke baad tum:

- Different retriever types samajh paoge
- Vector Index Retriever implement kar paoge
- BM25 keyword retrieval samajh paoge
- Document Summary Retrievers use kar paoge
- Auto Merging Retriever samajh paoge
- Recursive Retriever samajh paoge
- Query Fusion Retriever ke different modes compare kar paoge
- Production-grade RAG pipelines design kar paoge

---

# Required Libraries

Main libraries:

- llama-index
- llama-index-embeddings-huggingface
- llama-index-llms-ibm
- llama-index-retrievers-bm25
- sentence-transformers
- rank-bm25

---

# Important Imports

## Core LlamaIndex

- VectorStoreIndex
- SummaryIndex
- Document
- Settings
- StorageContext

## Retrievers

- VectorIndexRetriever
- QueryFusionRetriever
- RecursiveRetriever
- AutoMergingRetriever
- BM25Retriever

## Embeddings

- HuggingFaceEmbedding

## IBM Integration

- WatsonxLLM

---

# watsonx.ai Integration

Lab IBM watsonx.ai ko LlamaIndex ke saath integrate karta hai.

### Purpose

- IBM foundation models use karna
- LlamaIndex compatibility maintain karna
- Production-ready architecture banana

### Embedding Model

Used model:

BAAI/bge-small-en-v1.5

Purpose:

- Text ko vectors me convert karna
- Semantic similarity search perform karna

---

# Background

## Advanced Retrievers Kya Hote Hain?

Advanced retrievers normal similarity search se aage badhkar:

- Better relevance dete hain
- Context preserve karte hain
- Multiple retrieval strategies combine karte hain
- Complex document structures handle karte hain

## Importance

Benefits:

- Higher retrieval quality
- Better RAG performance
- Improved context understanding
- Better scalability

---

# Sample Dataset

Lab AI/ML related documents use karta hai.

Topics include:

- Machine Learning
- Deep Learning
- Natural Language Processing
- Computer Vision
- Reinforcement Learning
- Transfer Learning
- Transformers
- Large Language Models
- RAG
- Vector Databases

---

# AdvancedRetrieversLab Class

Lab class:

- Documents create karti hai
- Multiple indexes build karti hai
- Retrieval experiments support karti hai

Indexes created:

1. Vector Index
2. Summary Index
3. Hierarchical Indexes

---

# 1. Vector Index Retriever

## Idea

Semantic search use karta hai.

Exact words match karna zaruri nahi.

### Example

Query:
"AI models that understand language"

Relevant Result:
"NLP" document

Even if exact words present na hon.

## Configuration

similarity_top_k = 3

Matlab:

Top 3 most similar documents retrieve honge.

## Best Use Cases

- General semantic search
- RAG applications
- Knowledge assistants
- FAQ systems

## Advantages

- Meaning samajhta hai
- Synonyms handle karta hai
- Flexible search

## Limitations

- Exact keyword search me BM25 better ho sakta hai

---

# 2. BM25 Retriever

## Overview

BM25 ek keyword-based retrieval algorithm hai.

Search engines me extensively use hota hai.

---

## TF-IDF Foundation

TF-IDF =

Term Frequency × Inverse Document Frequency

### Problem

TF-IDF:

- Document length properly handle nahi karta
- Term saturation ignore karta hai

---

## BM25 Improvements

BM25 solve karta hai:

### 1. Document Length Normalization

Long documents unfair advantage nahi lete.

### 2. Term Frequency Saturation

Ek keyword 100 baar repeat karne se score infinitely increase nahi hota.

### 3. Better Ranking

More realistic relevance scoring.

---

## Use Cases

- Exact keyword search
- Search engines
- Legal documents
- Technical documentation

---

## Advantages

- Fast
- Interpretable
- Excellent keyword matching

## Limitations

- Semantic meaning nahi samajhta

---

# 3. Document Summary Index Retriever

## Concept

Har document ka summary create kiya jata hai.

Retrieval summaries ke basis par hota hai.

### Workflow

Document
→ Summary
→ Retrieval

---

## Benefits

- Large documents efficiently handle karta hai
- Noise reduce karta hai
- High-level understanding improve karta hai

---

## Use Cases

- Long reports
- Research papers
- Books
- Enterprise documents

---

# 4. Auto Merging Retriever

## Problem

Chunking se context toot jata hai.

Example:

Large paragraph
→ multiple chunks

Relevant info multiple chunks me split ho sakta hai.

---

## Solution

Auto Merging Retriever:

Relevant child chunks retrieve karta hai.

Agar required ho to:

Parent chunks merge karta hai.

---

## Benefits

- Context preservation
- Better coherence
- More complete answers

---

## Best Use Cases

- Large hierarchical documents
- PDFs
- Documentation

---

# 5. Recursive Retriever

## Concept

References follow karta hai.

Agar retrieved node kisi aur node ko reference karta hai:

Retriever recursively us reference ko bhi retrieve karta hai.

---

## Workflow

Query
→ Node A
→ Reference B
→ Retrieve B
→ Reference C
→ Retrieve C

---

## Benefits

- Deep knowledge traversal
- Connected information retrieval

---

## Use Cases

- Knowledge graphs
- Linked documents
- Multi-level references

---

# 6. Query Fusion Retriever

## Core Idea

Single query par depend nahi karta.

Multiple query variations generate karta hai.

Fir results combine karta hai.

---

## Why Useful?

Users different ways me same cheez pooch sakte hain.

Fusion retrieval:

- Recall improve karta hai
- Coverage improve karta hai
- Missing information reduce karta hai

---

# 6.1 Reciprocal Rank Fusion (RRF)

## Formula

Score = Σ (1 / (k + rank))

### Idea

Higher-ranked results ko zyada importance milti hai.

---

## Advantages

- Simple
- Robust
- Widely used

---

# 6.2 Relative Score Fusion

## Idea

Scores normalize kiye jate hain.

Fir combine hote hain.

---

## Benefits

- Better score comparison
- Different retrievers ke outputs combine kar sakta hai

---

# 6.3 Distribution-Based Score Fusion

## Idea

Score distributions analyze ki jati hain.

Statistical normalization perform hota hai.

---

## Benefits

- More sophisticated fusion
- Better score balancing

---

# Recommended Retriever Selection

## General Semantic Search

Use:

Vector Index Retriever

---

## Exact Keyword Search

Use:

BM25 Retriever

---

## Long Documents

Use:

Document Summary Retriever

---

## Hierarchical Documents

Use:

Auto Merging Retriever

---

## Linked Knowledge Sources

Use:

Recursive Retriever

---

## Maximum Recall

Use:

Query Fusion Retriever

---

# Exercise 1 — Custom Hybrid Retriever

Goal:

BM25 + Vector Retriever combine karna.

### Steps

1. Create Vector Retriever
2. Create BM25 Retriever
3. Combine results
4. Remove duplicates
5. Rank results
6. Test with multiple queries

### Learning Outcome

Keyword + Semantic search combine karna.

---

# Exercise 2 — Production RAG Pipeline

Goal:

Production-ready RAG system banana.

### Components

- Retriever
- LLM
- Query Engine
- Evaluation

### Testing

Pipeline ko:

- Different queries
- Accuracy
- Relevance

ke basis par test karna.

---

# Key Takeaways

| Retriever | Strength |
|------------|------------|
| Vector | Semantic search |
| BM25 | Keyword search |
| Summary | Large documents |
| Auto Merging | Context preservation |
| Recursive | Reference traversal |
| Query Fusion | Maximum recall |

---

# Interview Revision (Very Important)

### Vector vs BM25

Vector:
Meaning-based search

BM25:
Keyword-based search

---

### Auto Merging vs Recursive

Auto Merging:
Parent-child chunks merge karta hai.

Recursive:
References follow karta hai.

---

### Why Query Fusion?

Single query limitations reduce karne ke liye.

---

### Best Production Choice?

Usually:

Hybrid Retrieval

Vector + BM25

because:

- Semantic understanding
- Exact keyword matching

dono milte hain.

---

# Final One-Line Summary

Advanced Retrievers retrieval quality improve karte hain by combining semantic search, keyword search, hierarchical context handling, reference traversal, and multi-query fusion to build stronger production-grade RAG systems.
