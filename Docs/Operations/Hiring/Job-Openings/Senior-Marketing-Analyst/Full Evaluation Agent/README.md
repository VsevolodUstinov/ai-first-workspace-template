# FULL EVALUATION AGENT
*[TEMPLATE EXAMPLE - This is a functional evaluation agent for demonstration purposes]*

This automated agent evaluates candidates for the Senior Marketing Analyst role by analyzing their resumes, interview notes, and other relevant documents.

## Template Configuration

**Before using this agent in your company:**

1. **Replace Company Name Placeholder:**
   - In `agent-prompt.md`: Replace `[COMPANY_NAME]` with your actual company name
   - In `agent.py`: Replace `[COMPANY_NAME]` with your actual company name (appears in 3 locations)

2. **Customize Evaluation Criteria:**
   - Modify the competencies list in `agent.py` to match your specific requirements
   - Update scoring thresholds in `agent-config.json`
   - Adjust the context files to point to your actual job requirements

3. **Set Up Directory Structure:**
   - Ensure your candidate folders follow the expected naming convention
   - Place the agent in the correct relative position to your candidates directory

## Quick Start for Template Users

1. **Setup:**
   ```bash
   # Install dependencies
   pip install markdown
   
   # Replace company name placeholders
   sed -i 's/\[COMPANY_NAME\]/YourCompany/g' agent-prompt.md
   sed -i 's/\[COMPANY_NAME\]/YourCompany/g' agent.py
   ```

2. **Run evaluation:**
   ```bash
   # Make script executable
   chmod +x run-agent.sh
   
   # Evaluate all candidates
   ./run-agent.sh
   
   # Or evaluate specific candidate
   ./run-agent.sh --candidate Candidate-John-Doe
   ```

3. **Customize for your needs:**
   - Modify competencies in `agent.py`
   - Adjust scoring rules in `agent-config.json`
   - Update context files paths as needed

## Overview

The agent uses AI-powered analysis to:

1. Read candidate resumes and other documents
2. Compare candidate qualifications against the role requirements
3. Generate evaluation scores across key competencies
4. Produce comprehensive evaluations and final scores
5. Automatically create Fathom summaries for quick review

> **⚠️ IMPORTANT NOTE:** This is a demonstration agent that uses placeholder scoring logic. For production use, you need to integrate it with a real LLM API (OpenAI, Anthropic, etc.) or custom AI model to perform actual intelligent evaluation of candidate materials.

## Setup Requirements

- Python 3.7 or higher
- Required Python packages:
  - markdown
  - argparse

You can install the required packages using pip:

```
pip install markdown
```

## Directory Structure

The agent expects a specific directory structure:

```
Senior-Marketing-Analyst/
├── Scoring-Rules.md
├── Role-Competency-Matrix.md
├── Position-Description.md
├── Candidates/
│   ├── Candidate-John-Doe/
│   │   ├── CV.md
│   │   ├── ...
│   └── Other candidates...
└── Agent/
    ├── agent.py
    ├── agent-config.json
    └── README.md (this file)
```

## Configuration

The agent is configured via the `agent-config.json` file. Key settings include:

- Context files to read for evaluation criteria
- Weightings for different competency areas
- Minimum score threshold for passing candidates
- Output file settings

## Usage

To evaluate all candidates:

```bash
python agent.py
```

To evaluate a specific candidate:

```bash
python agent.py --candidate Candidate-John-Doe
```

## Output Files

For each candidate, the agent generates:

1. **Evaluation.md** - Detailed evaluation with scores and notes
2. **Final-Score.md** - Simple pass/fail and final score
3. **AI-Notes.md** - Additional AI-generated insights about the candidate

## Human Approval

By default, the agent requires human approval before finalizing evaluations. This setting can be adjusted in the configuration file.

## Adding New Candidates

Place new candidate folders in the `Candidates/` directory following the naming convention `Candidate-[Name]`. The agent will automatically discover and evaluate them. 