import json

# open json file
with open('test_case_data.json') as file:
    test_case_data = json.load(file)


# grab data

print("Listing all test cases....")
print("*" * 40)
# get all test case names
for tests in test_case_data:
    print(tests)


print("\nGetting variable test_case_data from a test case....")
print("*" * 40)
# get variable from a test case using for loop
for test_var in test_case_data['test_create_mvd_using_udf']:
    print(test_var['endpoint_name'])

# get variable from a test case
print(test_case_data['test_create_mvd_using_udf'][0]['type_of_record'])


print("\nListing all test cases and variables....")
print("*" * 40)
# get all test case names
for test in test_case_data:
    test_name = test
    print(f"Test Case Name: {test_name}")
    for variables in test_case_data[test]:
        for key, value in variables.items():
            print(f"\tVarName: {key} | VarValue: {value}")
