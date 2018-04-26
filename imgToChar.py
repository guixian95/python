from PIL import Image;
import argparse; #python 命令行解析模块
ascii_char = '''@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.'''
parser=argparse.ArgumentParser()
parser.add_argument('file')#输入的文件
parser.add_argument('-o','--output')#输出文件
parser.add_argument('--width',type=int,default=80)#输出字符串宽度
parser.add_argument('--height',type=int,default=80)#输出字符串高度
args=parser.parse_args()
img=args.file
width=args.width
height=args.height
output=args.output
def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126*r+0.7152*g+0.0722*b) #将颜色转为灰度值 [0,255]
    return ascii_char[int(gray/alpha*length)]#将灰度值转为字符
if __name__ == '__main__':
    im = Image.open(img)
    im = im.resize((width, height), Image.NEAREST)
    txt = ""
    for i in range(height):
        for j in range(width):
            args = im.getpixel((j,i))
            txt += get_char(*(args))
        txt += '\n'
    print(txt)
    output = output if output else 'output.txt'
    with open(output, 'w') as f:
        f.write(txt)
