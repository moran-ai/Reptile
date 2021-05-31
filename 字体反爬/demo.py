import base64
import io
from fontTools.ttLib import TTFont

# base64后面的字体源码
font_face = ''
# 解码
online_face = TTFont(io.BytesIO(base64.b64decode(font_face)))

# 保存为xml文件
online_face.saveXML('m.xml')
online_face.save('m.ttf')