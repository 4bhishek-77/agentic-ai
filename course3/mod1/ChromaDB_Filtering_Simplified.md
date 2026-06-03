# ChromaDB Filtering — Simplified Notes

## Quick Idea

Filtering in ChromaDB means **narrowing down documents before or during retrieval**.

There are two types:

| Filter Type | What it Filters | Similar SQL Concept |
|------------|----------------|--------------------|
| Metadata Filtering | Metadata fields like source, year, author, version | WHERE clause |
| Document Filtering | Actual text inside documents | LIKE / CONTAINS |

---

## Metadata Filtering

### Equal ($eq)

```python
where={"source": "langchain.com"}
```

Equivalent:

```sql
WHERE source = 'langchain.com'
```

### Not Equal ($ne)

```python
where={"source":{"$ne":"langchain.com"}}
```

Equivalent:

```sql
WHERE source != 'langchain.com'
```

### Greater Than ($gt)

```python
where={"version":{"$gt":0.3}}
```

Equivalent:

```sql
WHERE version > 0.3
```

### Less Than ($lt)

```python
where={"version":{"$lt":0.3}}
```

Equivalent:

```sql
WHERE version < 0.3
```

---

## Logical Operators

### AND

```python
where={
    "$and":[
        {"source":"langchain.com"},
        {"version":{"$lt":0.3}}
    ]
}
```

Equivalent:

```sql
WHERE source='langchain.com'
AND version < 0.3
```

### OR

```python
where={
    "$or":[
        {"source":"langchain.com"},
        {"source":"llamaindex.ai"}
    ]
}
```

Equivalent:

```sql
WHERE source='langchain.com'
OR source='llamaindex.ai'
```

---

## List Operators

### IN

```python
where={
    "source":{
        "$in":["langchain.com","llamaindex.ai"]
    }
}
```

Equivalent:

```sql
WHERE source IN (...)
```

### NOT IN ($nin)

```python
where={
    "source":{
        "$nin":["langchain.com","llamaindex.ai"]
    }
}
```

Equivalent:

```sql
WHERE source NOT IN (...)
```

---

## Document Filtering

Suppose document text is:

```text
This is a document about pandas
```

### Contains

```python
where_document={
    "$contains":"pandas"
}
```

Meaning: Find documents containing "pandas".

### Not Contains

```python
where_document={
    "$not_contains":"pandas"
}
```

Meaning: Exclude documents containing "pandas".

---

## Combining Metadata + Document Filters

```python
collection.get(
    where={"version":{"$gt":0.1}},
    where_document={
        "$contains":"LangChain"
    }
)
```

Meaning:

- version > 0.1
- document contains "LangChain"

Both conditions must be satisfied.

---

## Operator Cheat Sheet

| Operator | Meaning |
|----------|---------|
| $eq | Equal |
| $ne | Not Equal |
| $gt | Greater Than |
| $gte | Greater Than or Equal |
| $lt | Less Than |
| $lte | Less Than or Equal |
| $in | Value exists in list |
| $nin | Value not in list |
| $and | All conditions true |
| $or | Any condition true |
| $contains | Text contains keyword |
| $not_contains | Text does not contain keyword |

---

## Why Useful in RAG?

Without filtering:

- Search all documents.
- More noise.

With filtering:

```python
collection.query(
    query_texts=["AI projects"],
    where={"year":2025}
)
```

Process:

1. Keep only documents where year = 2025.
2. Perform vector similarity search on those documents.

Result:

- Faster retrieval.
- More relevant answers.

---

## Interview Answer

Metadata filtering = filtering using structured fields such as source, year, tags, author, or version.

Document filtering = filtering using document text content.

ChromaDB allows combining metadata filters, document filters, and vector similarity search to retrieve highly relevant documents for RAG applications.
