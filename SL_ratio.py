def c(x,y,z) :
    c = []
    for k in range((len(x))): # c1
        c.append(((((x[z] - x[k])**2) + ((y[z] - y[k])**2)) ** (1/2)))
    return c
    
def point_sort(x : list) -> list : #เเยกมาเป็นที่ละตัว
    if len(x) == 1:
        return x #ได้มาตัวเดียว
    else :
        กลาง = len(x) // 2
        ซ้าย = point_sort(x[ : กลาง]) #เอาตั้งเเต่ตัวเเรกถึงตัวกลาง
        ขวา = point_sort(x[กลาง : ]) # เอาตั้งเเต่ตัวกลางถึงสุดท้าย

        return new(ซ้าย,ขวา) #เข้าฟังชั่นเทียบ

def new(left,right) : #เทียบซ้าย ขวา
    i = 0
    j = 0
    s = [] #ผลลัพท์


    while i < len(left) and j < len(right): #ลูป เทียบซ้าย ขวาทีละตัวจนฝั่งใดฝั่งหนึ่งเทียบหมด
        o = left[i]
        w = right[j]
        if o < w:
            s.append(left[i])
            i += 1
        else:
            s.append(right[j])
            j += 1
    while i < len(left): #ลูปที่ถ้าเทียบฝั่งขวาหมดก่อน
        s.append(left[i])
        i += 1
    while j < len(right): #ลูปที่ถ้าเทียบฝั่งซ้ายหมดก่อน
        s.append(right[j])
        j += 1

    return s

def linear_search_N(x,key) :
    for j in range(len(key)):
        for i in range(len(x)) :
            if x[i] == key:
                return key
    return "error"

def linear_search_SLP(x,key,q) :
    for j in range(len(key)):
        for i in range(len(x)) :
            if x[i] == key[j] :
                q += 1
    return q

def linear_search_SLN(x,key,q,w) :
    if w in x :
        x.remove(w)
    for j in range(len(key)):
        for i in range(len(x)) :
            if x[i] == key[j] :
                q += 1
    return q


def linear_search(x,key) :
    z = []
    for j in range(len(key)):
        for i in range(len(x)) :
            if x[i] == key[j] :
                if i < 45:
                    z.append("R%d" % (i+1))
                else:
                    z.append("B%d" % (i+1))
    return z

def linear_search_Def4(x,key) :
    def4 = []
    for j in range(len(key)):
        for i in range(len(x)) :
            if x[i] == key[j] :
                def4.append(x[i])
    return def4

def del_d(d,e,j):
    d.remove(d[0])
    if j in d:
        d.remove(j)
    for i in range(len(d) - e):
        del d[e]
    return d    

x = [3.000,5.200,10.600,18.700,27.500,32.000,35.100,40.800,48.700,55.800,62.300,70.000,75.000,77.000,5.000,8.000,12.700,21.900,29.600,37.500,44.400,52.900,60.400,66.700,73.700,10.000,15.600,23.900,32.600,42.800,50.400,54.800,63.400,69.900,13.500,17.500,26.600,36.400,46.700,53.700,60.600,21.500,29.100,41.600,51.600,32.300,38.000,42.300,47.700,45.600,41.200,36.400,34.300,38.200,41.590,15.000,40.000,60.000,59.000,42.000]
y = [40.000,38.400,34.100,30.000,26.500,25.500,25.100,24.700,26.000,27.500,30.000,35.000,38.600,40.600,36.500,33.400,31.000,24.600,21.400,20.000,21.400,21.900,25.000,28.900,35.300,30.000,27.100,21.300,17.200,15.170,16.400,18.600,23.000,28.000,24.300,21.100,15.900,11.500,11.100,13.800,16.400,14.200,8.700,6.000,9.300,28.400,26.500,27.000,29.900,32.400,29.600,29.800,33.300,32.300,33.980,30.000,10.000,20.000,22.000,21.000]

c1 = c(x,y,0)
c2 = c(x,y,1)
c3 = c(x,y,2)
c4 = c(x,y,3)
c5 = c(x,y,4)
c6 = c(x,y,5)
c7 = c(x,y,6)
c8 = c(x,y,7)
c9 = c(x,y,8)
c10 = c(x,y,9)
c11 = c(x,y,10)
c12 = c(x,y,11)
c13 = c(x,y,12)
c14 = c(x,y,13)
c15 = c(x,y,14)
c16 = c(x,y,15)
c17 = c(x,y,16)
c18 = c(x,y,17)
c19 = c(x,y,18)
c20 = c(x,y,19)
c21 = c(x,y,20)
c22 = c(x,y,21)
c23 = c(x,y,22)
c24 = c(x,y,23)
c25 = c(x,y,24)
c26 = c(x,y,25)
c27 = c(x,y,26)
c28 = c(x,y,27)
c29 = c(x,y,28)
c30 = c(x,y,29)
c31 = c(x,y,30)
c32 = c(x,y,31)
c33 = c(x,y,32)
c34 = c(x,y,33)
c35 = c(x,y,34)
c36 = c(x,y,35)
c37 = c(x,y,36)
c38 = c(x,y,37)
c39 = c(x,y,38)
c40 = c(x,y,39)
c41 = c(x,y,40)
c42 = c(x,y,41)
c43 = c(x,y,42)
c44 = c(x,y,43)
c45 = c(x,y,44)
c46 = c(x,y,45)
c47 = c(x,y,46)
c48 = c(x,y,47)
c49 = c(x,y,48)
c50 = c(x,y,49)
c51 = c(x,y,50)
c52 = c(x,y,51) 
c53 = c(x,y,52) 
c54 = c(x,y,53) 
c55 = c(x,y,54)
c56 = c(x,y,55) 
c57 = c(x,y,56)
c58 = c(x,y,57) 
c59 = c(x,y,58)
c60 = c(x,y,59) 

def print_d(q):
    if q == "R1":
        return  R1
    elif q == "R2":
        return R2
    elif q == "R3":
        return(R3)
    elif q == "R4":
        return(R4)
    elif q == "R5":
        return(R5)
    elif q == "R6":
        return(R6)
    elif q == "R7":
        return(R7)
    elif q == "R8":
        return(R8)
    elif q == "R9":
        return(R9)
    elif q == "R10":
        return(R10)
    elif q == "R11":
        return R11
    elif q == "R12":
        return R12
    elif q == "R13":
        return R13
    elif q == "R14":
        return R14
    elif q == "R15":
        return R15
    elif q == "R16":
        return R16
    elif q == "R17":
        return R17
    elif q == "R18":
        return R18
    elif q == "R19":
        return R19
    elif q == "R20":
        return R20
    elif q == "R21":
        return R21
    elif q == "R22":
        return R22
    elif q == "R23":
        return R23
    elif q == "R24":
        return R24
    elif q == "R25":
        return R25
    elif q == "R26":
        return R26
    elif q == "R27":
        return R27
    elif q == "R28":
        return R28
    elif q == "R29":
        return R29
    elif q == "R30":
        return R30
    elif q == "R31":
        return R31
    elif q == "R32":
        return R32
    elif q == "R33":
        return R33
    elif q == "R34":
        return R34
    elif q == "R35":
        return R35
    elif q == "R36":
        return R36
    elif q == "R37":
        return R37
    elif q == "R38":
        return R38
    elif q == "R39":
        return R39
    elif q == "R40":
        return R40
    elif q == "R41":
        return R41
    elif q == "R42":
        return R42
    elif q == "R43":
        return R43
    elif q == "R44":
        return R44
    elif q == "R45":
        return R45
    elif q == "B46":
        return B46
    elif q == "B47":
        return B47
    elif q == "B48":
        return B48
    elif q == "B49":
        return B49
    elif q == "B50":
        return B50
    elif q == "B51":
        return B51
    elif q == "B52":
        return B52
    elif q == "B53":
        return B53
    elif q == "B54":
        return B54
    elif q == "B55":
        return B55
    elif q == "B56":
        return B56
    elif q == "B57":
        return B57
    elif q == "B58":
        return B58
    elif q == "B59":
        return B59
    elif q == "B60":
        return B60
    else:
        return "error"

B_ALL = ["B46","B47","B48","B49","B50","B51","B52","B53","B54","B55","B56","B57","B58","B59","B60"]


while True:
    Many = input("ออกมากี่ตัว: ")
    if Many == "end":
        break
    else:
        Many = int(Many)
        w = input("เเสดงตัวไหน:") 
        SLP = 0
        SLN = 0

        d1 = (point_sort(c1))#ระยะห่าง6อันดับ

        R1 = linear_search(c1, d1)#จุดที่ห่าง 6 อันดับ

        R1 = del_d(R1,Many,w)

        d2 = (point_sort(c2))#ระยะห่าง6อันดับ

        R2 = linear_search(c2, d2)#จุดที่ห่าง 6 อันดับ

        R2 = del_d(R2,Many,w)

        d3 = (point_sort(c3))#ระยะห่าง6อันดับ

        R3 = linear_search(c3, d3)#จุดที่ห่าง 6 อันดับ

        R3 = del_d(R3,Many,w)

        d4 = (point_sort(c4))#ระยะห่าง6อันดับ

        R4 = linear_search(c4, d4)#จุดที่ห่าง 6 อันดับ

        R4 = del_d(R4,Many,w)

        d5 = (point_sort(c5))#ระยะห่าง6อันดับ

        R5 = linear_search(c5, d5)#จุดที่ห่าง 6 อันดับ

        R5 = del_d(R5,Many,w)

        d6 = (point_sort(c6))#ระยะห่าง6อันดับ

        R6 = linear_search(c6, d6)#จุดที่ห่าง 6 อันดับ

        R6 = del_d(R6,Many,w)

        d7 = (point_sort(c7))#ระยะห่าง6อันดับ

        R7 = linear_search(c7, d7)#จุดที่ห่าง 6 อันดับ

        R7 = del_d(R7,Many,w)

        d8 = (point_sort(c8))#ระยะห่าง6อันดับ

        R8 = linear_search(c8, d8)#จุดที่ห่าง 6 อันดับ

        R8 = del_d(R8,Many,w)

        d9 = (point_sort(c9))#ระยะห่าง6อันดับ

        R9 = linear_search(c9, d9)#จุดที่ห่าง 6 อันดับ

        d10 = (point_sort(c10))#ระยะห่าง6อันดับ

        R10 = linear_search(c10, d10)#จุดที่ห่าง 6 อันดับ

        d11 = (point_sort(c11))#ระยะห่าง6อันดับ

        R11 = linear_search(c11, d11)#จุดที่ห่าง 6 อันดับ

        d12 = (point_sort(c12))#ระยะห่าง6อันดับ

        R12 = linear_search(c12, d12)#จุดที่ห่าง 6 อันดับ

        d13 = (point_sort(c13))#ระยะห่าง6อันดับ

        R13 = linear_search(c13, d13)#จุดที่ห่าง 6 อันดับ

        d14 = (point_sort(c14))#ระยะห่าง6อันดับ

        R14 = linear_search(c14, d14)#จุดที่ห่าง 6 อันดับ

        d15 = (point_sort(c15))#ระยะห่าง6อันดับ

        R15 = linear_search(c15, d15)#จุดที่ห่าง 6 อันดับ

        d16 = (point_sort(c16))#ระยะห่าง6อันดับ

        R16 = linear_search(c16, d16)#จุดที่ห่าง 6 อันดับ

        d17 = (point_sort(c17))#ระยะห่าง6อันดับ

        R17 = linear_search(c17, d17)#จุดที่ห่าง 6 อันดับ

        d18 = (point_sort(c18))#ระยะห่าง6อันดับ

        R18 = linear_search(c18, d18)#จุดที่ห่าง 6 อันดับ

        d19 = (point_sort(c19))#ระยะห่าง6อันดับ

        R19 = linear_search(c19, d19)#จุดที่ห่าง 6 อันดับ

        d20 = (point_sort(c20))#ระยะห่าง6อันดับ

        R20 = linear_search(c20, d20)#จุดที่ห่าง 6 อันดับ

        d21 = (point_sort(c21))#ระยะห่าง6อันดับ

        R21 = linear_search(c21, d21)#จุดที่ห่าง 6 อันดับ

        d22 = (point_sort(c22))#ระยะห่าง6อันดับ

        R22 = linear_search(c22, d22)#จุดที่ห่าง 6 อันดับ

        d23 = (point_sort(c23))#ระยะห่าง6อันดับ

        R23 = linear_search(c23, d23)#จุดที่ห่าง 6 อันดับ

        d24 = (point_sort(c24))#ระยะห่าง6อันดับ

        R24 = linear_search(c24, d24)#จุดที่ห่าง 6 อันดับ

        d25 = (point_sort(c25))#ระยะห่าง6อันดับ

        R25 = linear_search(c25, d25)#จุดที่ห่าง 6 อันดับ

        d26 = (point_sort(c26))#ระยะห่าง6อันดับ

        R26 = linear_search(c26, d26)#จุดที่ห่าง 6 อันดับ

        d27 = (point_sort(c27))#ระยะห่าง6อันดับ

        R27 = linear_search(c27, d27)#จุดที่ห่าง 6 อันดับ

        d28 = (point_sort(c28))#ระยะห่าง6อันดับ

        R28 = linear_search(c28, d28)#จุดที่ห่าง 6 อันดับ

        d29 = (point_sort(c29))#ระยะห่าง6อันดับ

        R29 = linear_search(c29, d29)#จุดที่ห่าง 6 อันดับ

        d30 = (point_sort(c30))#ระยะห่าง6อันดับ

        R30 = linear_search(c30, d30)#จุดที่ห่าง 6 อันดับ

        d31 = (point_sort(c31))#ระยะห่าง6อันดับ

        R31 = linear_search(c31, d31)#จุดที่ห่าง 6 อันดับ

        d32 = (point_sort(c32))#ระยะห่าง6อันดับ

        R32 = linear_search(c32, d32)#จุดที่ห่าง 6 อันดับ

        d33 = (point_sort(c33))#ระยะห่าง6อันดับ

        R33 = linear_search(c33, d33)#จุดที่ห่าง 6 อันดับ

        d34 = (point_sort(c34))#ระยะห่าง6อันดับ

        R34 = linear_search(c34, d34)#จุดที่ห่าง 6 อันดับ

        d35 = (point_sort(c35))#ระยะห่าง6อันดับ

        R35 = linear_search(c35, d35)#จุดที่ห่าง 6 อันดับ

        d36 = (point_sort(c36))#ระยะห่าง6อันดับ

        R36 = linear_search(c36, d36)#จุดที่ห่าง 6 อันดับ

        d37 = (point_sort(c37))#ระยะห่าง6อันดับ

        R37 = linear_search(c37, d37)#จุดที่ห่าง 6 อันดับ

        d38 = (point_sort(c38))#ระยะห่าง6อันดับ

        R38 = linear_search(c38, d38)#จุดที่ห่าง 6 อันดับ

        d39 = (point_sort(c39))#ระยะห่าง6อันดับ

        R39 = linear_search(c39, d39)#จุดที่ห่าง 6 อันดับ

        d40 = (point_sort(c40))#ระยะห่าง6อันดับ

        R40 = linear_search(c40, d40)#จุดที่ห่าง 6 อันดับ

        d41 = (point_sort(c41))#ระยะห่าง6อันดับ

        R41 = linear_search(c41, d41)#จุดที่ห่าง 6 อันดับ

        d42 = (point_sort(c42))#ระยะห่าง6อันดับ

        R42 = linear_search(c42, d42)#จุดที่ห่าง 6 อันดับ

        d43 = (point_sort(c43))#ระยะห่าง6อันดับ

        R43 = linear_search(c43, d43)#จุดที่ห่าง 6 อันดับ

        d44 = (point_sort(c44))#ระยะห่าง6อันดับ

        R44 = linear_search(c44, d44)#จุดที่ห่าง 6 อันดับ

        d45 = (point_sort(c45))#ระยะห่าง6อันดับ

        R45 = linear_search(c45, d45)#จุดที่ห่าง 6 อันดับ

        d46 = (point_sort(c46))#ระยะห่าง6อันดับ

        B46 = linear_search(c46, d46)#จุดที่ห่าง 6 อันดับ

        d47 = (point_sort(c47))#ระยะห่าง6อันดับ

        B47 = linear_search(c47, d47)#จุดที่ห่าง 6 อันดับ

        d48 = (point_sort(c48))#ระยะห่าง6อันดับ

        B48 = linear_search(c48, d48)#จุดที่ห่าง 6 อันดับ

        d49 = (point_sort(c49))#ระยะห่าง6อันดับ

        B49 = linear_search(c49, d49)#จุดที่ห่าง 6 อันดับ

        d50 = (point_sort(c50))#ระยะห่าง6อันดับ

        B50 = linear_search(c50, d50)#จุดที่ห่าง 6 อันดับ

        d51 = (point_sort(c51))#ระยะห่าง6อันดับ

        B51 = linear_search(c51, d51)#จุดที่ห่าง 6 อันดับ

        d52 = (point_sort(c52))#ระยะห่าง6อันดับ

        B52 = linear_search(c52, d52)#จุดที่ห่าง 6 อันดับ

        d53 = (point_sort(c53))#ระยะห่าง6อันดับ

        B53 = linear_search(c53, d53)#จุดที่ห่าง 6 อันดับ

        d54 = (point_sort(c54))#ระยะห่าง6อันดับ

        B54 = linear_search(c54, d54)#จุดที่ห่าง 6 อันดับ

        d55 = (point_sort(c55))#ระยะห่าง6อันดับ

        B55 = linear_search(c55, d55)#จุดที่ห่าง 6 อันดับ

        d56 = (point_sort(c56))#ระยะห่าง6อันดับ

        B56 = linear_search(c56, d56)#จุดที่ห่าง 6 อันดับ

        d57 = (point_sort(c57))#ระยะห่าง6อันดับ

        B57 = linear_search(c57, d57)#จุดที่ห่าง 6 อันดับ

        d58 = (point_sort(c58))#ระยะห่าง6อันดับ

        B58 = linear_search(c58, d58)#จุดที่ห่าง 6 อันดับ

        d59 = (point_sort(c59))#ระยะห่าง6อันดับ

        B59 = linear_search(c59, d59)#จุดที่ห่าง 6 อันดับ

        d60 = (point_sort(c60))#ระยะห่าง6อันดับ

        B60 = linear_search(c60, d60)#จุดที่ห่าง 6 อันดับ

        R9 = del_d(R9,Many,w)
        R10 = del_d(R10,Many,w)
        R11 = del_d(R11,Many,w)
        R12 = del_d(R12,Many,w)
        R13 = del_d(R13,Many,w)
        R14 = del_d(R14,Many,w)
        R15 = del_d(R15,Many,w)
        R16 = del_d(R16,Many,w)
        R17 = del_d(R17,Many,w)
        R18 = del_d(R18,Many,w)
        R19 = del_d(R19,Many,w)
        R20 = del_d(R20,Many,w)
        R21 = del_d(R21,Many,w)
        R22 = del_d(R22,Many,w)
        R23 = del_d(R23,Many,w)
        R24 = del_d(R24,Many,w)
        R25 = del_d(R25,Many,w)
        R26 = del_d(R26,Many,w)
        R27 = del_d(R27,Many,w)
        R28 = del_d(R28,Many,w)
        R29 = del_d(R29,Many,w)
        R30 = del_d(R30,Many,w)
        R31 = del_d(R31,Many,w)
        R32 = del_d(R32,Many,w)
        R33 = del_d(R33,Many,w)
        R34 = del_d(R34,Many,w)
        R35 = del_d(R35,Many,w)
        R36 = del_d(R36,Many,w)
        R37 = del_d(R37,Many,w)
        R38 = del_d(R38,Many,w)
        R39 = del_d(R39,Many,w)
        R40 = del_d(R40,Many,w)
        R41 = del_d(R41,Many,w)
        R42 = del_d(R42,Many,w)
        R43 = del_d(R43,Many,w)
        R44 = del_d(R44,Many,w)
        R45 = del_d(R45,Many,w)
        B46 = del_d(B46,Many,w)
        B47 = del_d(B47,Many,w)
        B48 = del_d(B48,Many,w)
        B49 = del_d(B49,Many,w)
        B50 = del_d(B50,Many,w)
        B51 = del_d(B51,Many,w)
        B52 = del_d(B52,Many,w)
        B53 = del_d(B53,Many,w)
        B54 = del_d(B54,Many,w)
        B55 = del_d(B55,Many,w)
        B56 = del_d(B56,Many,w)
        B57 = del_d(B57,Many,w)
        B58 = del_d(B58,Many,w)
        B59 = del_d(B59,Many,w)
        B60 = del_d(B60,Many,w)

        w_TO_W = print_d(w)

        if w_TO_W == "error":
            print(w_TO_W)
            break
        else:
            print("%s: "%(w) ,end = "")
            print(w_TO_W)
            print("SLP: ",end = "")
            SLP = linear_search_SLP(w_TO_W,B_ALL,SLP)
            print(SLP)
            print("--------------------------------------------------- ")
            n = input("N คือ: ")
            while n != "end":
                n_TO_N = print_d(n)
                while linear_search_N(w_TO_W,n) == "error":
                    n = input("N คือ: ")
                    n_TO_N = print_d(n)
                print("%s: "%(n),end = "")
                print(n_TO_N)
                print("SLN: ",end= "")
                SLN = linear_search_SLN(n_TO_N,B_ALL,SLN,w)
                print(SLN)
                if SLN == 0:
                    print("SL_ratio = Infinity")
                else:
                    SL_ratio = SLP/SLN
                    print("SL_ratio = %f" %(SL_ratio))
                print("")
                n = input("N คือ: ")
                SLN = 0