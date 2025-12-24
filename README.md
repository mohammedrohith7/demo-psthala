# Azure GenAI MLOps Platform

## Overview
This repository contains the source code and infrastructure definitions for an industry-standard GenAI MLOps platform on Azure. It supports strict environment isolation (Dev vs UAT) and connects with external Data & Security teams.

## Features
- **Infrastructure as Code**: Terraform-managed Azure resources (OpenAI, Search, APIM).
- **Environment Isolation**: Dedicated UAT environment with parameterized configs.
- **Data Seeding**: Automated scripts to seed UAT with sanitized enterprise data (ServiceNow, KB, MIG).
- **Security**: Integrated AI Red Teaming workflows.

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Run locally: `make run`
3. Deploy: Use GitLab CI pipelines.

## Documentation
- [Runbook (UAT Setup)](docs/RUNBOOK.md)
- [AI Security & Red Teaming](docs/SECURITY_AI_RED_TEAM.md)
