#!/bin/bash
# Script to run the [COMPANY_NAME] Screening Agent

# Set the script to exit on error
set -e

# Define colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Print banner
echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}  [COMPANY_NAME] Screening Agent${NC}"
echo -e "${BLUE}================================================${NC}"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is not installed.${NC}"
    echo "Please install Python 3 to use this agent."
    exit 1
fi

# Check for dependencies
echo -e "${YELLOW}Checking dependencies...${NC}"
python3 -c "import markdown" 2>/dev/null || {
    echo -e "${YELLOW}Installing required packages...${NC}"
    pip install markdown
}

# Get directory of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Change to the agent directory
cd "$DIR"

# Parse command line arguments
CANDIDATE=""
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -c|--candidate) CANDIDATE="$2"; shift ;;
        *) echo "Unknown parameter: $1"; exit 1 ;;
    esac
    shift
done

# Run the agent
echo -e "${YELLOW}Running agent...${NC}"
if [ -z "$CANDIDATE" ]; then
    # Evaluate all candidates
    python3 agent.py
else
    # Evaluate specific candidate
    python3 agent.py --candidate "$CANDIDATE"
fi

echo -e "${GREEN}Screening completed!${NC}" 