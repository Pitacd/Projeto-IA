minus="-"
plus="+"
x="x"
o="o"
blank=0

whichFormRemove=0 #0=dont remove|1 or more is which form to remove in the respective piece type
#b=board
#l=line
#c=column


def removeForms(b, piece, l, c): #returns [bWithAlterations,points]
    b[l][c]=piece
    if piece==minus:
        return verifyMinus(b, l, c)
    elif piece==plus:
        return verifyPlus(b)
    elif piece==x:
        return verifyX(b)
    elif piece==o:
        return verifyCircle(b)
    else:
        print("Piece doesnt exist.\n")
        return [b,0]


#/\/\/\/\/\/\/\/\/\/\/\/  "-"  \/\/\/\/\/\/\/\/\/\/\/\
def verifyMinus(b, l, c):
    points=0
    numberOfMinus=1
    if not c==0:
        if b[l][c-1]==minus:
            b[l][c-1]=blank
            numberOfMinus+=1
    if not c==4:
        if b [l][c+1]==minus:
            b[l][c+1]=blank
            numberOfMinus+=1
    if not numberOfMinus==1:
        b[l][c]=blank
        points+=2**numberOfMinus
    return [b,points]


#/\/\/\/\/\/\/\/\/\/\/\/  "+"  \/\/\/\/\/\/\/\/\/\/\/\
def verifyPlus(b):
    points=0
    if isBigPlus(b):
        removeBigPlus(b)
        points+=2**9
    elif isSmallPlus(b):
        removeSmallPlus(b)
        points+=2**5
    return [b,points]

def isBigPlus(b):
    return (b[2][0]==plus and b[2][1]==plus and b[2][2]==plus and b[2][3]==plus and b[2][4]==plus and b[0][2]==plus and b[1][2]==plus and b[3][2]==plus and b[4][2]==plus)
def removeBigPlus(b):
    b[2]=[blank,blank,blank,blank,blank]
    b[0][2]=blank
    b[1][2]=blank
    b[3][2]=blank
    b[4][2]=blank
    return b

def isSmallPlus(b):
    #whichFormRemove: 0=none|1-9 left->right top->bottom
    global whichFormRemove
    whichFormRemove=0
    i=0
    possibleSmall=[[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]  #REFERENCE TO THE MIDDLE PIECE
    for p in possibleSmall:
        i+=1
        if (b[p[0]][p[1]]==plus and b[p[0]+1][p[1]]==plus and b[p[0]-1][p[1]]==plus and b[p[0]][p[1]+1]==plus and b[p[0]][p[1]-1]==plus):
            whichFormRemove=i
            break
    return whichFormRemove
def removeSmallPlus(b):
    possibleSmall=[[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]
    p=possibleSmall[whichFormRemove-1]
    b[p[0]][p[1]]=blank
    b[p[0]+1][p[1]]=blank
    b[p[0]-1][p[1]]=blank
    b[p[0]][p[1]+1]=blank
    b[p[0]][p[1]-1]=blank
    return b

#/\/\/\/\/\/\/\/\/\/\/\/  "x"  \/\/\/\/\/\/\/\/\/\/\/\
def verifyX(b):
    points=0
    if isBigX(b):
        removeBigX(b)
        points+=2**9
    elif isSmallX(b):
        removeSmallX(b)
        points+=2**5
    return [b,points]

def isBigX(b):
    return (b[0][0]==x and b[1][1]==x and b[2][2]==x and b[3][3]==x and b[4][4]==x and b[0][4]==x and b[1][3]==x and b[3][1]==x and b[4][0]==x)
def removeBigX(b):
    b[0][0]=blank
    b[1][1]=blank
    b[2][2]=blank
    b[3][3]=blank
    b[4][4]=blank 
    b[0][4]=blank
    b[1][3]=blank
    b[3][1]=blank
    b[4][0]=blank
    return b

def isSmallX(b):
    #whichFormRemove: 0=none|1-9 left->right top->bottom
    global whichFormRemove
    whichFormRemove=0
    i=0
    possibleSmall=[[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]  #REFERENCE TO THE MIDDLE PIECE
    for p in possibleSmall:
        i+=1
        if b[p[0]][p[1]]==x and b[p[0]-1][p[1]-1]==x and b[p[0]-1][p[1]+1]==x and b[p[0]+1][p[1]-1]==x and b[p[0]+1][p[1]+1]==x:
            whichFormRemove=i
            break
    return whichFormRemove
def removeSmallX(b):
    possibleSmall=[[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]
    p=possibleSmall[whichFormRemove-1]
    b[p[0]][p[1]]=blank
    b[p[0]-1][p[1]-1]=blank
    b[p[0]-1][p[1]+1]=blank
    b[p[0]+1][p[1]-1]=blank
    b[p[0]+1][p[1]+1]=blank
    return b
#/\/\/\/\/\/\/\/\/\/\/\/  "o"  \/\/\/\/\/\/\/\/\/\/\/\
def verifyCircle(b):
    points=0
    if isMegaCircle(b): # if is MEGA, 5x5  16pieces
        b=removeMegaCircle(b)
        points+=2**16
    elif isBigCircle(b):# if is BIG, 4x4  12pieces
        b=removeBigCircle(b)
        points+=2**12
    elif isMidCircle(b):# if is MID, 3x3  8pieces
        b=removeMidCircle(b)
        points+=2**8
    elif isSmallCircle(b):# if is SMALL, 2x2  4pieces
        removeSmallCircle(b)
        points+=2**4
    return [b,points]

def isMegaCircle(b):
    return (b[0][0]==o and b[0][1]==o and b[0][2]==o and b[0][3]==o and b[0][4]==o and b[1][0]==o and b[2][0]==o and b[3][0]==o and b[4][0]==o and b[4][1]==o and b[4][2]==o and b[4][3]==o and b[4][4]==o and b[3][4]==o and b[2][4]==o and b[1][4]==o)
def removeMegaCircle(b):
    b[0]=[blank,blank,blank,blank,blank]
    b[4]=[blank,blank,blank,blank,blank]
    b[1][0]=blank
    b[2][0]=blank
    b[3][0]=blank
    b[1][4]=blank
    b[2][4]=blank
    b[3][4]=blank
    return b

def isBigCircle(b):
    #whichFormRemove: 0=none|1=top left|2= top right|3=bottom left|4=bottom right
    global whichFormRemove
    whichFormRemove=0
    i=0
    possibleBig=[[0,0],[0,1],[1,0],[1,1]]
    for p in possibleBig:
        i+=1
        if b[p[0]][p[1]]==o and b[p[0]][p[1]+1]==o and b[p[0]][p[1]+2]==o and b[p[0]][p[1]+3]==o and b[p[0]+1][p[1]]==o and b[p[0]+2][p[1]]==o and b[p[0]+3][p[1]]==o and b[p[0]+3][p[1]+1]==o and b[p[0]+3][p[1]+2]==o and b[p[0]+3][p[1]+3]==o and b[p[0]+2][p[1]+3]==o and b[p[0]+1][p[1]+3]==o:
            whichFormRemove=i
            break
    return whichFormRemove
def removeBigCircle (b):
    possibleBig=[[0,0],[0,1],[1,0],[1,1]]
    p=possibleBig[whichFormRemove-1]
    b[p[0]][p[1]]=blank
    b[p[0]][p[1]+1]=blank
    b[p[0]][p[1]+2]=blank
    b[p[0]][p[1]+3]=blank
    b[p[0]+1][p[1]]=blank
    b[p[0]+2][p[1]]=blank
    b[p[0]+3][p[1]]=blank
    b[p[0]+3][p[1]+1]=blank
    b[p[0]+3][p[1]+2]=blank
    b[p[0]+3][p[1]+3]=blank
    b[p[0]+2][p[1]+3]=blank
    b[p[0]+1][p[1]+3]=blank
    return b

def isMidCircle(b):
    #whichFormRemove: 0=none|1-9 left->right top->bottom
    global whichFormRemove
    whichFormRemove=0
    i=0
    possibleMid=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    for p in possibleMid:
        i+=1
        if b[p[0]][p[1]]==o and b[p[0]][p[1]+1]==o and b[p[0]][p[1]+2]==o and b[p[0]+1][p[1]]==o and b[p[0]+2][p[1]]==o and b[p[0]+2][p[1]+1]==o and b[p[0]+2][p[1]+2]==o and b[p[0]+1][p[1]+2]==o:
            whichFormRemove=i
            break
    return whichFormRemove
def removeMidCircle (b):
    possibleMid=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    p=possibleMid[whichFormRemove-1]
    b[p[0]][p[1]]=blank
    b[p[0]][p[1]+1]=blank
    b[p[0]][p[1]+2]=blank
    b[p[0]+1][p[1]]=blank
    b[p[0]+2][p[1]]=blank
    b[p[0]+2][p[1]+1]=blank
    b[p[0]+2][p[1]+2]=blank
    b[p[0]+1][p[1]+2]=blank
    return b

def isSmallCircle(b):
    #whichFormRemove: 0=none|1-16 left->right top->bottom
    global whichFormRemove
    whichFormRemove=0
    i=0
    possibleSmall=[[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]
    for p in possibleSmall:
        i+=1
        if b[p[0]][p[1]]==o and b[p[0]+1][p[1]]==o and b[p[0]][p[1]+1]==o and b[p[0]+1][p[1]+1]==o:
            whichFormRemove=i
            break
    return whichFormRemove
def removeSmallCircle (b):
    possibleSmall=[[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]
    p=possibleSmall[whichFormRemove-1]
    b[p[0]][p[1]]=blank
    b[p[0]+1][p[1]]=blank
    b[p[0]][p[1]+1]=blank
    b[p[0]+1][p[1]+1]=blank
    return b