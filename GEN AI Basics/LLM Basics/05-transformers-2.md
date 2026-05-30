# Feed Forward Neural Networks (FFN)

After the Multi-Head Attention layer processes the relationships between words, the output is passed to a Feed Forward Neural Network (FFN).

The FFN helps the model:

- Learn complex patterns
- Extract higher-level features
- Improve token representations
- Increase model capacity

---

# How FFN Works

A Feed Forward Network consists of:

1. Input Layer
2. Hidden Layer
3. Output Layer

Workflow:

```text
Attention Output
        ↓
Linear Layer
        ↓
Activation Function
        ↓
Linear Layer
        ↓
Output
```

---

# Why FFN is Needed

Attention helps the model understand relationships between words.

FFN helps the model learn deeper patterns from those relationships.

Think of it as:

```text
Attention → Understanding Relationships

FFN → Learning Complex Features
```

---

# Example

Sentence:

```text
The doctor treated the patient.
```

Attention identifies relationships:

```text
doctor ↔ treated
treated ↔ patient
```

FFN learns higher-level concepts:

```text
medical treatment
healthcare context
doctor-patient interaction
```

---

# Residual Connections

Deep neural networks suffer from:

- Vanishing gradients
- Training instability
- Performance degradation

To solve this problem, Transformers use:

# Residual Connections

---

# Concept

Instead of passing only:

```text
Layer Output
```

the model adds:

```text
Layer Output + Original Input
```

Formula:

```text
Output = Layer(Input) + Input
```

---

# Why Residual Connections Help

Benefits:

- Easier training
- Better gradient flow
- Faster convergence
- Allows deeper networks

---

# Example

Without residual connection:

```text
Input
 ↓
Layer
 ↓
Output
```

With residual connection:

```text
Input
  ↘
   Layer
  ↙
Output + Input
```

This preserves important information.

---

# Layer Normalization

Training deep neural networks can cause numerical instability.

Values may become:

- Too large
- Too small

This slows learning.

To solve this problem:

Transformers use Layer Normalization.

---

# Purpose of Layer Normalization

Layer Normalization helps:

- Stabilize training
- Improve convergence
- Reduce training time
- Improve model performance

---

# Workflow

```text
Attention Output
       ↓
Add Residual Connection
       ↓
Layer Normalization
       ↓
Feed Forward Network
       ↓
Add Residual Connection
       ↓
Layer Normalization
```

---

# Encoder Architecture

The original Transformer consists of:

```text
Encoder
   ↓
Decoder
```

The Encoder is responsible for:

- Understanding input text
- Capturing context
- Building representations

---

# Encoder Workflow

```text
Input Text
      ↓
Embeddings
      ↓
Positional Encoding
      ↓
Multi-Head Attention
      ↓
Feed Forward Network
      ↓
Output Representation
```

---

# What Does Encoder Do?

Example:

```text
The cat sat on the mat.
```

The Encoder learns:

- grammatical structure
- semantic meaning
- contextual relationships

The output becomes a rich representation of the sentence.

---

# Encoder-Based Models

Examples:

- BERT
- RoBERTa
- ALBERT
- DistilBERT

Applications:

- Sentiment Analysis
- Text Classification
- Named Entity Recognition
- Semantic Search

---

# Decoder Architecture

The Decoder is responsible for:

- Generating output
- Predicting next tokens
- Producing text

---

# Decoder Workflow

```text
Previous Tokens
        ↓
Embeddings
        ↓
Positional Encoding
        ↓
Masked Multi-Head Attention
        ↓
Feed Forward Network
        ↓
Next Token Prediction
```

---

# Why Decoder Uses Masking

When generating text:

The model must not see future words.

Example:

```text
I love _____
```

The model should predict:

```text
AI
```

without seeing future tokens.

Masking ensures this.

---

# Decoder-Based Models

Examples:

- GPT
- GPT-2
- GPT-3
- GPT-4
- LLaMA
- Claude
- Gemini

Applications:

- Text Generation
- Chatbots
- Code Generation
- Summarization

---

# Encoder vs Decoder

| Feature | Encoder | Decoder |
|----------|----------|----------|
| Purpose | Understand Input | Generate Output |
| Direction | Bidirectional | Left-to-Right |
| Text Generation | Limited | Excellent |
| Example | BERT | GPT |

---

# Bidirectional vs Autoregressive Learning

## Encoder

Looks at:

```text
Previous Words
+
Future Words
```

Example:

```text
The bank is near the river.
```

Encoder sees the entire sentence.

---

## Decoder

Looks only at:

```text
Previous Words
```

Example:

```text
The bank is ...
```

Decoder predicts one token at a time.

---

# Types of Transformer Models

Modern Transformer models fall into three categories.

---

# 1. Encoder-Only Models

Examples:

- BERT
- RoBERTa

Best For:

- Search
- Classification
- Understanding tasks

---

# 2. Decoder-Only Models

Examples:

- GPT
- LLaMA
- Claude

Best For:

- Text Generation
- Chatbots
- Coding Assistants

---

# 3. Encoder-Decoder Models

Examples:

- T5
- BART

Best For:

- Translation
- Summarization
- Question Answering

---

# Transformer Workflow (Complete)

Step 1:

Input Text

```text
I love AI
```

---

Step 2:

Tokenization

```text
["I", "love", "AI"]
```

---

Step 3:

Token IDs

```text
[101, 205, 789]
```

---

Step 4:

Embeddings

Convert token IDs into vectors.

---

Step 5:

Positional Encoding

Add sequence information.

---

Step 6:

Multi-Head Attention

Understand relationships between words.

---

Step 7:

Feed Forward Networks

Learn deeper features.

---

Step 8:

Residual Connections

Preserve information.

---

Step 9:

Layer Normalization

Stabilize training.

---

Step 10:

Output Prediction

Generate next token or representation.

---

# GPT vs BERT

## GPT

Uses:

```text
Decoder-Only Transformer
```

Strengths:

- Text generation
- Chatbots
- Coding assistance
- Creative writing

Examples:

- ChatGPT
- GPT-4

---

## BERT

Uses:

```text
Encoder-Only Transformer
```

Strengths:

- Understanding language
- Classification
- Search
- Semantic analysis

Examples:

- Google Search
- NLP classification systems

---

# Why Transformers Became So Popular

Transformers offer:

- Better context understanding
- Faster training
- Massive scalability
- State-of-the-art performance

This made them the foundation of modern AI.

---

# Advantages of Transformers

## 1. Parallel Processing

Processes all tokens simultaneously.

---

## 2. Better Long-Range Context

Captures relationships between distant words.

---

## 3. Scalability

Can be trained with billions of parameters.

---

## 4. Superior Performance

Outperforms older architectures on most NLP tasks.

---

## 5. Transfer Learning

Pretrained models can be reused for many tasks.

---

# Limitations of Transformers

## 1. High Computational Cost

Require powerful GPUs or TPUs.

---

## 2. Large Memory Consumption

Processing long documents is expensive.

---

## 3. Context Window Limitations

Cannot remember unlimited information.

---

## 4. Training Cost

Training large models costs millions of dollars.

---

# Real-World Applications

## Chatbots

- ChatGPT
- Claude
- Gemini

---

## Search Engines

- Google Search
- Semantic Search

---

## Translation

- Google Translate
- DeepL

---

## Recommendation Systems

- Netflix
- YouTube
- Spotify

---

## AI Coding Assistants

- GitHub Copilot
- Cursor
- Codeium

---

## Healthcare

- Medical report generation
- Drug discovery
- Clinical summarization

---

# Important Terms

| Term | Meaning |
|--------|---------|
| Transformer | Deep learning architecture introduced in 2017 |
| Attention | Mechanism to focus on important words |
| Multi-Head Attention | Multiple attention heads working together |
| Encoder | Understands input |
| Decoder | Generates output |
| FFN | Feed Forward Network |
| Residual Connection | Skip connection for stable training |
| Layer Normalization | Stabilizes learning |
| Positional Encoding | Adds word order information |

---

# Interview Questions

## 1. What problem did Transformers solve?

They solved the limitations of RNNs and LSTMs by introducing Attention and Parallel Processing.

---

## 2. Why are Transformers faster than RNNs?

Because they process all tokens simultaneously rather than sequentially.

---

## 3. What is the most important innovation in Transformers?

Attention Mechanism.

---

## 4. What is Multi-Head Attention?

Multiple attention mechanisms working in parallel to learn different relationships.

---

## 5. Why is Positional Encoding required?

Because Transformers do not naturally understand word order.

---

## 6. What is the difference between Encoder and Decoder?

Encoder understands input while Decoder generates output.

---

## 7. Which architecture does GPT use?

Decoder-Only Transformer.

---

## 8. Which architecture does BERT use?

Encoder-Only Transformer.

---

## 9. What is the purpose of Residual Connections?

To improve gradient flow and stabilize training.

---

## 10. Why is Layer Normalization used?

To make training faster and more stable.

---

# Summary

Transformers are the foundation of modern Generative AI and Large Language Models.

They replaced RNNs and LSTMs by introducing:

- Attention Mechanisms
- Parallel Processing
- Better Context Understanding

The major components of a Transformer are:

- Embeddings
- Positional Encoding
- Multi-Head Attention
- Feed Forward Networks
- Residual Connections
- Layer Normalization

Transformers power nearly all modern AI systems including:

- ChatGPT
- GPT-4
- Gemini
- Claude
- BERT
- LLaMA

Understanding Transformers is essential before learning:

- Attention Mechanisms
- Self-Attention
- GPT Architecture
- BERT Architecture
- RAG Systems
- AI Agents
- Modern LLM Engineering