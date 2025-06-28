# [COMPANY_NAME] Screening Agent
*[TEMPLATE EXAMPLE - This is a functional screening agent for demonstration purposes]*

This automated agent assists with the initial screening of candidates for the Senior Marketing Analyst role by analyzing their CVs and screening interview notes.

## Template Configuration

**Before using this agent in your company:**

1. **Replace Company Name Placeholder:**
   - In `agent-prompt.md`: Replace `[COMPANY_NAME]` with your actual company name
   - In `agent.py`: Replace `[COMPANY_NAME]` with your actual company name
   - In `agent-config.json`: Replace `[COMPANY_NAME]` with your actual company name
   - In `run-agent.sh`: Replace `[COMPANY_NAME]` with your actual company name

2. **Customize Evaluation Criteria:**
   - Modify the critical competencies in `agent-config.json`
   - Update fit thresholds based on your hiring standards
   - Adjust the red flags and role expectation factors

3. **Set Up Directory Structure:**
   - Ensure your global rules files exist in the expected locations
   - Update file paths in `agent-config.json` if your structure differs

## Overview

The screening agent uses AI-powered analysis to:

1. Review candidate CVs and screening interview transcripts
2. Evaluate candidate suitability based on initial impressions
3. Assess alignment with role requirements
4. Generate structured screening evaluations
5. Provide recommendations on next steps in the hiring process

> **⚠️ IMPORTANT NOTE:** This is a demonstration agent that uses placeholder screening logic. For production use, you need to integrate it with a real LLM API (OpenAI, Anthropic, etc.) or custom AI model to perform actual intelligent evaluation of candidate materials.

## Quick Start for Template Users

1. **Setup:**
   ```bash
   # Install dependencies
   pip install markdown
   
   # Replace company name placeholders
   sed -i 's/\[COMPANY_NAME\]/YourCompany/g' agent-prompt.md
   sed -i 's/\[COMPANY_NAME\]/YourCompany/g' agent.py
   sed -i 's/\[COMPANY_NAME\]/YourCompany/g' agent-config.json
   sed -i 's/\[COMPANY_NAME\]/YourCompany/g' run-agent.sh
   ```

2. **Run screening:**
   ```bash
   # Make script executable
   chmod +x run-agent.sh
   
   # Screen all candidates
   ./run-agent.sh
   
   # Or screen specific candidate
   ./run-agent.sh --candidate Candidate-John-Doe
   ```

3. **Customize for your needs:**
   - Modify critical competencies in `agent-config.json`
   - Adjust red flags and role expectation factors
   - Update file paths for your directory structure

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
├── Global-Rules/
│   ├── General-Hiring-Policy.md
│   ├── Scoring-Framework.md
│   └── Interview-Guidelines.md
├── Position-Description.md
├── Role-Competency-Matrix.md
├── Candidates/
│   ├── Candidate-John-Doe/
│   │   ├── CV.md
│   │   ├── Fathom-Screening-Interview.md
│   │   └── ...
│   └── Other candidates...
└── Screening-Agent/
    ├── agent.py
    ├── agent-config.json
    ├── agent-prompt.md
    └── README.md (this file)
```

## Configuration

The agent is configured via the `agent-config.json` file. Key settings include:

- Context files that define evaluation criteria
- Critical competencies for the role
- Fit thresholds for candidate evaluation
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

1. **Screening-Evaluation.md** - Initial evaluation with recommendations
2. **AI-Notes.md** - Additional AI-generated insights about the candidate

## Human Approval

By default, the agent requires human approval before finalizing evaluations. This setting can be adjusted in the configuration file.

## Relationship to Full Evaluation Agent

The Screening Agent works alongside the Full Evaluation Agent in a two-stage process:

1. **Screening Agent**: Performs initial candidate screening based on CV and screening interview
2. **Full Evaluation Agent**: Conducts comprehensive evaluation including technical interview results

This allows for a more efficient hiring process by quickly identifying promising candidates for more in-depth evaluation. 