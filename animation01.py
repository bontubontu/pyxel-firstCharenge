import pyxel

Width = 128
Height = 128
IMG_NO = 1

pyxel.init(Width,Height,fps=10)
pyxel.load('mychara.pyxres')

ani_no = 0
ani_max = 8

while True:
    pyxel.cls(1)
    ani_no = (ani_no + 1) % ani_max
    pyxel.blt(
        Width / 2, Height/2,
        IMG_NO,
        0 + (ani_no * 16),0,16,16)
    pyxel.flip()