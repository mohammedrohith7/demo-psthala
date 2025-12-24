# UAT Environment Management Runbook

## Overview
This runbook details the procedures for provisioning, maintaining, and validating the User Acceptance Testing (UAT) environment for the GenAI MLOps platform.

## 1. Environment Provisioning
The UAT environment is provisioned using Terraform via GitLab CI.

### Steps:
1. **Trigger Provisioning**:
   - Go to GitLab Pipelines.
   - Run the manual job `provision_uat`.
   - This applies Terraform with `-var="environment=uat"`.
   
2. **Resources Created**:
   - Resource Group: `rg-genai-mlops-uat`
   - OpenAI Resource: `oai-genai-mlops-uat`
   - AI Search (VectorDB): `search-genai-mlops-uat`
   - API Management: `apim-genai-mlops-uat`

## 2. Configuration Management
Configuration is handled via Environment Variables and `src/core/config.py`.
- **Environment**: UAT keys are injected via GitLab CI/CD Secrets.
- **Config**: `SERVICENOW_ENDPOINT`, `KB_API_ENDPOINT`, etc., are parameterized.

## 3. Data Seeding
To validate the chatbot, the UAT environment must be seeded.

### Steps:
1. **Automated Seeding**:
   - The `seed_uat` job runs automatically after `provision_uat` succeeds in the UAT branch/tag.
   - It runs `src/scripts/seed_uat_data.py`.
   
2. **Data Mocked**:
   - ServiceNow Incidents
   - Knowledge Base Articles
   - MIG Topology
   - D2Ops Metrics
   - IaC Templates

## 4. AI Red Teaming (Security)
We partner with the AI Attack Team.
- **Job**: `ai_security_scan`
- **Action**: Monitor this job for vulnerability reports.
- **Details**: See [SECURITY_AI_RED_TEAM.md](SECURITY_AI_RED_TEAM.md).
