from PIL import Image, ImageDraw, ImageFont
def createCertificate(name, id, sign):
    # Open the image
    image = Image.open("templates/temp.jpg")

    # Initialize the drawing context
    draw = ImageDraw.Draw(image)


    # Choose a font and size
    '''
    This part will define the Name characteristics
    '''
    Namefont = ImageFont.truetype("font/static/Alkatra-Regular.ttf", size=40)

    # Choose the position and color for the text
    Name_position = (690, 550)
    # 690, 550 for Soham De
    Name_color = (0, 0, 0)  # White color in RGB format

    # Text to write on the image
    Name = name


    '''
    This part below defines the characteristics of the Unique ID
    '''
    id_position = (342,850)
    UniqueId = id
    idfont = ImageFont.truetype("arial.ttf", size=30)


    '''
    This part below defines the characteristics of the Signature
    '''

    sign_position = (685,810)
    signature = sign
    signfont = ImageFont.truetype("arial.ttf", size=35)


    # Draw the text on the image
    draw.text(Name_position, Name, fill=Name_color, font=Namefont)
    draw.text(id_position, UniqueId, fill=Name_color, font=idfont)
    draw.text(sign_position, signature, fill=Name_color, font=signfont)

    # Save or display the modified image
    image.save(f'certificate/{Name}_{UniqueId}.jpg')
    return image

"""
testing
"""
name = input("Enter name: ")
id = input('Enter your unique Id:')
sign = input("Enter sign: ")
createCertificate(name , id, sign )
print("your certificate has been generated! ")




