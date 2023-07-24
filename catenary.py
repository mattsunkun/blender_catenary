#!/usr/bin/env python3
## -*- coding: utf-8 -*-

import numpy as np
import bpy


# 既存要素削除
for item in bpy.data.meshes:
    print(item)
    bpy.data.meshes.remove(item)


# x,y座標に応じてz座標を返す関数
def rsq(x, y):
    return np.square(x) + np.square(y)


def calc_z(x, y, a=3):
    z = a * np.cosh(np.sqrt(rsq(x, y)) / a)
    return z


# 分割数
div = 1000
x_len = div
y_len = div

# 範囲
man_radius = 9
x_min = -man_radius
x_max = man_radius
y_min = -man_radius
y_max = man_radius


lattice_x = np.linspace(x_min, x_max, x_len)
lattice_y = np.linspace(y_min, y_max, y_len)

verts = [[x, y, calc_z(x, y)] for y in lattice_y for x in lattice_x]
faces = [
    [x_len * y + x, x_len * y + x + 1, x_len * (y + 1) + x + 1, x_len * (y + 1) + x]
    for y in range(y_len - 1)
    for x in range(x_len - 1)
    if rsq((x - div / 2 + 1), (y - div / 2 + 1)) <= np.square(div / 2)
]

msh = bpy.data.meshes.new("cubemesh")  # Meshデータの宣言
msh.from_pydata(verts, [], faces)  # 頂点座標と各面の頂点の情報でメッシュを作成
cube_obj = bpy.data.objects.new("cube_001", msh)  # メッシュデータでオブジェクトを作成
bpy.context.scene.collection.objects.link(cube_obj)  # シーンにオブジェクトを配置
