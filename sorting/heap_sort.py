"""
heap sort(a)
    h ← BinaryHeap()
    h.a ← a
    h.n ← length(a)
    m ← h.ndiv 2
    for i in m − 1,m − 2,m − 3,...,0 do
        h.trickle down(i)
    while h.n > 1 do
        h.n ← h.n − 1
        h.a[h.n],h.a[0] ← h.a[0],h.a[h.n]
        h.trickle down(0)
"""
