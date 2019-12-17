def mergeSort(nlist) :
    print("Splitting ",nlist)
    if len(nlist) > 1 :
        mid = len(nlist)//2
        lefthaft = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthaft)
        mergeSort(righthalf)
        i=j=k=0
        while i < len(lefthaft) and j < len(righthalf) :
            if lefthaft[i] < righthalf[j] :
                nlist[k]=lefthaft[i]
                i=i+1
            else :
                nlist[k] = righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthaft) :
            nlist[k] = lefthaft[i]
            i=i+1
            k=k+1
        while j < len(righthalf) :
            nlist[k] = righthalf[j]
            j=j+1
            k=k+1
    print("Merging",nlist)

nlist = [14,46,43,27,57,41,45,21,70]
mergeSort(nlist)
print(nlist)