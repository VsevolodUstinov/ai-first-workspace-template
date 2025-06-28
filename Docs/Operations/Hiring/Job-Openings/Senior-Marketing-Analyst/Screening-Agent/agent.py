#!/usr/bin/env python3
"""
[COMPANY_NAME] Screening Agent
A tool for screening candidates for the Senior Marketing Analyst role

This script evaluates candidates based on their CV and screening interview,
producing a screening evaluation that helps determine if they should proceed
to the technical interview stage.
"""

import os
import json
import re
import datetime
import shutil
import sys
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("EvaluationAgent")

class SeniorMarketingAnalystScreeningAgent:
    """Agent that evaluates candidates for the Senior Marketing Analyst role based on their CV and screening interview."""
    
    def __init__(self, config_path=None):
        """Initialize the agent with configuration settings."""
        self.config = None
        self.candidate_data = {}
        self.evaluations = {}
        
        # Load configuration if provided
        if config_path:
            self.load_config(config_path)
            
    def load_config(self, config_path):
        """Load configuration from a JSON file."""
        try:
            with open(config_path, 'r') as f:
                self.config = json.load(f)
            logger.info(f"Configuration loaded from {config_path}")
        except Exception as e:
            logger.error(f"Failed to load configuration: {str(e)}")
            raise
            
    def load_candidate_data(self, candidate_folder):
        """Load candidate data from their folder."""
        try:
            # Define paths to candidate files
            cv_path = os.path.join(candidate_folder, "CV.md")
            interview_path = os.path.join(candidate_folder, "Fathom-Screening-Interview.md")
            
            # Load CV data if available
            if os.path.exists(cv_path):
                with open(cv_path, 'r') as f:
                    self.candidate_data['cv'] = f.read()
                    
            # Load interview data if available
            if os.path.exists(interview_path):
                with open(interview_path, 'r') as f:
                    self.candidate_data['interview'] = f.read()
                    
            # Check if we have enough data to proceed
            if not self.candidate_data.get('cv') or not self.candidate_data.get('interview'):
                logger.warning("Candidate CV or interview data is missing or empty")
                return False
                
            logger.info(f"Candidate data loaded from {candidate_folder}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to load candidate data: {str(e)}")
            return False
            
    def evaluate_candidate(self, candidate_folder):
        """Evaluate a candidate based on their CV and interview data."""
        # Load candidate data
        if not self.load_candidate_data(candidate_folder):
            return False
            
        # Extract name from the candidate folder or data
        candidate_name = self._extract_candidate_name()
        
        # Perform evaluation
        self._evaluate_technical_skills()
        self._evaluate_experience()
        self._evaluate_fit()
        
        # Generate outputs
        self._generate_screening_evaluation(candidate_folder, candidate_name)
        self._generate_ai_notes(candidate_folder)
        
        logger.info(f"Evaluation completed for candidate: {candidate_name}")
        return True
        
    def _extract_candidate_name(self):
        """Extract the candidate's name from their data."""
        # Try to extract from CV
        if self.candidate_data.get('cv'):
            # Look for name at the beginning of CV (usually first line)
            lines = self.candidate_data['cv'].split('\n')
            if lines:
                # Return first non-empty line as the name
                for line in lines:
                    if line.strip():
                        return line.strip()
        
        # If we couldn't extract the name, return a generic placeholder
        return "Candidate"
        
    def _evaluate_technical_skills(self):
        """Evaluate the candidate's technical skills based on CV and interview."""
        # This is a simplified implementation
        self.evaluations['technical_skills'] = {
            'sql_expertise': self._assess_sql_expertise(),
            'etl_experience': self._assess_etl_experience(),
            'api_integration': self._assess_api_experience(),
            'data_modeling': self._assess_data_modeling(),
            'analytics_tools': self._assess_analytics_tools()
        }
        
    def _evaluate_experience(self):
        """Evaluate the candidate's relevant experience."""
        # This is a simplified implementation
        self.evaluations['experience'] = {
            'marketing_analytics': self._assess_marketing_analytics_experience(),
            'client_communication': self._assess_client_communication(),
            'documentation': self._assess_documentation_experience()
        }
        
    def _evaluate_fit(self):
        """Evaluate the candidate's fit for the role and company."""
        # This is a simplified implementation
        self.evaluations['fit'] = {
            'culture_fit': self._assess_culture_fit(),
            'language_skills': self._assess_language_skills(),
            'salary_expectations': self._assess_salary_expectations()
        }
    
    # Assessment methods for specific skills
    def _assess_sql_expertise(self):
        """Assess the candidate's SQL expertise."""
        # Look for SQL mentions in CV and interview
        cv = self.candidate_data.get('cv', '').lower()
        interview = self.candidate_data.get('interview', '').lower()
        
        # Check for SQL mentions
        sql_mentions = len(re.findall(r'\bsql\b', cv + interview))
        postgres_mentions = len(re.findall(r'\bpostgre(s|sql)\b', cv + interview))
        advanced_sql = any(term in cv + interview for term in ['window function', 'cte', 'join', 'subquery'])
        
        if sql_mentions > 5 and advanced_sql:
            return "Strong"
        elif sql_mentions > 2 or postgres_mentions > 0:
            return "Mentioned in CV"
        else:
            return "Not mentioned"
    
    def _assess_etl_experience(self):
        """Assess the candidate's ETL experience."""
        cv = self.candidate_data.get('cv', '').lower()
        interview = self.candidate_data.get('interview', '').lower()
        
        etl_terms = ['etl', 'extract', 'transform', 'load', 'data pipeline', 'data integration']
        etl_mentions = sum(1 for term in etl_terms if term in cv + interview)
        
        if etl_mentions >= 3:
            return "Strong"
        elif etl_mentions > 0:
            return "Mentioned"
        else:
            return "Missing"
    
    def _assess_api_experience(self):
        """Assess the candidate's API integration experience."""
        cv = self.candidate_data.get('cv', '').lower()
        interview = self.candidate_data.get('interview', '').lower()
        
        api_terms = ['api', 'rest', 'json', 'integration', 'http']
        api_mentions = sum(1 for term in api_terms if term in cv + interview)
        
        if api_mentions >= 3:
            return "Strong"
        elif api_mentions > 0:
            return "Mentioned"
        else:
            return "Missing"
    
    def _assess_data_modeling(self):
        """Assess the candidate's data modeling experience."""
        cv = self.candidate_data.get('cv', '').lower()
        interview = self.candidate_data.get('interview', '').lower()
        
        modeling_terms = ['data model', 'schema', 'database design', 'entity relationship']
        mentions = sum(1 for term in modeling_terms if term in cv + interview)
        
        if mentions >= 2:
            return "Strong"
        elif mentions > 0 or "set up analytics" in cv + interview:
            return "Self-Reported"
        else:
            return "Not mentioned"
    
    def _assess_analytics_tools(self):
        """Assess the candidate's experience with analytics tools."""
        cv = self.candidate_data.get('cv', '').lower()
        interview = self.candidate_data.get('interview', '').lower()
        
        tools = {
            'google_analytics': ['google analytics', 'ga4', 'universal analytics'],
            'power_bi': ['power bi', 'powerbi', 'power-bi'],
            'tableau': ['tableau'],
            'python': ['python', 'pandas', 'numpy'],
            'r': [' r ', ' r,', 'r programming', 'r language']
        }
        
        results = {}
        for tool, terms in tools.items():
            tool_mentions = sum(1 for term in terms if term in cv + interview)
            if tool_mentions >= 2:
                results[tool] = "Strong"
            elif tool_mentions > 0:
                results[tool] = "Mentioned in CV"
            else:
                results[tool] = "Not mentioned"
                
        return results
    
    def _assess_marketing_analytics_experience(self):
        """Assess the candidate's marketing analytics experience."""
        cv = self.candidate_data.get('cv', '').lower()
        interview = self.candidate_data.get('interview', '').lower()
        
        marketing_terms = ['marketing analytics', 'digital marketing', 'campaign', 'attribution']
        platforms = ['google ads', 'facebook ads', 'instagram ads', 'yandex direct']
        
        marketing_mentions = sum(1 for term in marketing_terms if term in cv + interview)
        platform_mentions = sum(1 for platform in platforms if platform in cv + interview)
        
        if marketing_mentions >= 3 and platform_mentions >= 2:
            return "Strong"
        elif marketing_mentions > 0 or platform_mentions > 0:
            return "Mentioned in CV"
        else:
            return "Not mentioned"
    
    def _assess_client_communication(self):
        """Assess the candidate's client communication experience."""
        cv = self.candidate_data.get('cv', '').lower()
        interview = self.candidate_data.get('interview', '').lower()
        
        client_terms = ['client', 'stakeholder', 'presentation', 'report', 'communicate']
        client_mentions = sum(1 for term in client_terms if term in cv + interview)
        
        if client_mentions >= 3:
            return "Strong"
        elif client_mentions > 0:
            return "Self-Reported"
        else:
            return "Not mentioned"
    
    def _assess_documentation_experience(self):
        """Assess the candidate's experience with documentation."""
        cv = self.candidate_data.get('cv', '').lower()
        interview = self.candidate_data.get('interview', '').lower()
        
        doc_terms = ['documentation', 'technical writing', 'specification', 'report', 'presentation']
        doc_mentions = sum(1 for term in doc_terms if term in cv + interview)
        
        if doc_mentions >= 3:
            return "Strong"
        elif doc_mentions > 0:
            return "Self-Reported"
        else:
            return "Not mentioned"
    
    def _assess_culture_fit(self):
        """Assess the candidate's potential culture fit."""
        interview = self.candidate_data.get('interview', '').lower()
        
        positive_terms = ['team', 'collaboration', 'learning', 'growth', 'challenge', 'remote work', 'flexible']
        positive_mentions = sum(1 for term in positive_terms if term in interview)
        
        if positive_mentions >= 3:
            return "Strong"
        elif positive_mentions > 0:
            return "Potential"
        else:
            return "Unclear"
    
    def _assess_language_skills(self):
        """Assess the candidate's language skills."""
        cv = self.candidate_data.get('cv', '').lower()
        interview = self.candidate_data.get('interview', '').lower()
        
        english_patterns = [
            r'english.{1,20}(c1|c2|advanced|fluent|proficient)',
            r'(c1|c2|advanced|fluent|proficient).{1,20}english'
        ]
        
        russian_patterns = [
            r'russian.{1,20}(native|fluent|mother tongue)',
            r'(native|fluent|mother tongue).{1,20}russian'
        ]
        
        english_level = None
        for pattern in english_patterns:
            match = re.search(pattern, cv + interview)
            if match:
                english_level = "Mentioned in CV"
                break
                
        russian_level = None
        for pattern in russian_patterns:
            match = re.search(pattern, cv + interview)
            if match:
                russian_level = "Mentioned in CV"
                break
                
        return {
            'english': english_level or "Not mentioned",
            'russian': russian_level or "Not mentioned"
        }
    
    def _assess_salary_expectations(self):
        """Assess if the candidate's salary expectations are within range."""
        interview = self.candidate_data.get('interview', '').lower()
        
        # Look for salary mentions in the interview
        salary_patterns = [
            r'salary.{1,50}(\d[\d\s,.]+)',
            r'compensation.{1,50}(\d[\d\s,.]+)',
            r'expecting.{1,50}(\d[\d\s,.]+)',
            r'(\d[\d\s,.]+).{1,20}(usd|eur|euro|dollar)'
        ]
        
        for pattern in salary_patterns:
            match = re.search(pattern, interview)
            if match:
                # Very basic check - in a real implementation would need to normalize currency
                return "Self-Reported"
                
        return "Not mentioned"
    
    def _generate_screening_evaluation(self, candidate_folder, candidate_name):
        """Generate a screening evaluation document."""
        try:
            output_path = os.path.join(candidate_folder, self.config['candidateEvaluationSettings']['outputFiles']['screening'])
            
            # Build content sections
            summary = self._build_summary_section(candidate_name)
            competency_table = self._build_competency_table()
            decision = self._build_decision_section()
            concerns = self._build_concerns_section()
            
            # Combine sections into full document
            content = f"""# Screening Evaluation: {candidate_name}

## Summary
{summary}

## Competency Evidence Table

{competency_table}

## Preliminary Decision
{decision}

## Concerns
{concerns}

## Initial Impression
[Initial impression of the candidate]

## Experience Alignment
[Assessment of how candidate's experience aligns with the role]

## Technical Skills (Initial Assessment)
[Initial assessment of technical capabilities]

## Cultural Fit
[Assessment of cultural fit]

## Recommended Next Steps
- [ ] Proceed to Technical Interview
- [ ] Request Additional Information
- [ ] Reject Candidacy

## Notes
[Additional notes on screening evaluation] 
"""
            
            # Write to file
            with open(output_path, 'w') as f:
                f.write(content)
                
            logger.info(f"Screening evaluation saved to {output_path}")
            
        except Exception as e:
            logger.error(f"Failed to generate screening evaluation: {str(e)}")
    
    def _generate_ai_notes(self, candidate_folder):
        """Generate AI notes document with more detailed analysis."""
        try:
            output_path = os.path.join(candidate_folder, self.config['candidateEvaluationSettings']['outputFiles']['aiNotes'])
            
            content = """# AI Analysis Notes

## CV Analysis
[AI analysis of candidate CV]

## Interview Analysis
[AI analysis of screening interview]

## Technical Skills Assessment
[AI assessment of technical skills]

## Cultural Fit Assessment
[AI assessment of cultural fit]

## Recommended Questions for Follow-up
[List of recommended questions for next interview stage] 
"""
            
            # Write to file
            with open(output_path, 'w') as f:
                f.write(content)
                
            logger.info(f"AI notes saved to {output_path}")
            
        except Exception as e:
            logger.error(f"Failed to generate AI notes: {str(e)}")
    
    def _build_summary_section(self, candidate_name):
        """Build the summary section of the evaluation."""
        # In a real implementation, this would use NLG or a templating system
        # This is a simplified placeholder
        return f"{candidate_name} is a candidate for the Senior Marketing Analyst position. Further screening is needed to assess their qualifications."
    
    def _build_competency_table(self):
        """Build the competency evidence table."""
        table = """| Competency          | Status             | Notes                                                   |
|---------------------|--------------------|---------------------------------------------------------|
| SQL Expert          | [Status]           | [Details based on CV and interview]                      |
| ETL & Data Pipelines| [Status]           | [Details based on CV and interview]                      |
| API Integration     | [Status]           | [Details based on CV and interview]                      |
| Data Modeling       | [Status]           | [Details based on CV and interview]                      |
| Marketing Analytics | [Status]           | [Details based on CV and interview]                      |
| Web Analytics Tools | [Status]           | [Details based on CV and interview]                      |
| Ad Platforms        | [Status]           | [Details based on CV and interview]                      |
| Client Communication| [Status]           | [Details based on CV and interview]                      |
| Documentation       | [Status]           | [Details based on CV and interview]                      |
| English Language    | [Status]           | [Details based on CV and interview]                      |
| Russian Language    | [Status]           | [Details based on CV and interview]                      |
| Salary Expectations | [Status]           | [Details based on CV and interview]                      |"""
        
        return table
    
    def _build_decision_section(self):
        """Build the preliminary decision section."""
        return "**[Decision Placeholder]**"
    
    def _build_concerns_section(self):
        """Build the concerns section."""
        return "1. [Concern 1]\n2. [Concern 2]\n3. [Concern 3]"
    
    def create_candidate_folder(self, job_opening_path, candidate_name):
        """Create a folder for a new candidate with template files."""
        try:
            # Create candidate folder path
            candidate_folder_name = f"Candidate-{candidate_name}"
            candidate_folder_path = os.path.join(job_opening_path, "Candidates", candidate_folder_name)
            
            # Create folder if it doesn't exist
            os.makedirs(candidate_folder_path, exist_ok=True)
            
            # Create empty template files as per the new rule
            cv_path = os.path.join(candidate_folder_path, "CV.md")
            interview_path = os.path.join(candidate_folder_path, "Fathom-Screening-Interview.md")
            
            # Create empty CV and interview files
            with open(cv_path, 'w') as f:
                f.write("")  # Empty file as per the new rule
                
            with open(interview_path, 'w') as f:
                f.write("")  # Empty file as per the new rule
                
            # Create template evaluation files
            self._create_evaluation_templates(candidate_folder_path)
            
            logger.info(f"Created candidate folder for {candidate_name} at {candidate_folder_path}")
            return candidate_folder_path
            
        except Exception as e:
            logger.error(f"Failed to create candidate folder: {str(e)}")
            return None
    
    def _create_evaluation_templates(self, candidate_folder_path):
        """Create template files for evaluations."""
        try:
            # Create template screening evaluation
            screening_path = os.path.join(candidate_folder_path, self.config['candidateEvaluationSettings']['outputFiles']['screening'])
            with open(screening_path, 'w') as f:
                f.write("""# Screening Evaluation - [Candidate Name]

**DECISION: [✅ PROCEED TO TECHNICAL INTERVIEW / ❌ REJECT CANDIDACY]**

> **NOTE: This evaluation is based ONLY on the candidate's CV and screening interview. The purpose is to determine whether to proceed to the technical interview stage, not to make a final hiring decision.**

## Summary
[Provide a concise summary of the candidate's background, experience, technical skills, and relevant qualifications. Include current role, years of experience, key achievements, and educational background.]

## Competency Assessment
| Competency | Rating | Evidence |
|------------|--------|----------|
| SQL Expertise | _/5 | [Evidence of SQL skills and experience] |
| ETL & Data Pipelines | _/5 | [Evidence of ETL experience] |
| API Integration | _/5 | [Evidence of API integration experience] |
| Data Modeling | _/5 | [Evidence of data modeling skills] |
| Marketing Analytics | _/5 | [Evidence of marketing analytics experience] |
| Web Analytics Tools | _/5 | [Evidence of web analytics tool experience] |
| Power BI | _/5 | [Evidence of Power BI skills] |
| Client Communication | _/5 | [Evidence of client communication skills] |
| Documentation | _/5 | [Evidence of documentation skills] |
| English Proficiency | _/5 | [Evidence of English language skills] |
| Team Fit | _/5 | [Evidence of team compatibility] |

## Key Strengths
1. [Key strength 1]
2. [Key strength 2]
3. [Key strength 3]
4. [Key strength 4]
5. [Key strength 5]

## Concerns
- [Concern 1]
- [Concern 2]
- [Concern 3]
- [Concern 4]
- [Concern 5]

## Technical Assessment
[Provide an assessment of the candidate's technical capabilities relevant to the role. Include specific skills, tools, and methodologies they have experience with. Comment on their problem-solving approach and technical depth.]

## Cultural Fit
[Assess how well the candidate's values, working style, and communication approach align with the company culture. Include observations about remote work compatibility, adaptability, teamwork, and client interaction style.]

## Next Steps
- [ ] Proceed to Technical Interview
- [ ] Request Additional Information
- [ ] Reject Candidacy

## Notes
[Include additional observations, salary expectations, availability, and any specific areas to focus on in the technical interview if proceeding.]
""")
            
            # Create template AI notes
            ai_notes_path = os.path.join(candidate_folder_path, self.config['candidateEvaluationSettings']['outputFiles']['aiNotes'])
            with open(ai_notes_path, 'w') as f:
                f.write("""# AI Analysis Notes

## CV Analysis
[AI analysis of candidate CV]

## Interview Analysis
[AI analysis of screening interview]

## Technical Skills Assessment
[AI assessment of technical skills]

## Cultural Fit Assessment
[AI assessment of cultural fit]

## Recommended Questions for Follow-up
[List of recommended questions for next interview stage]
""")
            
            # Create template full evaluation
            evaluation_path = os.path.join(candidate_folder_path, "Evaluation.md")
            with open(evaluation_path, 'w') as f:
                f.write("""# Comprehensive Evaluation

## Technical Skills
- SQL: [Score/10]
- Power BI: [Score/10]
- API Integration: [Score/10]
- Data Processing: [Score/10]
- Technical Communication: [Score/10]

## Soft Skills
- Communication: [Score/10]
- Problem-solving: [Score/10]
- Client Interaction: [Score/10]
- Adaptability: [Score/10]
- Team Fit: [Score/10]

## Overall Assessment
[Overall assessment of candidate fit for the role]

## Hiring Recommendation
- [ ] Strong Hire
- [ ] Hire
- [ ] Consider Hiring
- [ ] Do Not Hire

[Justification for recommendation]
""")
            
            # Create template final score
            final_score_path = os.path.join(candidate_folder_path, "Final-Score.md")
            with open(final_score_path, 'w') as f:
                f.write("""# Final Candidate Score

## Technical Competency: [Score 1-10]
[Justification for score]

## Experience Relevance: [Score 1-10]
[Justification for score]

## Cultural Fit: [Score 1-10]
[Justification for score]

## Communication Skills: [Score 1-10]
[Justification for score]

## Overall Score: [Average of above scores]
""")
            
            # Create template technical interview
            tech_interview_path = os.path.join(candidate_folder_path, "Fathom-Technical-Interview.md")
            with open(tech_interview_path, 'w') as f:
                f.write("""# Technical Interview

[This file will contain the transcript or notes from the technical interview with the candidate]

## SQL Assessment
[Notes on candidate's SQL skills demonstration]

## Data Modeling Assessment
[Notes on candidate's data modeling knowledge]

## Power BI/Visualization Assessment
[Notes on candidate's visualization skills]

## API/Integration Knowledge
[Notes on candidate's API and integration knowledge]

## Technical Communication
[Assessment of how well the candidate explains technical concepts]

## Overall Technical Assessment
[Summary of technical strengths and weaknesses]
""")
            
            logger.info(f"Evaluation templates created at {candidate_folder_path}")
            
        except Exception as e:
            logger.error(f"Failed to create evaluation templates: {str(e)}")

# Main execution for command line usage
if __name__ == "__main__":
    try:
        # Parse command-line arguments
        if len(sys.argv) < 3:
            print("Usage: python agent.py <command> <arguments>")
            print("Commands:")
            print("  evaluate <candidate_folder>  - Evaluate a candidate")
            print("  create <candidate_name>      - Create a new candidate folder")
            sys.exit(1)
            
        command = sys.argv[1]
        config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "agent-config.json")
        agent = SeniorMarketingAnalystScreeningAgent(config_path)
        
        if command == "evaluate":
            candidate_folder = sys.argv[2]
            success = agent.evaluate_candidate(candidate_folder)
            if not success:
                sys.exit(1)
                
        elif command == "create":
            candidate_name = sys.argv[2]
            job_opening_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            agent.create_candidate_folder(job_opening_path, candidate_name)
            
        else:
            print(f"Unknown command: {command}")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        sys.exit(1)