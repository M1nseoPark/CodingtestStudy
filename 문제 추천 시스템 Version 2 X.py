import heapq
import sys

n = int(sys.stdin.readline())
minHeap = []
maxHeap = []
gmin = {}
gmax = {}
level = {}

for _ in range(n):
    p, l, g = map(int, sys.stdin.readline().split())
    heapq.heappush(minHeap, [l, p])
    heapq.heappush(maxHeap, [-l, -p])
    gmin[g] = []
    gmax[g] = []
    heapq.heappush(gmin[g], [l, p])
    heapq.heappush(gmax[g], [-l, -p])
    level[p] = l

m = int(sys.stdin.readline())
for _ in range(m):
    c = sys.stdin.readline().split()

    # add P L G
    if c[0] == 'add':
        heapq.heappush(minHeap, [int(c[2]), int(c[1])])
        heapq.heappush(maxHeap, [-int(c[2]), -int(c[1])])
        if int(c[3]) not in gmin:
            gmin[int(c[3])] = []
            gmax[int(c[3])] = []
        heapq.heappush(gmin[int(c[3])], [int(c[2]), int(c[1])])
        heapq.heappush(gmax[int(c[3])], [-int(c[2]), -int(c[1])])
        level[int(c[1])] = int(c[2])

    # solved P
    if c[0] == 'solved':
        level[int(c[1])] = 0

    # recommend G x
    if c[0] == 'recommend':
        if c[2] == '1':
            while True:
                temp = heapq.heappop(gmax[int(c[1])])
                # 이미 다 푼 문제가 아니라면 
                if level[-temp[1]] != 0:
                    print(-temp[1])
                    heapq.heappush(gmax[int(c[1])], temp)
                    break
                        
        else:
            while True:
                temp = heapq.heappop(gmin[int(c[1])])
                # 이미 다 푼 문제가 아니라면 
                if level[temp[1]] != 0:
                    print(temp[1])
                    heapq.heappush(gmin[int(c[1])], temp)
                    break

    # recommend2 x
    if c[0] == 'recommend2':
        if c[1] == '1':
            while maxHeap:
                temp = heapq.heappop(maxHeap)
                if level[-temp[1]] != 0:
                    print(-temp[1])
                    heapq.heappush(maxHeap, temp)
                    break

        else:
            while minHeap:
                temp = heapq.heappop(minHeap)
                if level[temp[1]] != 0:
                    print(temp[1])
                    heapq.heappush(minHeap, temp)
                    break

    # recommend3 x L
    if c[0] == 'recommend3':
        if c[1] == '1':
            save = []
            flag = False
            while minHeap:
                temp = heapq.heappop(minHeap)
                if level[temp[1]] != 0:
                    if temp[0] >= int(c[2]):
                        print(temp[1])
                        heapq.heappush(minHeap, temp)
                        flag = True
                        break
                    else:
                        save.append(temp)

            if not flag:
                print(-1)

            for i in range(len(save)):
                heapq.heappush(minHeap, save[i])

        else:
            save = []
            flag = False
            while maxHeap:
                temp = heapq.heappop(maxHeap)
                if level[-temp[1]] != 0:
                    if -temp[0] < int(c[2]):
                        print(-temp[1])
                        heapq.heappush(maxHeap, temp)
                        flag = True
                        break
                    else:
                        save.append(temp)

            if not flag:
                print(-1)

            for i in range(len(save)):
                heapq.heappush(maxHeap, save[i])

    #print(minHeap)
    #print(maxHeap)
    #print(level)
    #print('-----')
            
