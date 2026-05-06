#!/bin/bash

# Color codes
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}════════════════════════════════════════${NC}"
echo -e "${BLUE}  Skincare Recommendation System Setup  ${NC}"
echo -e "${BLUE}════════════════════════════════════════${NC}\n"

# Check Python version
echo -e "${YELLOW}[1/4] Checking Python version...${NC}"
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo -e "      Python $python_version found ${GREEN}✓${NC}\n"

# Create virtual environment
echo -e "${YELLOW}[2/4] Creating virtual environment...${NC}"
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo -e "      Virtual environment created ${GREEN}✓${NC}\n"
else
    echo -e "      Virtual environment already exists ${GREEN}✓${NC}\n"
fi

# Activate virtual environment
echo -e "${YELLOW}[3/4] Activating virtual environment...${NC}"
source venv/bin/activate
echo -e "      Environment activated ${GREEN}✓${NC}\n"

# Install dependencies
echo -e "${YELLOW}[4/4] Installing dependencies...${NC}"
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1
echo -e "      Dependencies installed ${GREEN}✓${NC}\n"

echo -e "${GREEN}════════════════════════════════════════${NC}"
echo -e "${GREEN}  Ready to run! Use this command:${NC}"
echo -e "${GREEN}════════════════════════════════════════${NC}"
echo -e "\n${BLUE}streamlit run app.py${NC}\n"
