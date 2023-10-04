
def main():
    info= [4,18,12,9,2,17,24]
    length= len(info)
    total= sum(info)
    mean= total/length
    print ("The mean is", mean)

    info.sort()

    if length % 2==0:
        possible= info[length//2]
        possible2= info[length//2-1]
        median= (possible + possible2)/2
    else:
        median= info[length//2]
    print ("Median is", median)

if __name__ =="__main__":
    main()
