# 2XXX年，人类通过对火星的大气进行宜居改造分析，使得火星已在理论上具备人类宜居的条件；
# 由于技术原因，无法一次性将火星大气全部改造，只能通过局部处理形式；
# 假设将火星待改造的区域为row *
# column的网格，每个网格有3个值，宜居区、可改造区、死亡区，使用YES、NO、NA代替，YES表示该网格已经完成大气改造，NO表示该网格未进行改造，后期可进行改造，NA表示死亡区，不作为判断是否改造完的宜居，无法穿过；
# 初始化下，该区域可能存在多个宜居区，并目每个宜居区能同时在每个大阳日单位向上下左右四个方向的相邻格子进行扩散，自动将4个方向相邻的真空区改造成宜居区；
# 请计算这个待改造区域的网格中，可改造区是否能全部成宜居区，如果可以，则返回改造的大阳日天教，不可以则返回-1
import sys

# def solution():
anble = []
need = 0
day = 0
queue = []
for item in sys.stdin:
    if not item.strip():
        print("item", item)
        break
    else:
        anble.append(item.split())
for i in range(len(anble)):
    for j in range(len(anble[0])):
        if anble[i][j] == "NO":
            need += 1
        if anble[i][j] == "YES":
            queue.append([i, j])
if not queue:
    print(-1)
if need == len(anble) * len(anble[0]):
    print(0)
offset = [[0, 1], [0, -1], [1, 0], [-1, 0]]
while queue and need > 0:
    new_queue = []
    for q in queue:
        x, y = q
        for off in offset:
            new_x = x + off[0]
            new_y = y + off[1]
            if anble[new_x][new_y] == "NO":
                anble[new_x][new_y] = "YES"
                new_queue.append([new_x, new_y])
                need -= 1
                break
    day += 1
    queue = new_queue
print(day)

# YES YES NO
# NO NO NO
# YES NO NO
