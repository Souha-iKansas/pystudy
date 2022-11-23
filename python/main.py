#!/usr/bin/env python3

SIZE = 3

class sudoku():
    #二次元配列を書きたい
    def __init__(self):
        self.cells = [[None for i in range(SIZE*SIZE)] for j in range(SIZE*SIZE)]
#        print(self.cells)
        self.count = 0

    #標準入力から問題を入力するメソッドを書きたい
    def input(self):
        for i in range(SIZE*SIZE):
            line = input()
#            print(line)
            line = line.split()
            for index, num in enumerate(line):
                if num != '-':
                    self.cells[i][index] = int(num)
                else:
                    self.cells[i][index] = -1
#        print(self.cells)

    #標準出力から整形して出力するメソッドを書きたい
    def print(self):
        for i, line in enumerate(self.cells):
            for j, num in enumerate(line):
                if num == -1:
                    print(' ', end=' ')
                else:
                    print(num, end=' ')
            print()

    #空欄を一個探すメソッドを書きたい
    def get_first_blank(self):
        for i, line in enumerate(self.cells):
            for j, num in enumerate(line):
                if num == -1:
                    return i, j
        return None
    
    #候補の手をリストにするメソッド
    def get_candidates(self, row, col):
        hist = {i+1: 0 for i in range(SIZE*SIZE)}
        hist[-1] = 0
        for i in range(SIZE*SIZE):
            hist[self.cells[row][i]] += 1
            hist[self.cells[i][col]] += 1
        block_row = row//3
        block_col = col//3
        block_row_head = block_row*3
        block_col_head = block_col*3
        for r in range(SIZE):
            for c in range(SIZE):
                hist[self.cells[r+block_row_head][c+block_col_head]] += 1
        
        result = []
        for i in range(SIZE*SIZE):
            if hist[i+1] == 0:
                result.append(i+1)
        return result

    #空欄に値を深さ探求で埋めていく
    def dfs(self):
        self.count += 1
        blank = self.get_first_blank()
        if blank == None:
            return True
        row, col = blank
        cands = self.get_candidates(row, col)
        for num in cands:
            #print(cands)
            self.cells[row][col] = num
            if self.dfs() == True:
                return True
        self.cells[row][col] = -1
        return False

def main():
    sdk = sudoku()
    sdk.input()
    sdk.print()
    row, col = sdk.get_first_blank()
    sdk.get_candidates(row, col)
    sdk.dfs()
    sdk.print()
    print(sdk.count)

if __name__ == '__main__':
    main()