import json
test_case_data = '''
{
    "test_create_mvd_using_udf": [
        {
            "type_of_record": "DENIED",
            "endpoint_name": "auto",
            "new_var": "auto2"
        }
    ]
        ,
        "test_create_org": [
        {
            "org_name": "automation_org",
            "alc": "53434343"
        }
    ],
            "test_create_FI": [
        {
            "fi_name": "BOFA",
            "can": "33223"
        }
    ]
}
'''
data = json.loads(test_case_data)

print("Listing all test cases....")
print("*" * 40)
# get all test case names
for tests in data:
    print(tests)


print("\nGetting variable data from a test case....")
print("*" * 40)
# get variable from a test case
for test_var in data['test_create_mvd_using_udf']:
    print(test_var['endpoint_name'])

print("\nListing all test cases and variables....")
print("*" * 40)
# get all test case names
for test in data:
    test_name = test
    print(f"Test Case Name: {test_name}")
    for variables in data[test]:
        for key, value in variables.items():
            print(f"\tVarName: {key} | VarValue: {value}")

