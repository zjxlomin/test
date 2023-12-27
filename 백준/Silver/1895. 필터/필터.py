r, c = map(int, input().split())
image = {}
for x in range(0, r):
    image[x] = list(map(int, input().split()))
filtered_image = []
for i in range(0, r - 2):
    for j in range(0, c - 2):
        pixel = []
        pixel.append(image[i][j])
        pixel.append(image[i][j + 1])
        pixel.append(image[i][j + 2])
        pixel.append(image[i + 1][j])
        pixel.append(image[i + 1][j + 1])
        pixel.append(image[i + 1][j + 2])
        pixel.append(image[i + 2][j])
        pixel.append(image[i + 2][j + 1])
        pixel.append(image[i + 2][j + 2])
        pixel = sorted(pixel)
        filtered_image.append(pixel[4])
l = len(filtered_image)
res = 0
t = int(input())
for k in range(0, l):
    if (filtered_image[k] >= t): res += 1
print(res)