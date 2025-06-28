# LLM Integration Guide
*[TEMPLATE DOCUMENTATION - Guide for implementing real AI evaluation]*

This agent currently uses placeholder logic for demonstration purposes. To make it production-ready, you need to integrate it with a real Large Language Model (LLM).

## Integration Options

### 1. OpenAI GPT Integration
```python
import openai

def evaluate_with_openai(prompt, candidate_data):
    client = openai.OpenAI(api_key="your-api-key")
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": str(candidate_data)}
        ],
        temperature=0.1
    )
    
    return response.choices[0].message.content
```

### 2. Anthropic Claude Integration
```python
import anthropic

def evaluate_with_claude(prompt, candidate_data):
    client = anthropic.Anthropic(api_key="your-api-key")
    
    response = client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=2000,
        messages=[
            {"role": "user", "content": f"{prompt}\n\nCandidate Data:\n{candidate_data}"}
        ]
    )
    
    return response.content[0].text
```

### 3. Local Model Integration (Ollama)
```python
import requests

def evaluate_with_ollama(prompt, candidate_data):
    response = requests.post('http://localhost:11434/api/generate',
        json={
            'model': 'llama2',
            'prompt': f"{prompt}\n\nCandidate Data:\n{candidate_data}",
            'stream': False
        })
    
    return response.json()['response']
```

## Implementation Steps

### Step 1: Replace Placeholder Functions
In `agent.py`, replace these methods with real LLM calls:
- `_evaluate_critical_competency()`
- `_evaluate_competency()`
- `_generate_notes()`

### Step 2: Add Environment Variables
```bash
# .env file
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
LLM_PROVIDER=openai  # or anthropic, ollama
```

### Step 3: Update Dependencies
```bash
pip install openai anthropic python-dotenv
```

### Step 4: Implement Structured Output
Use the LLM to return structured JSON for consistent scoring:

```python
evaluation_prompt = f"""
{self.prompt}

Please evaluate this candidate and return a JSON response with:
{{
    "competencyScores": {{
        "SQL Proficiency": 1-5,
        "ETL Experience": 1-5,
        // ... other competencies
    }},
    "fitResult": "Strong Fit" | "Potential Fit" | "Weak Fit",
    "notes": "Detailed explanation of concerns or strengths"
}}

Candidate Data: {candidate_data}
"""
```

## Cost Considerations

### Token Usage Estimates:
- **OpenAI GPT-4:** ~$0.03-0.06 per evaluation
- **Claude 3 Sonnet:** ~$0.015-0.03 per evaluation  
- **Local Models:** Free after setup

### Optimization Tips:
1. Cache context files to avoid re-sending
2. Use cheaper models for initial screening
3. Implement batch processing for multiple candidates
4. Set token limits to control costs

## Testing Your Integration

### Unit Tests:
```python
def test_llm_integration():
    agent = CandidateEvaluationAgent()
    test_candidate = {"files": {"CV.md": "Sample CV content"}}
    
    evaluation = agent.evaluate_candidate(test_candidate)
    
    assert "competencyScores" in evaluation
    assert evaluation["fitResult"] in ["Strong Fit", "Potential Fit", "Weak Fit"]
    assert isinstance(evaluation["notes"], str)
```

### Validation:
1. Test with known good/bad candidates
2. Compare LLM results with human evaluations
3. Monitor consistency across multiple runs
4. Validate JSON structure and scoring ranges

## Production Considerations

### Error Handling:
```python
try:
    evaluation = evaluate_with_llm(prompt, candidate_data)
except Exception as e:
    logger.error(f"LLM evaluation failed: {e}")
    # Fallback to human evaluation or default scoring
```

### Rate Limiting:
```python
import time
from functools import wraps

def rate_limit(calls_per_minute=60):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(60 / calls_per_minute)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Security:
- Store API keys securely (environment variables, secrets manager)
- Sanitize candidate data before sending to external APIs
- Implement audit logging for all LLM calls
- Consider data privacy regulations (GDPR, etc.)

---

*This guide provides the foundation for implementing real AI evaluation. Choose the LLM provider that best fits your technical requirements, budget, and data privacy needs.* 