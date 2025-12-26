# Azure GenAI MLOps Platform

## Overview
This repository contains the source code and infrastructure definitions for an industry-standard GenAI MLOps platform on Azure. It supports strict environment isolation (Dev vs UAT) and connects with external Data & Security teams.

## Architecture
The codebase is organized into modular components for scalability:
- **`src/ml`**: Classical Machine Learning pipelines and models.
- **`src/ai`**: General AI utilities and processing functions.
- **`src/genai`**: Generative AI service integrations (Azure OpenAI).
- **`src/rag`**: Retrieval Augmented Generation implementation using LangChain and Azure AI Search.
- **`src/llm`**: LLM evaluation metrics and management.

## Features
- **Infrastructure as Code**: Terraform-managed Azure resources (OpenAI, Search, APIM).
- **Environment Isolation**: Dedicated UAT environment with parameterized configs.
- **Data Seeding**: Automated scripts to seed UAT with sanitized enterprise data (ServiceNow, KB, MIG).
- **Security**: Integrated AI Red Teaming workflows.

## API Endpoints
- `POST /genai/generate`: Direct LLM text generation.
- `POST /rag/query`: Knowledge-base query with context retrieval.
- `POST /llm/evaluate`: Performance evaluation for LLM responses.
- `POST /ml/train`: Bootstrap classical ML training jobs.

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Run locally: `uvicorn src.app.main:app --reload`
3. Deploy: Use GitLab CI pipelines.

## Documentation
- [Runbook (UAT Setup)](docs/RUNBOOK.md)
- [AI Security & Red Teaming](docs/SECURITY_AI_RED_TEAM.md)
