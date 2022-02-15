# list

## O(1)

| Operation | Usage       |
| --------- | ----------- |
| Length    | len(l)      |
| Append    | l.append(0) |
| Pop last  | l.pop()     |
| Get       | l[0]        |
| Set       | l[0] = 0    |

## O(N)
| Operation    | Usage          |
| ------------ | -------------- |
| Copy         | l.copy()       |
| Pop          | l.pop(0)       |
| Insert       | l.insert(0, 5) |
| Delete       | del l[0]       |
| Iteration    | for i in l:    |
| Delete slice | del l[1:3]     |
| Containment  | 3 in l         |
| Extreme      | min(l), max(l) |
| Count        | l.count(0)     |
| Index        | l.index(0)     |
| Reverse      | l.reverse()    |
| Remove       | l.remove()     |

## O(N log N)
| Operation | Usage    |
| --------- | -------- |
| Sort      | l.sort() |

## etc
| Operation | Usage          | Time complexity |
| --------- | -------------- | --------------- |
| Set slice | ll[:k] = l[:k] | O(N + k)        |
| Slice     | l[x:y]         | O(y - x)        |
| Extend    | l.extend(lst2) | O(len(lst2))    |
| Multiply  | l * k          | O(Nk)           |
