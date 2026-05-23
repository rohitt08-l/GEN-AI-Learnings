# Tokenization in Large Language Models (LLMs)

# Introduction

Before a Large Language Model (LLM) can understand or process text, the text must first be converted into smaller pieces called:

# Tokens

Tokenization is the process of breaking text into smaller units that the model can process mathematically.

LLMs do not directly understand:
- words
- sentences
- paragraphs

Instead, they process:
- tokens
- numerical IDs
- embeddings

Tokenization is one of the most fundamental concepts in Natural Language Processing (NLP) and Generative AI.

---

# Why Tokenization is Needed

Computers cannot directly understand human language.

For example:

```text
Python is amazing
```

A neural network cannot process raw text directly.

So the text must first be:
1. Broken into tokens
2. Converted into token IDs
3. Converted into vectors (embeddings)

Only then can the LLM process the input.

---

# What is a Token?

A token is a small unit of text.

A token can be:
- a word
- part of a word
- a character
- punctuation
- whitespace

---

# Example of Tokens

Sentence:

```text
I love artificial intelligence
```

Possible tokens:

```text
["I", " love", " artificial", " intelligence"]
```

Another tokenizer may split it differently:

```text
["I", " love", " arti", "ficial", " intelligence"]
```

Different tokenizers produce different token splits.

---

# Important Point

# Tokens are NOT always words

This is a very important concept.

Example:

```text
unbelievable
```

may become:

```text
["un", "believ", "able"]
```

This helps models:
- handle unknown words
- reduce vocabulary size
- process multiple languages efficiently

---

# Tokenization Workflow

The tokenization process generally follows these steps:

---

# Step 1 — Input Text

Example:

```text
ChatGPT helps developers.
```

---

# Step 2 — Text Splitting

The tokenizer splits text into tokens.

Example:

```text
["Chat", "G", "PT", " helps", " developers", "."]
```

---

# Step 3 — Token IDs

Each token is mapped to a numerical ID.

Example:

```text
[1834, 92, 541, 2048, 8192, 13]
```

LLMs work with token IDs internally.

---

# Step 4 — Embedding Conversion

Token IDs are converted into vectors called embeddings.

These embeddings are then processed by transformer layers.

---

# Types of Tokenization

There are multiple tokenization techniques used in NLP.

---

# 1. Word Tokenization

Splits text based on spaces.

Example:

```text
I love AI
```

becomes:

```text
["I", "love", "AI"]
```

---

# Advantages

- Simple
- Easy to understand

---

# Limitations

- Large vocabulary size
- Cannot handle unknown words properly
- Poor multilingual handling

---

# 2. Character Tokenization

Splits text into characters.

Example:

```text
ChatGPT
```

becomes:

```text
["C", "h", "a", "t", "G", "P", "T"]
```

---

# Advantages

- Handles unknown words
- Small vocabulary

---

# Limitations

- Very long sequences
- Slower processing
- Harder context understanding

---

# 3. Subword Tokenization

Most modern LLMs use subword tokenization.

Words are split into meaningful smaller parts.

Example:

```text
unhappiness
```

becomes:

```text
["un", "happi", "ness"]
```

---

# Advantages

- Efficient vocabulary size
- Handles rare words
- Better language understanding

---

# Popular Subword Methods

- BPE (Byte Pair Encoding)
- WordPiece
- SentencePiece

---

# Byte Pair Encoding (BPE)

BPE is one of the most widely used tokenization methods.

Used in:
- GPT models
- OpenAI tokenizers

---

# How BPE Works

BPE:
1. Starts with characters
2. Finds frequently occurring pairs
3. Merges frequent pairs repeatedly

Example:

```text
l o w
l o w e r
n e w e s t
```

Frequent pairs are merged gradually.

---

# Why BPE is Powerful

It balances:
- vocabulary size
- sequence length
- efficiency

It also handles:
- unknown words
- spelling variations
- multilingual text

---

# WordPiece Tokenization

Used in:
- BERT
- Google NLP models

Example:

```text
playing
```

may become:

```text
["play", "##ing"]
```

The `##` indicates continuation of a word.

---

# SentencePiece

Used in:
- T5
- LLaMA
- multilingual models

Works directly on raw text without preprocessing.

---

# Special Tokens in LLMs

LLMs use special tokens for specific purposes.

---

# Common Special Tokens

| Token | Purpose |
|---|---|
| `<BOS>` | Beginning of sentence |
| `<EOS>` | End of sentence |
| `<PAD>` | Padding |
| `<UNK>` | Unknown token |
| `<CLS>` | Classification token |

---

# Context Window

LLMs can only process a limited number of tokens at one time.

This limit is called the:

# Context Window

Examples:
- 4K tokens
- 8K tokens
- 32K tokens
- 128K tokens

---

# Why Context Window Matters

A larger context window allows:
- longer conversations
- larger documents
- better memory
- document understanding

---

# Token Limits in APIs

Most AI APIs charge based on:
- input tokens
- output tokens

More tokens:
- increase cost
- increase latency
- require more memory

---

# Approximate Token Rules

These are rough estimates:

| Text | Approx Tokens |
|---|---|
| 1 word | 1–2 tokens |
| 100 words | 130 tokens |
| 1 paragraph | 100–300 tokens |

---

# Tokenization in OpenAI Models

OpenAI uses tokenizers such as:
- tiktoken

Example:

```python
import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")

tokens = encoding.encode("Hello world")

print(tokens)
```

---

# Decoding Tokens

Token IDs can also be converted back into text.

Example:

```python
decoded = encoding.decode(tokens)

print(decoded)
```

---

# Why Tokenization is Important in LLMs

Tokenization directly affects:
- model performance
- cost
- speed
- memory usage
- context understanding

Efficient tokenization improves:
- scalability
- inference quality
- multilingual support

---

# Real-World Applications

---

# 1. Chatbots

Breaking user input into processable tokens.

---

# 2. Machine Translation

Converting multilingual text efficiently.

---

# 3. Search Engines

Semantic text processing.

---

# 4. AI Coding Assistants

Processing code tokens.

---

# Tokenization Challenges

---

# 1. Rare Words

Handling uncommon or invented words.

---

# 2. Multiple Languages

Different languages require different tokenization strategies.

---

# 3. Emojis & Symbols

Handling:
- emojis
- punctuation
- special characters

---

# 4. Long Documents

Large documents create huge token counts.

---

# Important Terms

| Term | Meaning |
|---|---|
| Token | Small text unit |
| Tokenization | Splitting text into tokens |
| Vocabulary | Set of known tokens |
| Token ID | Numerical representation of token |
| Context Window | Maximum tokens model can process |
| BPE | Byte Pair Encoding |
| Embedding | Vector representation of token |

---

# Interview Questions

## 1. What is tokenization?

Tokenization is the process of converting text into smaller units called tokens.

---

## 2. Why do LLMs use tokenization?

Because neural networks cannot directly process raw text.

---

## 3. What are tokens?

Tokens are small units of text such as:
- words
- subwords
- characters
- punctuation

---

## 4. Which tokenization method is commonly used in GPT models?

Byte Pair Encoding (BPE).

---

## 5. What is a context window?

The maximum number of tokens an LLM can process at one time.

---

# Summary

Tokenization is the process of converting text into smaller processable units called tokens.

It is a foundational concept in Large Language Models because neural networks cannot directly understand raw text.

Modern LLMs mainly use subword tokenization methods such as:
- BPE
- WordPiece
- SentencePiece

Efficient tokenization improves:
- language understanding
- scalability
- multilingual support
- model performance