Class BinarySearch():
def __init__(self, a, b):
        super(BinarySearch, self).__init__(range(b, a*b + b,b))
        self.array = []
        self.length = a
        self.step = b
        for i in range(b,a,b):
            array.append(i)
        return array



def search(self, value):
    self.value = value
    bool_find, value_idx, count = binary_search(value, self)
    result = {}
    startpoint = 0
    n = len(array)
    min = array[0]
    max = array[n-1]

    result['count']= count
    result['index']= value_idx
    return result
    
def binarySearch(val, my_list):
  my_list.sort()
  sub_list = my_list
  n=0
  if val == sub_list[0] or val == sub_list[-1]:
    return True, my_list.index(val), n
  while sub_list:
    startpoint = 0
    stoppoint = len(sub_list) - 1
    midpoint = int(round((startpoint + stoppoint)/2))
    n +=1
  if out_of_range(val, sub_list):
    n +=2
    return False, -1, n
  else:
    if val == sub_list[midpoint]:
      return true, my_list.index(val), n
    elif val < sub_list[midpoint]:
      sub_list = sub_list[startpoint:]
      
def out_of_range(t, l):
  if  [0] > t or [-1] < t:
    return True
  else:
    return False
    
def main():
  return binarySearch


 