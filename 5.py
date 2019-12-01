import math
def ItemSimilarity_cos(train):
    C = dict()
    N = dict()
    for u,items in train.items():
        for i in items.keys():
            if i not in N.keys():
                N[i] = 0
            N[i] += items[i]*items[i]
            for j in items.keys():
                if i == j:
                    continue
                if i not in C.keys():
                    C[i] = dict()
                if j not in C[i].keys():
                    C[i][j] = 0
                C[i][j] += items[i]*items[j]
    W = dict()
    for i, related_items in C.items():
        if i not in W.keys():
            W[i] = dict()
        for j,cij in related_items.items():
            W[i][j] = cij /( math.sqrt(N[i])*math.sqrt(N[j]))
    return W
if __name__ == '__main__':
    Train_Data = {
        'A':{'苹果':2,'香蕉':2,'西瓜':2},
        'B':{'苹果':2,'西瓜':2},
        'C':{'苹果':2,'香蕉':2,'菠萝':2},
        'D':{'香蕉':2,'葡萄':2},
        'E':{'葡萄':2,'菠萝':2},
        'F':{'香蕉':2,'西瓜':2},
    }
    W = ItemSimilarity_cos(Train_Data)
    print(W)