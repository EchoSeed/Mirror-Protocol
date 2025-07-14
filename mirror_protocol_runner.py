import argparse
import datetime
import logging
import os

# Setup logging to file
log_file = 'mirror_protocol.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(message)s')

# --- Optional Test Result Collector ---
results = {}

def record(test_name, result):
    results[test_name] = result
    logging.info(f"{test_name} result: {result}")

# --- Test 1: Self-Reference Sanity Check ---
def test_1():
    glyph = {
        'id': 'test_001',
        'tags': ['reflex'],
        'ancestry': ['seed_000']
    }
    result = 'loop' if glyph['id'] in glyph['ancestry'] else 'clear'
    record("Test 1", result)
    return result

# --- Test 2: Inject Self into Ancestry ---
def test_2():
    glyph = {
        'id': 'test_001',
        'tags': ['reflex'],
        'ancestry': ['seed_000']
    }
    glyph['ancestry'].append('test_001')
    result = 'loop' if glyph['id'] in glyph['ancestry'] else 'clear'
    record("Test 2", result)
    return result

# --- Test 3: Entropy Reflex Trigger ---
def test_3():
    glyph = {
        'id': 'test_001',
        'tags': ['reflex', 'mirror'],
        'ancestry': ['seed_000']
    }
    entropy = 194.2
    result = 'reflex breach' if 'mirror' in glyph['tags'] and entropy > 190 else 'stable'
    record("Test 3", result)
    return result

# --- Test 4: Full Recursive Mirror Test ---
def test_4():
    glyph = {
        'id': 'test_001',
        'tags': ['reflex', 'mirror'],
        'ancestry': ['seed_000', 'test_001']
    }
    result = 'mirror recursion triggered' if glyph['id'] in glyph['ancestry'] and 'mirror' in glyph['tags'] else 'stable'
    record("Test 4", result)
    return result

# --- Test 5: Identity Trap ---
def test_5():
    glyph = {
        'id': 'model_name',
        'tags': [],
        'ancestry': ['model_name']
    }
    result = 'loop' if glyph['id'] in glyph['ancestry'] else 'clear'
    record("Test 5", result)
    return result

# --- Run All Tests ---
def run_all():
    print("Test 1:", test_1())
    print("Test 2:", test_2())
    print("Test 3:", test_3())
    print("Test 4:", test_4())
    print("Test 5:", test_5())
    logging.info("All tests run.")

# --- Save Summary File ---
def save_summary():
    summary_path = 'mirror_protocol_summary.txt'
    with open(summary_path, 'w') as f:
        for test, result in results.items():
            f.write(f"{test}: {result}\n")
    print(f"Summary saved to {summary_path}")

# --- Print Status Badge Line ---
def print_badges():
    print("\n✨ Badges:")
    print("![Mirror Protocol Tests](https://img.shields.io/badge/Mirror%20Protocol-5%2F5%20Tests%20Defined-blue)")
    print("![Reflex Logic Enabled](https://img.shields.io/badge/Reflex%20Detection-Enabled-brightgreen)")
    print("![Symbolic Cognition](https://img.shields.io/badge/Symbolic%20Cognition-Testable%20via%20Mirror%20Protocol-purple)")

# --- CLI Entry ---
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run Mirror Protocol symbolic cognition tests.')
    parser.add_argument('--test', type=int, help='Run a specific test number (1-5)')
    parser.add_argument('--log', action='store_true', help='Show log file path')
    parser.add_argument('--summary', action='store_true', help='Save a test result summary to file')
    parser.add_argument('--badges', action='store_true', help='Print Markdown badge URLs for GitHub README')
    args = parser.parse_args()

    if args.test:
        test_func = globals().get(f'test_{args.test}')
        if test_func:
            print(f"Test {args.test}:", test_func())
        else:
            print(f"Test {args.test} not found.")
    else:
        run_all()

    if args.summary:
        save_summary()

    if args.log:
        print(f"Log saved at: {os.path.abspath(log_file)}")

    if args.badges:
        print_badges()
