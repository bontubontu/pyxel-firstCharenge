import pyxel
Width = 256
Height = 256
IMG_NO = 0
pyxel.init(Width,Height)
pyxel.load('mychara.pyxres') #作成したイメージデータを読み込む
pyxel.cls(1)
#ゲーム画面に画像を配置する
#キャラの左上のX座標,キャラの左上のY座標,イメージ番号,指定したイメージ番号の切り出しX座標開始位置,指定したイメージ番号の切り出しY座標開始位置,切り出すイメージの幅,切り出すイメージの高さ,透明にする色
pyxel.blt(Width/2,Height/2,IMG_NO,0,0,16,16,0)
pyxel.show()