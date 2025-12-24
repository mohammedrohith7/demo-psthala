# AI Security & Red Teaming

## Partnership with AI Attack Team
We collaborate with third-party DevOps AI Attack teams to ensure the robustness of our GenAI endpoints.

## Scope
- **Prompt Injection**: Validating resilience against jailbreaks.
- **Data Leakage**: Ensuring RAG pipeline does not retrieve restricted PII.
- **Model Denial of Service**: Rate limiting tests via APIM.

## Integration
The `.gitlab-ci.yml` pipeline includes a stage `security_scan`.
- This stage acts as a hook to invoke external scanning tools.
- It connects to the AI Attack Team dashboard.

### Incident Response
If a vulnerability is found:
1. **Isolate**: Block traffic to the UAT APIM endpoint.
2. **Rotate**: Regenerate OpenAI and Search keys.
3. **Patch**: Update system prompts or content filters.
4. **Re-seed**: Run `seed_uat` if data integrity is compromised.
