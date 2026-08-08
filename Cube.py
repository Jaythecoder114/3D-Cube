import math
import os
import time

def frange(start, stop, step):
    while start <= stop:
        yield start
        start += step

width = 120
height = 40

A = 0.0
B = 0.0
C = 0.0

cube_size = 12
distance = 60
k1 = 45

while True:
    zbuffer = [0] * (width * height)
    buffer = [" "] * (width * height)

    def draw_surface(cubeX, cubeY, cubeZ, ch):
        global A, B, C

        x = cubeX
        y = cubeY
        z = cubeZ

        x1 = x
        y1 = y * math.cos(A) - z * math.sin(A)
        z1 = y * math.sin(A) + z * math.cos(A)

        x2 = x1 * math.cos(B) + z1 * math.sin(B)
        y2 = y1
        z2 = -x1 * math.sin(B) + z1 * math.cos(B)

        x3 = x2 * math.cos(C) - y2 * math.sin(C)
        y3 = x2 * math.sin(C) + y2 * math.cos(C)
        z3 = z2 + distance

        ooz = 1 / z3

        xp = int(width / 2 + k1 * ooz * x3)
        yp = int(height / 2 - k1 * ooz * y3)

        if 0 <= xp < width and 0 <= yp < height:
            idx = xp + yp * width
            if ooz > zbuffer[idx]:
                zbuffer[idx] = ooz
                buffer[idx] = ch

    step = 0.6

    for x in frange(-cube_size, cube_size, step):
        for y in frange(-cube_size, cube_size, step):
            draw_surface(x, y, -cube_size, "#")
            draw_surface(cube_size, y, x, "@")
            draw_surface(-cube_size, y, -x, "$")
            draw_surface(-x, y, cube_size, "%")
            draw_surface(x, -cube_size, -y, "&")
            draw_surface(x, cube_size, y, "*")

    os.system("clear")  # Unter Windows stattdessen "cls"

    for y in range(height):
        print("".join(buffer[y * width:(y + 1) * width]))

    A += 0.03
    B += 0.02
    C += 0.015

    time.sleep(1 / 60)
