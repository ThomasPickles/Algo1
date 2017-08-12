


myArray = [3, 1, 16, 13, 9, 11, 14, 5, 7, 10, 12, 8, 2, 15, 4, 6]#

print('***MergeSort***')
print('Divide--->')
print('<---Merge')
print(myArray)

def mergeArray(left, right):
  print('Input is ')
  print(left)
  print(right)
  leftCounter = 0
  rightCounter = 0
  merge=[]
  print('Merge length is ' + str(len(left+right)))
  for k in range(len(left+right)):
   # TODO: optimise this bit (avoid repetition and avoid overflow)
    if (rightCounter == len(right)):
      merge.append(left[leftCounter])
      leftCounter+=1
    elif (leftCounter == len(left)):      
      merge.append(right[rightCounter])
      rightCounter+=1
    elif(left[leftCounter] < right[rightCounter]):
      merge.append(left[leftCounter])
      leftCounter+=1
    else:      
      merge.append(right[rightCounter])
      rightCounter+=1
  print('Output is:')
  print(merge)
  return merge

#  log += getTab(--level) + "[" + left + "]  [" + right + "]" + " >> [" + merge + "]\n";

def sortArray(A, n):
  if (n == 1):
    return A;
  else:
    newLength = int(n / 2)

    B=A[:newLength]
    C = A[newLength:]
    print(B)
    print(C)
  
    X = sortArray(B, newLength)
    Y = sortArray(C, newLength)
    Z = mergeArray(X, Y);
    return Z;

# def getTab(n):
#   str = "";
#   for i in range(n):
#     str += "  "
#   return str

# level = 0

sortArray(myArray, 16)



#document.getElementById('text').innerHTML = execute();
