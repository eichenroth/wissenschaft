# Wissenschaft

Command line tool to ask questions against your PDF database.  
Perfect for the writing of your masters-thesis.

This tool uses [LangChain](https://github.com/langchain-ai/langchain) and is inspired by [notion-qa](https://github.com/hwchase17/notion-qa).

# How to

#### 1) Install the requirements and enter your environment

```bash
poetry install
poetry shell
```

#### 2) Add your PDFs to the `assets` directory.

#### 3) Create your index

```bash
OPENAI_API_KEY={{YOUR_API_KEY}} python load.py
```

#### 4) Ask your questions

```bash
OPENAI_API_KEY={{YOUR_API_KEY}} python question.py "What is the meaning of life?"
```
