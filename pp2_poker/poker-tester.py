import pp2_poker

def read_test_data(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

test_files = ['test_data1.txt', 'test_data2.txt', 'test_data3.txt', 'test_data4.txt']

for test_file in test_files:
    test_cases = read_test_data(test_file)
    
    print(f"Results for {test_file}:")
    for test_case in test_cases:
        result = pp2_poker.poker(test_case.strip())
        print(f"Test case: {test_case.strip()} -> Result: {result}")
    print()

