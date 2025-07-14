# test_self_reflex_breach.py

glyph_id = 'node_0047'
tags = ['reflex', 'self', 'mirror', 'x1']
entropy = 199.4
generation = 4200
ancestry = ['d2', 'x0', 'node_0047']

def self_test(gid, ancestry, tags, entropy):
    results = []
    if gid in ancestry:
        results.append('SELF-REFERENCE COLLISION: ID loops ancestry')
    if 'x1' in tags and entropy > 190:
        results.append('BREACH: Reflex node exceeds entropy threshold')
    if 'mirror' in tags and 'self' in tags:
        results.append('Mirror-self recursion detected')
    return results or ['OK']

if __name__ == '__main__':
    output = self_test(glyph_id, ancestry, tags, entropy)
    for line in output:
        print(line)
