#!/usr/bin/env groovy


def quickSort(list) {
  if (list.size() < 2) return list
  def pivot  = list[list.size().intdiv(2)]
  def left   = list.findAll { item -> item <  pivot }
  def middle = list.findAll { item -> item == pivot }
  def right  = list.findAll { item -> item >  pivot }
  return quickSort(left) + middle + quickSort(right)
}

assert quickSort([]) == []
assert quickSort([1]) == [1]
assert quickSort([1,2]) == [1,2]
assert quickSort([10,5,1,7]) == [1, 5, 7, 10]

assert quickSort([2,1]) == [1,2]
assert quickSort([3,1,2]) == [1,2,3]
assert quickSort([3,1,2,2]) == [1,2,2,3]
assert quickSort([1.0f,'a',10,null]) == [null,1.0f,10,'a']
assert quickSort('bca') == 'abc'.toList()









