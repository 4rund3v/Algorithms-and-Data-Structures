"""
merge sort(a)
    if length(a) ≤ 1 then
        return a
    m ← length(a)div 2
    a0 ← merge sort(a[m])
    a1 ← merge sort(a[m])
    merge(a0,a1,a)
    return a
"""
