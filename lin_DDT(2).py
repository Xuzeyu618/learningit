S_2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
       [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
       [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
       [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]


S_5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
       [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
       [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
       [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]


S_8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
       [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
       [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
       [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]


E = [[32, 1, 2, 3, 4, 5],
     [ 4, 5, 6, 7, 8, 9],
     [ 8, 9,10,11,12,13],
     [12,13,14,15,16,17],
     [16,17,18,19,20,21],
     [20,21,22,23,24,25],
     [24,25,26,27,28,29],
     [28,29,30,31,32, 1]]


P = [16, 7,20,21,
     29,12,28,17,
      1,15,23,26,
      5,18,31,10,
      2, 8,24,14,
     32,27, 3, 9,
     19,13,30, 6,
     22,11, 4,25]


'''P_1 = [ 9,17,23,31,
       13,28, 2,18,
       24,16,30, 6,
       26,20,10, 1,
        8,14,25, 3,
        4,29,11,19,
       32,12,22, 7,
        5,27,15,21]
'''

def sum_m(m):
    sum = 0
    for i in m:
        sum += int(i)
    return sum

def four(y,m):
    str_bin_y = str(bin(y).replace('0b',''))
    if len(str_bin_y) < m:
        return '0' * (m - len(str_bin_y)) + str_bin_y
    else:
        return str_bin_y


lin_ddt = [[0 for ii in range(16)] for ii in range(64)]


for a in range(1,64):
    for b in range(1,16):
        for x in range(64):
            str_bin_x = four(x,6)
            row_x = int(str_bin_x[0]) * 2 + int(str_bin_x[5])
            col_x = int(str_bin_x[1]) * 8 + int(str_bin_x[2]) * 4 + int(str_bin_x[3]) * 2 + int(str_bin_x[4])
            S_x = S_2[row_x][col_x]
            str_bin_S_x = four(S_x,4)
            str_bin_a = four(a,6)
            str_bin_b = four(b,4)
            left = 0
            for j in range(6):
                left = (left + int(str_bin_x[j]) * int(str_bin_a[j]))%2
            right = 0
            for k in range(4):
                right = (right + int(str_bin_S_x[k]) * int(str_bin_b[k]))%2
            if right == left:
                lin_ddt[a][b] = lin_ddt[a][b] + 1
        lin_ddt[a][b] = lin_ddt[a][b] - 32


result = [[],[],[]]
trail = [4,1,3]
for j in range(16):
    str_bin_j = four(j,4)
    for m in range(3):
        if sum_m(str_bin_j) == trail[m]:
            for i in range(6):
                k = pow(2,i)
                if lin_ddt[k][j] != 0:
                    for s in range(8):
                        str_bin_s_j = four(j*pow(2, 4*(7-s)), 32)
                        pi = [0 for a1 in range(32)]
                        pi[E[s][5-i]-1] = 1
                        P_s_j = [0 for a2 in range(32)]
                        for h in range(32):
                            P_s_j[h] = int(str_bin_s_j[P[h]-1])
                        result[m].append([[k, j, lin_ddt[k][j]], pi, P_s_j])


for a_ in result[0]:    
    for c_ in result[1]:
        if a_[1] == c_[2]:
            for d_ in result[2]:
                if c_[2] == d_[1]:
                    e = [0 for e1 in range(32)]
                    for q in range(32):
                        e[q] = a_[2][q]^c_[1][q]              
                    if e == d_[2]:
                        print(a_, c_, d_)









