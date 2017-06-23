# Algorithms

## Searching

### Needle in Haystack

#### Parallel Collision

```
Initialize an empty table of M entries.
for i = 1 to M do
    Pick at random a point xi ∈ [N].
    Set tmp ← xi, len ← 0.
    while f(tmp) is not a distinguished point do
        tmp ← f(tmp).
        Increment len.
        end while
        tmp ← f(tmp).
        Increment len.
        Store in the table the pair (tmp, xi, len).
end for

for All collisions ((pi, xi, leni),(pj , xj , lenj )) s.t. pi = pj do
    Set tmp1 ← xi, tmp2 ← xj .
    if len1 > len2 then
        for i = 1 to len1 − len2 do
            tmp1 ← f(tmp1)
        end for
    end if
if len2 > len1 then
    for i = 1 to len2 − len1 do
        tmp2 ← f(tmp2)
    end for
end if

while f(tmp1) 6= f(tmp2) do
    tmp1 ← f(tmp1), tmp2 ← f(tmp2)
end while

print tmp1, tmp2.
end for
```



