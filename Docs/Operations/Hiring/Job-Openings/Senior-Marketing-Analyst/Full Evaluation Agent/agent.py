#!/usr/bin/env python3
"""
[COMPANY_NAME] Recruiter Assistant
-----------------------------------------
This agent evaluates candidates for the Senior Marketing Analyst role
by analyzing their materials against competency criteria.
"""

import os
import json
import argparse
import markdown
import logging
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("FullEvaluationAgent")

class CandidateEvaluationAgent:
    def __init__(self, config_path="agent-config.json"):
        """Initialize the agent with configuration settings."""
        self.config = self._load_config(config_path)
        self.context = {}
        self.candidates = []
        self.prompt = ""
        self.competencies = []
        
    def _load_config(self, config_path):
        """Load the agent configuration from JSON file."""
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading configuration: {e}")
            exit(1)
            
    def load_context(self):
        """Load all context files specified in the configuration."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        for context_type, path in self.config["contextFiles"].items():
            full_path = os.path.join(base_dir, path)
            try:
                with open(full_path, 'r') as f:
                    content = f.read()
                    self.context[context_type] = content
                    
                    # Store the prompt separately for easy access
                    if context_type == "agentPrompt":
                        self.prompt = content
                    
                    # Extract competencies from the competency matrix
                    if context_type == "competencyMatrix":
                        self.competencies = self._extract_competencies(content)
                        
                print(f"Loaded {context_type} from {path}")
            except Exception as e:
                print(f"Error loading {context_type} from {path}: {e}")
    
    def _extract_competencies(self, competency_matrix_content):
        """Extract competencies from the competency matrix content."""
        # This is a placeholder. In a real implementation, this would parse
        # the markdown to extract competency names and criteria
        # For now, returning a list of sample competencies
        return [
            "SQL Proficiency",
            "ETL Experience", 
            "API Integration",
            "Data Visualization",
            "Statistical Analysis",
            "Marketing Campaign Analysis",
            "Problem Solving",
            "Communication Skills",
            "Teamwork"
        ]
                
    def discover_candidates(self, candidates_dir="../Candidates"):
        """Discover all candidate folders in the specified directory."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_candidates_dir = os.path.join(base_dir, candidates_dir)
        
        try:
            candidate_folders = [f for f in os.listdir(full_candidates_dir) 
                               if os.path.isdir(os.path.join(full_candidates_dir, f))
                               and f.startswith("Candidate-")]
            
            self.candidates = candidate_folders
            print(f"Discovered {len(self.candidates)} candidates: {', '.join(self.candidates)}")
        except Exception as e:
            print(f"Error discovering candidates: {e}")
            
    def load_candidate_data(self, candidate_id, candidates_dir="../Candidates"):
        """Load all available data for a specific candidate."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        candidate_dir = os.path.join(base_dir, candidates_dir, candidate_id)
        
        candidate_data = {
            "id": candidate_id,
            "files": {}
        }
        
        try:
            for file in os.listdir(candidate_dir):
                if file.endswith(".md") or file.endswith(".pdf"):
                    file_path = os.path.join(candidate_dir, file)
                    with open(file_path, 'r') as f:
                        candidate_data["files"][file] = f.read()
            
            return candidate_data
        except Exception as e:
            print(f"Error loading data for candidate {candidate_id}: {e}")
            return None
            
    def evaluate_candidate(self, candidate_data):
        """Evaluate a candidate based on their data and context files."""
        if not candidate_data:
            return None
            
        # In a real implementation, this would pass the prompt and candidate data
        # to an LLM or AI system for evaluation. For demonstration purposes,
        # we're using placeholder scores.
        
        print("Using evaluation prompt to analyze candidate...")
        if self.prompt:
            # Display the first few lines of the prompt (for demonstration)
            prompt_preview = "\n".join(self.prompt.split("\n")[:3]) + "..."
            print(f"Prompt preview: {prompt_preview}")
            
        # This would be where the actual AI-powered evaluation happens
        # The AI would be given the prompt and candidate data
        
        # Generate competency scores (1-5 scale)
        competency_scores = {}
        for competency in self.competencies:
            # For critical skills, be more strict in the demo
            if competency in ["SQL Proficiency", "ETL Experience", "API Integration"]:
                score = self._evaluate_critical_competency(competency, candidate_data)
            else:
                score = self._evaluate_competency(competency, candidate_data)
            
            competency_scores[competency] = score
        
        # Determine fit based on scores
        fit_result = self._determine_fit(competency_scores)
        
        # Generate notes
        notes = self._generate_notes(candidate_data, competency_scores)
        
        evaluation = {
            "competencyScores": competency_scores,
            "fitResult": fit_result,
            "notes": notes,
            "timestamp": datetime.now().isoformat()
        }
        
        return evaluation
    
    def _evaluate_critical_competency(self, competency, candidate_data):
        """Evaluate critical competencies - being strict as per the prompt."""
        # In a real implementation, this would use LLM to analyze the candidate's
        # skills based on their documents
        
        # For demo purposes, randomly generate scores 1-4 (being strict)
        import random
        return random.randint(1, 4)
    
    def _evaluate_competency(self, competency, candidate_data):
        """Evaluate a standard competency on 1-5 scale."""
        # In a real implementation, this would use LLM to analyze
        
        # For demo purposes, randomly generate scores 2-5
        import random
        return random.randint(2, 5)
    
    def _determine_fit(self, competency_scores):
        """Determine overall fit based on competency scores."""
        # This is a simplified logic for demonstration
        # In a real implementation, this would follow the actual threshold logic
        
        # Count scores
        critical_skills = ["SQL Proficiency", "ETL Experience", "API Integration"]
        critical_scores = [competency_scores.get(skill, 0) for skill in critical_skills]
        all_scores = list(competency_scores.values())
        
        # Simple demo logic
        if min(critical_scores) >= 4 and sum(all_scores) / len(all_scores) >= 3.5:
            return "Strong Fit"
        elif min(critical_scores) >= 3 and sum(all_scores) / len(all_scores) >= 3:
            return "Potential Fit"
        else:
            return "Weak Fit"
    
    def _generate_notes(self, candidate_data, competency_scores):
        """Generate notes highlighting risks or missing data."""
        notes = []
        
        # Look for low scores
        low_scores = [comp for comp, score in competency_scores.items() if score <= 2]
        if low_scores:
            notes.append(f"Low scores in: {', '.join(low_scores)}")
        
        # Check for critical skills
        critical_skills = ["SQL Proficiency", "ETL Experience", "API Integration"]
        critical_issues = [skill for skill in critical_skills 
                          if competency_scores.get(skill, 0) < 3]
        if critical_issues:
            notes.append(f"WARNING: Insufficient critical skills in {', '.join(critical_issues)}")
        
        # Demo note about available data
        if len(candidate_data["files"]) < 2:
            notes.append("Limited data available for evaluation")
        
        return "\n".join(notes) if notes else "No significant concerns identified."
    
    def save_evaluation(self, candidate_id, evaluation, candidates_dir="../Candidates"):
        """Save the evaluation results to the appropriate files."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        candidate_dir = os.path.join(base_dir, candidates_dir, candidate_id)
        
        # Create evaluation markdown
        competency_table = "\n".join([f"| {comp} | {score}/5 |" 
                                     for comp, score in evaluation["competencyScores"].items()])
        
        evaluation_md = f"""# Candidate Evaluation: {candidate_id}

## Summary
Candidate evaluation completed on {evaluation['timestamp'].split('T')[0]}. 
Based on the available materials, this candidate is classified as a **{evaluation['fitResult']}**.

## Competency Scores

| Competency | Score |
|------------|-------|
{competency_table}

## Final Fit Conclusion
**{evaluation['fitResult']}**

## Notes
{evaluation['notes']}
"""

        # Create AI notes markdown
        ai_notes_md = f"""# AI-Generated Notes: {candidate_id}

## Evaluation Summary
This candidate was evaluated using the competency matrix and scoring rules for the Senior Marketing Analyst position.

## Competency Details
{competency_table}

## Overall Assessment
The candidate is assessed as a **{evaluation['fitResult']}** for the role.

## Notes and Concerns
{evaluation['notes']}

*This evaluation was automatically generated by the [COMPANY_NAME] Recruiter Assistant.*
"""

        # Create Final Score markdown (as per updated prompt)
        final_score_md = f"""# Final Evaluation: {candidate_id}

## Summary
Candidate evaluation completed on {evaluation['timestamp'].split('T')[0]}. 
Based on the available materials, this candidate is classified as a **{evaluation['fitResult']}**.

## Competency Scores

| Competency | Score |
|------------|-------|
{competency_table}

## Final Fit Conclusion
**{evaluation['fitResult']}**

## Key Concerns
{evaluation['notes']}

*This evaluation was automatically generated by the [COMPANY_NAME] Recruiter Assistant on {evaluation['timestamp']}*
"""

        # Save the files
        try:
            output_files = self.config["candidateEvaluationSettings"]["outputFiles"]
            
            with open(os.path.join(candidate_dir, output_files["evaluation"]), 'w') as f:
                f.write(evaluation_md)
                
            with open(os.path.join(candidate_dir, output_files["aiNotes"]), 'w') as f:
                f.write(ai_notes_md)
            
            # Save Final-Score.md as per the updated prompt requirement
            with open(os.path.join(candidate_dir, "Final-Score.md"), 'w') as f:
                f.write(final_score_md)
                
            print(f"Evaluation saved for candidate {candidate_id}")
            
        except Exception as e:
            print(f"Error saving evaluation for candidate {candidate_id}: {e}")
    
    def create_candidate_folder(self, candidate_name, candidates_dir="../Candidates"):
        """Create a folder for a new candidate with template files."""
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            candidate_folder_name = f"Candidate-{candidate_name}"
            candidate_folder_path = os.path.join(base_dir, candidates_dir, candidate_folder_name)
            
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
            screening_path = os.path.join(candidate_folder_path, "Screening-Evaluation.md")
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
            ai_notes_path = os.path.join(candidate_folder_path, "AI-Notes.md")
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
                f.write("""# Comprehensive Evaluation - [Candidate Name]

> **NOTE: This is the FINAL evaluation incorporating all candidate materials, including CV, screening interview, technical interview, and any additional assessments. This evaluation is used for the final hiring decision.**

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
[Overall assessment of candidate fit for the role, incorporating all materials and interview results]

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
                f.write("""# Final Candidate Score - [Candidate Name]

> **NOTE: This document represents the FINAL hiring decision based on complete candidate assessment.**

## Technical Competency: [Score 1-10]
[Justification for score]

## Experience Relevance: [Score 1-10]
[Justification for score]

## Cultural Fit: [Score 1-10]
[Justification for score]

## Communication Skills: [Score 1-10]
[Justification for score]

## Overall Score: [Average of above scores]

## Final Hiring Decision
- [ ] Extend Offer
- [ ] Keep in Talent Pool
- [ ] Reject

## Decision Maker
[Name and title of decision maker]

## Decision Date
[Date of final decision]
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
    
    def run(self, specific_candidate=None):
        """Run the agent to evaluate candidates."""
        print(f"Starting {self.config['name']}")
        
        # Load context files
        self.load_context()
        
        # Discover candidates
        self.discover_candidates()
        
        if not self.candidates:
            print("No candidates found to evaluate.")
            return
            
        # Process specific candidate or all candidates
        candidates_to_process = [specific_candidate] if specific_candidate else self.candidates
        
        for candidate_id in candidates_to_process:
            if candidate_id not in self.candidates and specific_candidate:
                print(f"Candidate {candidate_id} not found.")
                continue
                
            print(f"\nEvaluating candidate: {candidate_id}")
            
            # Load candidate data
            candidate_data = self.load_candidate_data(candidate_id)
            
            # Evaluate candidate
            evaluation = self.evaluate_candidate(candidate_data)
            
            # Save evaluation
            if evaluation:
                self.save_evaluation(candidate_id, evaluation)
                
                print(f"Evaluation complete for {candidate_id}")
                print(f"Result: {evaluation['fitResult']}")
            else:
                print(f"Failed to evaluate {candidate_id}")

def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(description='Candidate Evaluation Agent')
    parser.add_argument('--candidate', help='Specific candidate to evaluate')
    parser.add_argument('--config', default='agent-config.json', help='Configuration file path')
    parser.add_argument('--create', help='Create a new candidate folder with the given name')
    
    args = parser.parse_args()
    
    agent = CandidateEvaluationAgent(config_path=args.config)
    
    if args.create:
        agent.create_candidate_folder(args.create)
    else:
        agent.run(specific_candidate=args.candidate)

if __name__ == "__main__":
    main() 