from collections import defaultdict
import math
def defItemIndex(DictUser):
    DictItem=defaultdict(defaultdict)
    for key in DictUser:
        for i in DictUser[key]:
            DictItem[i][key]=[key,DictUser[key][i]]
    return DictItem


def defUserSimilarity(DictItem):
    N = dict()
    C=defaultdict(defaultdict)
    W=defaultdict(defaultdict)
    for key in DictItem:
        for x in DictItem[key]:
            i = DictItem[key][x]
            if i[0] not in N.keys():
                N[i[0]]=0
            N[i[0]]+=1
            for j in DictItem[key]:
                if i[0] == j[0]:
                    continue
                if j[0] not in C[i[0]].keys():
                    C[i[0]][j[0]] = 0
                C[i[0]][j[0]] += 1

    for i, related_user in C.items():
        for j, cij in related_user.items():
            W[i][j] = cij / math.sqrt(N[i] * N[j])
    return W
if __name__ == '__main__':
    Train_Data = {
        'A':{'苹果':1,'香蕉':1,'西瓜':1},
        'B':{'苹果':1,'西瓜':1},
        'C':{'苹果':1,'香蕉':1,'菠萝':1},
        'D':{'香蕉':1,'葡萄':1},
        'E':{'葡萄':1,'菠萝':1},
        'F':{'香蕉':1,'西瓜':1},
    }
    W = defItemIndex(Train_Data)
    print(defUserSimilarity(W))
