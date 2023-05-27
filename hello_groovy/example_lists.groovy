#!/usr/bin/env groovy

myList = ['a', 'b', 'c']
assert myList.isCase('a')
assert 'b' in myList
def candidate = 'c'
switch(candidate){
    case myList : assert true; break
    default     : assert false
}

assert ['x','a','z'].grep(myList) == ['a']

myList = []
if (myList) assert false

def expr = ''
for (i in [1,'*',5]){
    expr += i
}
assert expr == '1*5'

assert [1,[2,3]].flatten() == [1,2,3]

assert [1,3] == [3,1].sort()

assert [1,2,3].intersect([4,3,1])== [1,3]
assert [1,2,3].disjoint([4,5,6])
list = [1,2,3]
popped = list.pop()
assert popped == 1
assert list == [2,3]
assert [1,2].reverse() == [2,1]
assert [3,1,2].sort() == [1,2,3]
def list = [ [1,0], [0,1,2] ]
list = list.sort { a,b -> a[0] <=> b[0] }

assert list == [ [0,1,2], [1,0] ]
list = list.sort { item -> item.size() }
assert list == [ [1,0], [0,1,2] ]

list = ['a','b','c']
list.remove(2)
assert list == ['a','b']

list.remove('b')
assert list == ['a']

list = ['a','b','b','c']
list.removeAll(['b','c'])

assert list == ['a']

def doubled = [1,2,3].collect{ item ->
  item*2
}
assert doubled == [2,4,6]

def odd = [1,2,3].findAll{ item ->
  item % 2 == 1
}
assert odd == [1,3]

list = [1, 2, 3]
assert list.first()  == 1
assert list.head()   == 1
assert list.tail()   == [2, 3]

assert list.last() ==3 
assert list.count(2) == 1 
assert list.max() ==3 
assert list.min() ==1
def even = list.find { item ->
    item % 2 == 0
}

assert even == 2
assert list.every { item -> item < 5 }
assert list.any   { item -> item < 2 }

def store = ''
list.each { item ->
    store += item
}
assert store == '123'

store = ''
list.reverseEach { item ->
    store += item
}
assert store == '321'

store = ''
list.eachWithIndex { item, index ->
    store += "$index:$item "
}
assert store == '0:1 1:2 2:3 '
assert list.join('-') == '1-2-3'

result = list.inject(0) { clinks, guests ->
    clinks + guests
}
assert result == 0 + 1 + 2 + 3
assert list.sum() == 6
factorial = list.inject(1) { fac, item ->
    fac * item
}
assert factorial == 1 * 1 * 2 * 3


