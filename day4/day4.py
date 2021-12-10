### list comprehensions ? what are they???

# first line of input is draw
# boards are in boards.txt

draw = [15,62,2,39,49,25,65,28,84,59,75,24,20,76,60,55,17,7,93,69,32,23,44,81,8,67,41,56,43,89,95,97,61,77,64,37,29,10,79,26,51,48,5,86,71,58,78,90,57,82,45,70,11,14,13,50,68,94,99,22,47,12,1,74,18,46,4,6,88,54,83,96,63,66,35,27,36,72,42,98,0,52,40,91,33,21,34,85,3,38,31,92,9,87,19,73,30,16,53,80]

puzzle = open("boards.txt")

boards = []

#first board
board = []
for line in puzzle.readlines():
    if line == "\n":
        boards.append(board)
        board = []
    else:
        arr = []
        for n in line.split():
            arr.append(int(n))
        board.append(arr)
#last board
boards.append(board)

marked = [[[0,0,0,0,0] for __ in range(5)] for _ in range(len(boards))]

sols = []
avoid = []

def bingo(mul, index_board):
    sum = 0
    for r, row in enumerate(boards[index_board]):
        for c, el in enumerate(row):
            if marked[index_board][r][c] == 0:
                sum += el
    sols.append(sum * mul)
    avoid.append(index_board)

for d in draw:
    
    # look for d in every board
        # update accordingly
            # look at single row and column for bingo

    for index_board, board in enumerate(boards):
        for ir, r in enumerate(board):
            #ugly
            if index_board in avoid:
                break
            for ic, el in enumerate(r):
                if d == el:
                    marked[index_board][ir][ic] = 1
                    
                    tot = 0
                    for row in marked[index_board]:
                        if row[ic] == 1:
                            tot += 1
                    if tot == 5:
                        bingo(d, index_board) 
                        break
                    if 0 in marked[index_board][ir]:
                        break
                    bingo(d, index_board)

print(f"sol1 is {sols[0]} and sol2 is {sols[-1]}")
