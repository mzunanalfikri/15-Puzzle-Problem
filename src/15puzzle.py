#import depedencies
import copy
import time
from collections import deque

#kelas puzzle
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
        self.u = None
        self.l = None
        self.d = None
        self.r = None

    def countCostFunction(self):
    #fungsi untuk menghitung costfunction untuk tiap simpul
        count  = 0
        for i in range(4):
            for j in range(4):
                if (self.mat[i][j] != Puzzle.reference[i][j]):
                    count += 1
        return count;

    def generateUp(self):
    #fungsi untuk generate sumpul jika puzzle yang kosong digeser ke atas
        if (self.basis[0] - 1 >= 0):
            Puzzle.banyak_simpul += 1
            self.u = copy.deepcopy(self)
            self.u.mat[self.basis[0]][self.basis[1]] = self.u.mat[self.basis[0] - 1][self.basis[1]]
            self.u.mat[self.basis[0] - 1][self.basis[1]] = 0 
            self.u.basis = (self.basis[0] - 1 , self.basis[1])
            self.u.path  += "u"
            self.u.costfunction = self.u.countCostFunction() + len(self.u.path)

    def generateLeft(self):
    #fungsi untuk generate simpul jika puzzle yang kosong digeser ke kiri
        if (self.basis[1] - 1 >= 0):
            Puzzle.banyak_simpul += 1
            self.l = copy.deepcopy(self)
            self.l.mat[self.basis[0]][self.basis[1]] = self.l.mat[self.basis[0]][self.basis[1] - 1]
            self.l.mat[self.basis[0]][self.basis[1] - 1] = 0 
            self.l.basis = (self.basis[0] , self.basis[1] - 1)
            self.l.path  += "l"
            self.l.costfunction = self.l.countCostFunction() + len(self.l.path)

    def generateDown(self):
    #fungsi untuk generate simpul jika puzzle yang kosong digeser ke bawah
        if (self.basis[0] + 1 <= 3):
            Puzzle.banyak_simpul += 1
            self.d = copy.deepcopy(self)
            self.d.mat[self.basis[0]][self.basis[1]] = self.d.mat[self.basis[0] + 1][self.basis[1]]
            self.d.mat[self.basis[0] + 1][self.basis[1]] = 0 
            self.d.basis = (self.basis[0] + 1 , self.basis[1])
            self.d.path  += "d"
            self.d.costfunction = self.d.countCostFunction() + len(self.d.path)

    def generateRight(self):
    #fungsi untuk generate simpul jika puzzle yang kosong digeser ke kanan
        if (self.basis[1] + 1 <= 3):
            Puzzle.banyak_simpul += 1
            self.r = copy.deepcopy(self)
            self.r.mat[self.basis[0]][self.basis[1]] = self.r.mat[self.basis[0]][self.basis[1] + 1]
            self.r.mat[self.basis[0]][self.basis[1] + 1] = 0 
            self.r.basis = (self.basis[0] , self.basis[1] + 1)
            self.r.path  += "r"
            self.r.costfunction = self.r.countCostFunction() + len(self.r.path)

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
    #fungsi untuk menerima input dari console
        for i in range(4):
            temp = str(input())
            self.mat[i] = temp.split()
            for j in range(4):
                self.mat[i][j] = int(self.mat[i][j])
                if (self.mat[i][j] == 0):
                    self.basis = (i,j)
                if (self.mat[i][j] != Puzzle.reference[i][j]):
                    self.costfunction += 1
                
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
        print("Kurangi(i) : ", count)
        if (count % 2 == 0):
            # print("Solvable")
            return True
        else :
            # print("Not Solvable")
            return False

    def isInputValid(self):
    #fungsi mengembalikan true jika puzzle yang dimasukkan valid
        valid = [0 for i in range(16)]
        for i in range(4):
            for j in range(4):
                if (self.mat[i][j] > 15 or self.mat[i][j] < 0):
                    return False
                else :
                    valid[self.mat[i][j]] += 1
        for i in valid:
            if (i == 0):
                return False
        return True

def isEqual(matA, matB):
#mengembalikan true jika matriks A dan B sama
    for i in range(4):
        for j in range(4):
            if (matA[i][j] != matB[i][j]):
                return False
    return True

def isContain(kandidat, mat):
#mengembalikan true jika dalam array kandidat terdapat matriks mat
    for i in kandidat:
        if (isEqual(i, mat)):
            return True
    return False

def isFinish(mat, reference):
#mengembalikan true jika mat mencapai target
    return isEqual(mat, reference)

def sortQueue(Q):
#fungsi untuk sort Queue Q agar memenuhi prio Que
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
    end = isFinish(current.mat, Puzzle.reference)
    while(not(end)):
        #generate simpul W
        current.generateUp()
        if (current.u != None):
            if (isContain(kandidat, current.u.mat)):
                Puzzle.banyak_simpul -= 1
                current.u = None
            else :
                kandidat.append(current.u.mat)
                Q.append(current.u)
                if (isFinish(current.u.mat, Puzzle.reference)):
                    current = current.u
                    break
        #generate simpul A
        current.generateLeft()
        if (current.l != None):
            if (isContain(kandidat, current.l.mat)):
                Puzzle.banyak_simpul -= 1
                current.l = None
            else :
                kandidat.append(current.l.mat)
                Q.append(current.l)
                if (isFinish(current.l.mat, Puzzle.reference)):
                    current = current.l
                    break
        #generate S
        current.generateDown()
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
        #generate D
        current.generateRight()
        if (current.r != None):
            if (isContain(kandidat, current.r.mat)):
                Puzzle.banyak_simpul -= 1
                current.r = None
            else :
                kandidat.append(current.r.mat)
                Q.append(current.r)
                if (isFinish(current.r.mat, Puzzle.reference)):
                    current = current.r
                    break
        sortQueue(Q)
        current = Q.popleft()
        # print(Puzzle.banyak_simpul)
    return current

def masukanInput(Puz):
#prosedur untuk meminta pilihan input
    print("Pilih opsi cara memasukkan puzzle : ")
    print("1. Masukan dari file")
    print("2. Masukan dari console")
    x = int(input("Masukkan pilihan : "))
    if (x == 1):
        filename = str(input("Masukkan path file : "))
        Puz.readFile(filename)
    else :
        print()
        print("Masukkan 4 baris matriks, pisahkan dengan spasi, contoh : \n1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 0")
        Puz.inputFromConsole()

def cetakMatriks(mat):
#prosedur untuk mencetak matriks
    for i in range(4):
        for j in range(4):
            print(mat[i][j], end = " ")
        print()

def cetakPath(res, puz):
#prosedur untuk mencetak path
    mat = puz.mat
    basis = puz.basis
    path = res.path
    for i in path:
        if (i == "u"):
            print("Langkah : up")
            mat[basis[0]][basis[1]] = mat[basis[0] - 1][basis[1]]
            mat[basis[0] - 1][basis[1]] = 0
            basis = (basis[0] - 1, basis[1])
        elif (i == "l"):
            print("Langkah : left")
            mat[basis[0]][basis[1]] = mat[basis[0]][basis[1] - 1]
            mat[basis[0]][basis[1] - 1] = 0
            basis = (basis[0], basis[1] - 1)
        elif (i == "d"):
            print("Langkah : down")
            mat[basis[0]][basis[1]] = mat[basis[0] + 1][basis[1]]
            mat[basis[0] + 1][basis[1]] = 0
            basis = (basis[0] + 1, basis[1])
        elif (i == "r"):
            print("Langkah : right")
            mat[basis[0]][basis[1]] = mat[basis[0]][basis[1] + 1]
            mat[basis[0]][basis[1] + 1] = 0
            basis = (basis[0], basis[1] + 1)
        cetakMatriks(mat)

#Kamus 
kandidat = []
Q = deque()
Puz = Puzzle()

#Algoritma
print("============ SELAMAT DATANG DI PROGRAM 15 Puzzle ! ================")
print()
masukanInput(Puz)

print()
if (not Puz.isInputValid()):
    print("Input tidak valid, masukkan Puzzle lagi !")
    masukanInput(Puz)
print("Input Puzzle : ")
cetakMatriks(Puz.mat)
if (Puz.isSolvable()):
    print("Puzzle dapat diselesaikan !")
    now = time.time()
    Result = solvePuzzle(Puz, Q, kandidat)
    print("Waktu yand dibutuhkan : ", time.time()-now)
    print("Simpul yang di bangkitkan : ", Puzzle.banyak_simpul)
    print("Banyak langkah : ", len(Result.path))
    print("Path : ", Result.path)
    print()
    cetak = str(input("Cetak langkah ? (y/n)"))
    if (cetak == "Y" or cetak == "y"):
         cetakPath(Result, Puz)    
else :
    print("Puzzle tidak dapat diselesaikan")