# Rule Engine with AST

## Overview
This project implements a 3-tier rule engine application that determines user eligibility based on attributes like age, department, income, and spend. The system uses Abstract Syntax Trees (AST) to represent conditional rules, allowing for dynamic creation, combination, and modification of these rules.

## Features
- Create rules using a string representation
- Combine multiple rules into a single AST
- Evaluate rules against provided data
- Store rules in a database
- API for rule management and evaluation

## Design Choices
1. **AST Data Structure**: We use a `Node` class to represent the AST. Each node has:
   - `type`: String indicating node type ("operator" or "operand")
   - `left`: Reference to left child node
   - `right`: Reference to right child node
   - `value`: Optional value for operand nodes

2. **Database**: We use MongoDB to store rules and application metadata. This choice allows for flexible schema design and easy scalability.

3. **API Design**: 
   - `create_rule(rule_string)`: Creates an AST from a rule string
   - `combine_rules(rules)`: Combines multiple rules into a single AST
   - `evaluate_rule(JSON data)`: Evaluates a rule against provided data

## Setup Instructions

### Prerequisites
- Python 3.8+
- MongoDB
- Docker (optional)

### Installation
1. Clone the repository: git clone https://github.com/saranyamanne/rule-engine.git
2. cd rule-engine
3. Set up a virtual environment: On Windows use venv\Scripts\activate
4. Install dependencies:pip install -r requirements.txt
5. Set up MongoDB:
- Install MongoDB or use a Docker container:
  ```
  docker run -d -p 27017:27017 --name mongodb mongo:latest
  ```
  5. Set environment variables:export MONGODB_URI=mongodb://localhost:27017/rule_engine
 
  
### Running the Application
1. Start the API server:python app.py

2. The API will be available at `http://localhost:5000`

## API Endpoints
- POST /api/rules - Create a new rule
- GET /api/rules - List all rules
- POST /api/evaluate - Evaluate data against a rule

## Testing
Run the test suite:python -m unittest discover tests


## Dependencies
- Flask: Web framework for the API
- pymongo: MongoDB driver for Python
- jsonschema: JSON Schema validator

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
