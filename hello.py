import pyxel
WIDSTH = 256
HEIGHT = 256
pyxel.init(WIDSTH,HEIGHT) #画面の縦横のドット数を設定
pyxel.cls(1) #色番号を入力 0~15
pyxel.text(0,2,"Hello",8) #(文字の表示位置X,文字の表示位置Y,"表示したい文字列",文字色)
pyxel.show() #ゲームウィンドウを表示状態にする