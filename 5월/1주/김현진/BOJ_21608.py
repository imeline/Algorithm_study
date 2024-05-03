N = int(input())
students = [ list(map(int,input().split())) for _ in range(N*N)]
gyu = [[0 for _ in range(N)] for _ in range(N)]

student_pre = dict()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def favorite_empty_student(i,j,student):
    f_cnt=0
    e_cnt=0
    for k in range(4):
        di = i + dx[k]
        dj = j + dy[k]
        if 0<=di<N and 0<=dj<N:
            # print(gyu[di][dj], student, " 여기 여기 ")
            # print(arr)
            if gyu[di][dj] in student: #범위값, 좋아하는 애 있다
                f_cnt +=1
            if gyu[di][dj] == 0:
                e_cnt +=1
    return [f_cnt,e_cnt]

def liked(gyu):
    sum = 0
    for i in range(N):
        for j in range(N):
            cnt = 0
            for k in range(4):
                di = i + dx[k]
                dj = j + dy[k]
                if 0<=di<N and 0<=dj<N:
                    if gyu[di][dj] in student_pre[ gyu[i][j] ] :
                        cnt+=1
            if cnt >= 1:
                sum += 10**(cnt-1)

    return sum

# [좋아하는 학생 인접 많, 비어있는 칸 많, 헹 낮, 열 낮,]
for student in students:
    me = student[0]
    favor = student[1:]
    student_pre[me]=favor
    arr = []
    for i in range(N):
        for j in range(N):
            if gyu[i][j] == 0:
                favorite,empty = favorite_empty_student(i,j,student)
                arr.append([favorite,empty,i,j])

    # arr.sort(key = lambda x : x[3])
    arr.sort(key = lambda x : (x[2],x[3]))
    arr.sort(key = lambda x : (x[0],x[1]) , reverse= True)
    # arr.sort(key = lambda x : x[0],key=reversed)
    # print(arr)
    x,y = arr[0][2:]
    # print(x,y)
    gyu[x][y] = me

print(liked(gyu))


















