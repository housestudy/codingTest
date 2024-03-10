# 내 답
# 81점...
beginning = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
target = [[1, 0, 1], [0, 0, 0], [0, 0, 0]]

def solution(beginning, target):
    answer = 0

    col = len(beginning[0])
    row = len(beginning)

    checkCol = 0
    checkRow = 0
    
    # 1열 1행 2열 2행 3열 3행 ... 순으로 계속 비교하면서 뒤집기
    while checkCol < col or checkRow < row:
        # 열 확인
        if checkCol < col:
            for i in range(row):
                if beginning[i][checkCol] != target[i][checkCol]:
                    answer += 1
                    for j in range(col):
                        if beginning[i][j] == 0: beginning[i][j] = 1
                        else: beginning[i][j] = 0
            checkCol += 1

        # 행 확인
        if checkRow < row:
            for i in range(col):
                if beginning[checkRow][i] != target[checkRow][i]:
                    answer += 1
                    for j in range(row):
                        if beginning[j][i] == 0: beginning[j][i] = 1
                        else: beginning[j][i] = 0
            checkRow += 1

    for i in range(row):
        for j in range(col):
            if beginning[i][j] != target[i][j]:
                answer = -1

    return answer

print(solution(beginning, target))

# 답
def flipColumn(arr, col):
    n = len(arr)

    for i in range(n):
        if arr[i][col] == 1:
            arr[i][col] = 0
        else:
            arr[i][col] = 1


def solution(beginning, target):
    answer = float("inf")
    rows = len(beginning)
    cols = len(beginning[0])

    flipped = []
	# 미리 원본 배열을 flip시켜서 저장
    for i in range(rows):
        flipped.append([])
        for j in range(cols):
            if beginning[i][j]:
                flipped[i].append(0)
            else:
                flipped[i].append(1)

    # and시킬 bitmask를 돌면서
    for unit in range(1 << rows):
        rowFlipped = []
        flipCnt = 0
        for i in range(rows):
        	# 000, 010, 100... bitmask 생성
            comp = 1 << i

            # and한 값이 0이 아니면 해당 row 뒤집기
            if unit & comp:
                rowFlipped.append(flipped[i][:])
                flipCnt += 1
            # 해당 row 뒤집지 않기
            else:
                rowFlipped.append(beginning[i][:])
                
        # 열 뒤집기
        for j in range(cols):
            curCol = []
            targetCol = []

            for i in range(rows):
                curCol.append(rowFlipped[i][j])
                targetCol.append(target[i][j])
			
            # 현재 column과 target column이 다르면 뒤집기
            if curCol != targetCol:
                flipColumn(rowFlipped, j)
                flipCnt += 1

		# 결국 뒤집은 결과가 target과 같으면 뒤집은 횟수 갱신
        if rowFlipped == target:
            answer = min(answer, flipCnt)

    if answer == float("inf"):
        answer = -1

    return answer