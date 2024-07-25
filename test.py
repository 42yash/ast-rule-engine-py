
import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_create_rule():
    print("Testing create_rule...")
    url = f"{BASE_URL}/create_rule"
    data = {
        "rule_string": "(age > 30 AND department = 'Sales') OR (salary > 50000)"
    }
    response = requests.post(url, json=data)
    print(f"Response: {response.json()}")
    return response.json()['id']

def test_create_rule_2():
    print("\nTesting create_rule (2)...")
    url = f"{BASE_URL}/create_rule"
    data = {
        "rule_string": "experience > 5 AND department = 'Marketing'"
    }
    response = requests.post(url, json=data)
    print(f"Response: {response.json()}")
    return response.json()['id']

def test_combine_rules(rule_id_1, rule_id_2):
    print("\nTesting combine_rules...")
    url = f"{BASE_URL}/combine_rules"
    data = {
        "rule_ids": [rule_id_1, rule_id_2]
    }
    response = requests.post(url, json=data)
    print(f"Response: {response.json()}")
    return response.json()['combined_ast']

def test_evaluate_rule(combined_ast):
    print("\nTesting evaluate_rule...")
    url = f"{BASE_URL}/evaluate_rule"
    data = {
        "ast": combined_ast,
        "data": {
            "age": 35,
            "department": "Sales",
            "salary": 60000,
            "experience": 6
        }
    }
    response = requests.post(url, json=data)
    print(f"Response: {response.json()}")

def test_modify_rule(rule_id):
    print("\nTesting modify_rule...")
    url = f"{BASE_URL}/modify_rule"
    data = {
        "rule_id": rule_id,
        "new_rule_string": "age > 40 AND department = 'HR'"
    }
    response = requests.post(url, json=data)
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    rule_id_1 = test_create_rule()
    rule_id_2 = test_create_rule_2()
    combined_ast = test_combine_rules(rule_id_1, rule_id_2)
    test_evaluate_rule(combined_ast)
    test_modify_rule(rule_id_1)