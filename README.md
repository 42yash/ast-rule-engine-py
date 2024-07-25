# Rule Engine with AST

This project implements a simple 3-tier rule engine application using Flask, SQLAlchemy, and SQLite. It allows for the creation, combination, and evaluation of rules based on Abstract Syntax Trees (ASTs).

## Setup

1. Install the required dependencies:
   ```
   pip install flask sqlalchemy
   ```

2. Run the Flask application:
   ```
   python main.py
   ```

## API Endpoints

### 1. Create Rule
- **URL:** `/create_rule`
- **Method:** POST
- **Data Params:** 
  ```json
  {
    "rule_string": "(age > 30 AND department = 'Sales') OR (salary > 50000)"
  }
  ```
- **Success Response:**
  ```json
  {
    "id": 1,
    "ast": "..."
  }
  ```

### 2. Combine Rules
- **URL:** `/combine_rules`
- **Method:** POST
- **Data Params:** 
  ```json
  {
    "rule_ids": [1, 2]
  }
  ```
- **Success Response:**
  ```json
  {
    "combined_ast": "..."
  }
  ```

### 3. Evaluate Rule
- **URL:** `/evaluate_rule`
- **Method:** POST
- **Data Params:** 
  ```json
  {
    "ast": "...",
    "data": {
      "age": 35,
      "department": "Sales",
      "salary": 60000
    }
  }
  ```
- **Success Response:**
  ```json
  {
    "result": true
  }
  ```

### 4. Modify Rule
- **URL:** `/modify_rule`
- **Method:** POST
- **Data Params:** 
  ```json
  {
    "rule_id": 1,
    "new_rule_string": "age > 40 AND department = 'HR'"
  }
  ```
- **Success Response:**
  ```json
  {
    "message": "Rule updated successfully"
  }
  ```

## Sample Curl Workflow

Here's a step-by-step workflow using curl commands to test the rule engine:

1. Create the first rule:
   ```bash
   curl -X POST http://127.0.0.1:5000/create_rule -H "Content-Type: application/json" -d '{"rule_string": "(age > 30 AND department = '\''Sales'\'') OR (salary > 50000)"}'
   ```

2. Create the second rule:
   ```bash
   curl -X POST http://127.0.0.1:5000/create_rule -H "Content-Type: application/json" -d '{"rule_string": "experience > 5 AND department = '\''Marketing'\''"}'
   ```

3. Combine the rules (replace `1` and `2` with the actual rule IDs from steps 1 and 2):
   ```bash
   curl -X POST http://127.0.0.1:5000/combine_rules -H "Content-Type: application/json" -d '{"rule_ids": [1, 2]}'
   ```

4. Evaluate the combined rule (replace `<combined_ast>` with the actual combined AST from step 3):
   ```bash
   curl -X POST http://127.0.0.1:5000/evaluate_rule -H "Content-Type: application/json" -d '{
     "ast": "<combined_ast>",
     "data": {
       "age": 35,
       "department": "Sales",
       "salary": 60000,
       "experience": 6
     }
   }'
   ```

5. Modify a rule (replace `1` with the actual rule ID you want to modify):
   ```bash
   curl -X POST http://127.0.0.1:5000/modify_rule -H "Content-Type: application/json" -d '{
     "rule_id": 1,
     "new_rule_string": "age > 40 AND department = '\''HR'\''"
   }'
   ```

## Testing

You can use the provided `test.py` script to test the rule engine functionality. Run it using:

```
python test.py
```

This script will test creating rules, combining rules, evaluating rules, and modifying rules.
