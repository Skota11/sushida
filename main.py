import webbrowser
import time
import pyocr
import pyocr.builders
from PIL import Image
import pyautogui

def read():
    num = 6
    pyocr.tesseract.TESSERACT_CMD = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    tools = pyocr.get_available_tools()
    tool = tools[0]


    screen_shot = pyautogui.screenshot(region=(570 , 443 , 226 , 22)) 
    screen_shot.save(r"C:\Users\***\Desktop\test.png")

    img = Image.open('test.png')

    #画像を読みやすいように加工。
    img=img.convert('RGB')
    size=img.size
    img2=Image.new('RGB',size)
     
    border=110
     
    for x in range(size[0]):
        for y in range(size[1]):
            r,g,b=img.getpixel((x,y))
            if r > border or g > border or b > border:
                r = 255
                g = 255
                b = 255
            img2.putpixel((x,y),(r,g,b))

    builder = pyocr.builders.TextBuilder(tesseract_layout=num)
    text = tool.image_to_string(img, lang="eng", builder=builder)

    sushi_moji = text.lower() 
    print(sushi_moji)
    pyautogui.write(sushi_moji)


webbrowser.open('http://typingx0.net/sushida/play.html', new=0, autoraise=True)

time.sleep(18)

pyautogui.write('space')

while True:
    read()
    time.sleep(0.18)
