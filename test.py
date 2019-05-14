def test_letters(test_list):
    for i in test_list:
        im = Image.open(i)
        im.load()
        background = Image.new("RGB", im.size, (255, 255, 255))
        background.paste(im, mask=im.split()[3])  # 3 is the alpha channel
        image = background.convert('L')  # convert image to monochrome
        image = np.array(image)
        image = binarize_array(image)
        letter, dist = test_image(image, med)
        print(i + " = " + chr(int(letter)))
# iom = med[1040.0]
# ima = []
# line = []
# k = 0
# for i in iom:
#     if i == 1:
#         line.append([0,0,0])
#     else:
#         line.append([255,255,255])
#     k += 1
#     if k % 28 == 0:
#         ima.append(line)
#         line = []
#
# iom = smp.toimage(ima)
# iom.resize((200,200), Image.ANTIALIAS)
# iom.show()