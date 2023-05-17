
def n = 100

def total = 0
1.upto(n) {total += it-1}

assert total == n*(n-1)/2

// java version

int total2 = 0;

for (int i=0; i<n; i++)
    total2 += i;

assert total2 == n*(n-1)/2

// Groovy, but using Java indexing

def total3 = 0
0.upto(n-1) {total3 += it}
assert total3 == n*(n-1)/2

