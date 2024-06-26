import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import random

ttfontname = "C:\\Windows\\Fonts\\meiryob.ttc"
fontsize = 36
hiragana = "あいうえおぁぃぅぇぉかきくけこがぎぐげごさしすせそざじずぜぞたちつてとだぢづでどなにぬねのはひふへほばびぶべぼぱぴぷぺぽまみむめもやゆよらりるれろわをんっゃゅょゎ"
text = ""
text = text + random.choice(hiragana)
text = text + random.choice(hiragana)
text = text + random.choice(hiragana)
text = text + random.choice(hiragana)

# 画像サイズ，背景色，フォントの色を設定
canvasSize    = (300, 150)
backgroundRGB = (255, 255, 255)
textRGB       = (0, 0, 0)

# 文字を描く画像の作成
img  = PIL.Image.new('RGB', canvasSize, backgroundRGB)
draw = PIL.ImageDraw.Draw(img)

# 用意した画像に文字列を描く
font = PIL.ImageFont.truetype(ttfontname, fontsize)
textWidth, textHeight = draw.textsize(text,font=font)
textTopLeft = (canvasSize[0]//4, canvasSize[1]//2-textHeight//2) # 前から1/6，上下中央に配置
draw.text(textTopLeft, text, fill=textRGB, font=font)

img.save("image.png")
