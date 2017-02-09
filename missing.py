def find_empty(list1):
  seen = set()
  list1= []
  for x in list1:
    if x in seen:
      return 1
      seen.add(x)
      list1.append(x)

def number_missed(list):
    for item in list[1:]:
      if item != list[0]:
            return 0

def find_missing(self, list1):
        for x in range(0,len(list1) -1):
                if list1[x+1] - list1[x] != 1:
                        print (list1[x] + 1)
                else:
                  return 0