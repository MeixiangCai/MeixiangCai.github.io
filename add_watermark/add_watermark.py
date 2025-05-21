from PIL import Image,ImageFont,ImageDraw
img = Image.open("/Users/xiaoxiao/Desktop/all_python_projects/add_watermark/WechatIMG621.jpg")

font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Songti.ttc",size=42)
draw = ImageDraw.Draw(img)
draw.text(xy=(10,10),text="@Manggahan 2025",font=font,fill="Yellow")
img.save("/Users/xiaoxiao/Desktop/all_python_projects/add_watermark/result.JPG")
