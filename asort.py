
def split(data):
    if len(data)<2:
        return data
    else:
        left=data[:len(data)//2]
        right=data[len(data)//2:]
        return  merge( split(left),split(right)  )

def findMin(data,newMark):
    if newMark==len(data)-1:
        return data
    else:
        minIndex=newMark
        for mark in range(minIndex+1,len(data)):
            if data[mark]<=data[minIndex]:
                minIndex=mark
        temp=data[minIndex]
        data[minIndex]=data[newMark]
        data[newMark]=temp
        return findMin(data,newMark+1)

def merge(left,right):
    brr=[]
    indexLeft=0
    indexRight=0
    while indexLeft<len(left) and indexRight<len(right):
        if left[indexLeft]<=right[indexRight]:
            brr.append(left[indexLeft])
            indexLeft+=1
        else:
            brr.append(right[indexRight])
            indexRight+=1
    if indexRight<len(right):
        brr.extend(right[indexRight:])
    elif indexLeft<len(left):
        brr.extend(left[indexLeft:])
        """
        extend在添加多个元素进入链表时，可以不加括号的添加，而append带括号添加
        添加一个元素时只能用appends
        """
    return brr

def main():
    """
    Main function.
    :return: None
    """
    DATA1 = ([], [0], [0, 1], [1, 0], [5, 4, 3], [1, 9, 4, 2, 0, 3, 7])
    print('Testing merge sort...')
    for data in DATA1:
        print('data:', data, ', sorted:', split(data))
    """
    注意findMin方法，不能排序长度为空的链表
    """
    for data in DATA1:
        print('data:', data, ', sorted:', findMin(data,0))

if __name__ == '__main__':
    main()