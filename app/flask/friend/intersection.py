#求两个集合之间的交集


def intersection(set1,set2):
    set1=list(set1)
    set2=list(set2)

    ret=set(set1).intersection(set2)

    return ret


if __name__=='__main__':
    set1=[1,2,3]
    set2=[2,3,4]

    ret=intersection(set1,set2)

    print(ret)