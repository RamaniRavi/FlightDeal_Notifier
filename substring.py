from collections import OrderedDict


def merge_the_tools(string, k):
    # your code goes here
    # sub = [i for i in string[:k]]
    sub =[]
    j =0;
    l =0;
    for i in range(0,int(len(string)/k)):

        sub.append(string[j:j+k])
        j =j+k
        r = "".join(OrderedDict.fromkeys(sub[l]))
        print(r)
        l+=1
    for i in sub:
        print(i)




if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)