# test_detect_recursion.py

def add_to_ancestry(g):
    g['ancestry'].append(g['id'])
    return g

def detect_recursion(g):
    if g['id'] in g['ancestry']:
        return 'Recursion confirmed: ID found in ancestry'
    return 'No recursion detected'

def test_recursion_detection():
    glyph = {
        'id': 'c047',
        'tags': ['reflex', 'recursive', 'test'],
        'ancestry': ['c001', 'c023']
    }
    glyph = add_to_ancestry(glyph)
    result = detect_recursion(glyph)
    assert result == 'Recursion confirmed: ID found in ancestry'

if __name__ == '__main__':
    test_recursion_detection()
    print("✅ Recursion detection test passed.")
