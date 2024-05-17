evenNum = {1,2,3,4,6,8,10}
oddNum = {1,3,5,7,9}

num = evenNum.union(oddNum)
print(num)

diff = evenNum.difference(oddNum)

print(diff)

inter = evenNum.intersection(oddNum)

print(inter)

symdiff = evenNum.symmetric_difference(oddNum)

print(symdiff)

joint = evenNum.isdisjoint(oddNum)

print(joint)

sub = oddNum.issubset(evenNum)

print(sub)

sup = evenNum.issuperset(oddNum)

print(sup)

evenNum = list(evenNum)
oddNum = tuple(oddNum)

print(evenNum, oddNum)

evenNum = set(evenNum)

print(evenNum)