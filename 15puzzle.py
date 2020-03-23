import copy
from collections import deque

#y, x = i, j
class Puzzle:
    banyak_simpul = 0
    reference = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,0]]

    def __init__(self):
    #fungsi untuk konstruktor
        Puzzle.banyak_simpul += 1
        self.mat = [[0 for i in range(4)] for i in range(4)]
        self.basis = (0,0)
        self.path = ""
        self.costfunction = 0
        self.w = None
        self.a = None
        self.s = None
        self.d = None

    def countCostFunction(self):
        count  = 0
        for i in range(4):
            for j in range(4):
                if (self.mat[i][j] != Puzzle.reference[i][j]):
                    count += 1
        return count;

    def generateW(self):
    #fungsi untuk generate sumpul jika puzzle yang kosong digeser ke atas
        if (self.basis[0] - 1 >= 0):
            Puzzle.banyak_simpul += 1
            self.w = copy.deepcopy(self)
            self.w.mat[self.basis[0]][self.basis[1]] = self.w.mat[self.basis[0] - 1][self.basis[1]]
            self.w.mat[self.basis[0] - 1][self.basis[1]] = 0 
            self.w.basis = (self.basis[0] - 1 , self.basis[1])
            self.w.path  += "w"
            self.w.costfunction = self.w.countCostFunction() + len(self.w.path)

    def generateA(self):
    #fungsi untuk generate simpul jika puzzle yang kosong digeser ke kiri
        if (self.basis[1] - 1 >= 0):
            Puzzle.banyak_simpul += 1
            self.a = copy.deepcopy(self)
            self.a.mat[self.basis[0]][self.basis[1]] = self.a.mat[self.basis[0]][self.basis[1] - 1]
            self.a.mat[self.basis[0]][self.basis[1] - 1] = 0 
            self.a.basis = (self.basis[0] , self.basis[1] - 1)
            self.a.path  += "a"
            self.a.costfunction = self.a.countCostFunction() + len(self.a.path)

    def generateS(self):
    #fungsi untuk generate simpul jika puzzle yang kosong digeser ke bawah
        if (self.basis[0] + 1 <= 3):
            Puzzle.banyak_simpul += 1
            self.s = copy.deepcopy(self)
            self.s.mat[self.basis[0]][self.basis[1]] = self.s.mat[self.basis[0] + 1][self.basis[1]]
            self.s.mat[self.basis[0] + 1][self.basis[1]] = 0 
            self.s.basis = (self.basis[0] + 1 , self.basis[1])
            self.s.path  += "s"
            self.s.costfunction = self.s.countCostFunction() + len(self.s.path)

    def generateD(self):
    #fungsi untuk generate simpul jika puzzle yang kosong digeser ke kanan
        if (self.basis[1] + 1 <= 3):
            Puzzle.banyak_simpul += 1
            self.d = copy.deepcopy(self)
            self.d.mat[self.basis[0]][self.basis[1]] = self.d.mat[self.basis[0]][self.basis[1] + 1]
            self.d.mat[self.basis[0]][self.basis[1] + 1] = 0 
            self.d.basis = (self.basis[0] , self.basis[1] + 1)
            self.d.path  += "d"
            self.d.costfunction = self.d.countCostFunction() + len(self.d.path)

    def cetakPuzzle(self):
    #fungsi untuk mencetak puzzle
        for i in self.mat:
            for j in range(4):
                print(i[j], end = " ")
            print()
        print("Cost Function : ", self.costfunction)
        print("Basis : ", self.basis[0], self.basis[1])
        print("Path : ", self.path)
        print("Banyak simpul : ", Puzzle.banyak_simpul)

    def inputFromConsole(self):
        for i in range(4):
            for j in range(4):
                self.mat[i][j] = int(input())
                
    def readFile(self, filename):
    #fungsi untuk membaca dari file dan dimasukkan ke matriks
        f = open(filename, "r")
        for i in range(4):
            temp = f.readline()
            self.mat[i] = temp.split()
            for j in range(4):
                self.mat[i][j] = int(self.mat[i][j])
                if (self.mat[i][j] == 0):
                    self.basis = (i,j)
                if (self.mat[i][j] != Puzzle.reference[i][j]):
                    self.costfunction += 1
        f.close()
        

    def cetakBasis(self):
    #fungsi untuk mencetak basis
        print(self.basis[0] , self.basis[1])

    def isSolvable(self):
    #fungsi untuk cek apakah solvable atau tidak
        count = 0
        temp = []
        for i in range(4):
            for j in range(4):
                if (self.mat[i][j] == 0):
                    temp.append(16)
                else :
                    temp.append(self.mat[i][j])
        for i in range(len(temp)):
            for j in range(i+1, len(temp)):
                if (temp[i] > temp[j]):
                    count += 1
        if ((self.basis[0] + self.basis[1]) % 2 == 1):
            count += 1
        if (count % 2 == 0):
            print("Solvable")
            return True
        else :
            print("Not Solvable")
            return False

def isEqual(matA, matB):
    for i in range(4):
        for j in range(4):
            if (matA[i][j] != matB[i][j]):
                return False
    return True

def isContain(kandidat, mat):
    for i in kandidat:
        if (isEqual(i, mat)):
            return True
    return False

def isFinish(mat, reference):
    return isEqual(mat, reference)

def sortQueue(Q):
    for i in range(len(Q)):
        for j in range(i+1, len(Q)):
            if (Q[i].costfunction > Q[j].costfunction):
                temp = Q[i]
                Q[i] = Q[j]
                Q[j] = temp

def solvePuzzle(Puzz, Q, kandidat):
#fungsi untukk mencari path
    current = Puzz
    kandidat.append(Puzz.mat)
    while(True):
        #generate simpul W
        current.generateW()
        if (current.w != None):
            if (isContain(kandidat, current.w.mat)):
                Puzzle.banyak_simpul -= 1
                current.w = None
            else :
                kandidat.append(current.w.mat)
                Q.append(current.w)
                if (isFinish(current.w.mat, Puzzle.reference)):
                    current = current.w
                    break
        #generate simpul A
        current.generateA()
        if (current.a != None):
            if (isContain(kandidat, current.a.mat)):
                Puzzle.banyak_simpul -= 1
                current.a = None
            else :
                kandidat.append(current.a.mat)
                Q.append(current.a)
                if (isFinish(current.a.mat, Puzzle.reference)):
                    current = current.a
                    break
        #generate S
        current.generateS()
        if (current.s != None):
            if (isContain(kandidat, current.s.mat)):
                Puzzle.banyak_simpul -= 1
                current.s = None
            else :
                kandidat.append(current.s.mat)
                Q.append(current.s)
                if (isFinish(current.s.mat, Puzzle.reference)):
                    current = current.s
                    break
        #generate D
        current.generateD()
        if (current.d != None):
            if (isContain(kandidat, current.d.mat)):
                Puzzle.banyak_simpul -= 1
                current.d = None
            else :
                kandidat.append(current.d.mat)
                Q.append(current.d)
                if (isFinish(current.d.mat, Puzzle.reference)):
                    current = current.d
                    break
        # sortQueue(Q)
        current = Q.popleft()
        print(Puzzle.banyak_simpul)

    return current

#ALGORITMA

kandidat = []
Q = deque()

Puz = Puzzle()
# Puz.cetakPuzzle()
Puz.readFile("config.txt")
Puz.isSolvable()
# Puz.cetakPuzzle()
# print("Hasil : ", solvePuzzle(Puz, Q, kandidat).path)
# print("banyak simpul : ", Puzzle.banyak_simpul)
solvePuzzle(Puz, Q, kandidat).cetakPuzzle()


# print("="*14)
# Puz.cetakPuzzle()
# Puz.w.cetakPuzzle()

