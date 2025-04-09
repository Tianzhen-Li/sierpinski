'''
def sierpinski(tetras):
    process...
    tetras += 3 other tetras
    return tetras
for i in range(0, level):
    tetras = siepinski()


0, 01, 02, 03
1, 10, 12, 13
2, 20, 21, 23
3, 30, 31, 32

'''
level = 7
Tetras = [[[1, 1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1]]]
def midpoint(point_1, point_2):
    mid = [(p1 + p2)/2 for p1, p2 in zip(point_1, point_2)]
    return mid

def sierpinski(tetras):
    smaller_tetras = []
    for tetra in tetras:
        for i in range(0, 4):
            smaller_tetra = [tetra[i]]
            for j in range(0, 4):
                if i != j:
                    print(i, j)
                    smaller_tetra += [midpoint(tetra[i], tetra[j])]
            smaller_tetras += [smaller_tetra]
    return smaller_tetras
new_tetras = Tetras
for i in range(0, level):
    new_tetras = sierpinski(new_tetras)
    Tetras += new_tetras



def tetras_to_obj(tetras, file_name):
#generate vertices and faces
    vertices=[]
    faces = []
    i=1
    for tetra in tetras:
        vertices += tetra
        faces += [[i, i+1, i+2]]
        faces += [[i, i+1, i+3]]
        faces += [[i, i+2, i+3]]
        faces += [[i+1, i+2, i+3]]
        i +=4

    lines =['\n']
    for v in vertices:
        lines += ['v %lf %lf %lf\n' % (v[0], v[1], v[2])]

    for f in faces:
        lines += ['f %d %d %d\n' % (f[0],f[1],f[2])]

    with open(file_name, "w") as file:
        file.writelines(lines)


tetras_to_obj(new_tetras, 'test01.obj')

# for tetra in Tetras:
#     print(tetra)
