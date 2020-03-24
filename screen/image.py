from PIL import Image
from PIL import ImageChops


def compare_images(src_img1, src_img2, output_img):
    """
    比较图片，如果有不同则生成展示不同的图片

    @参数一: path_one: 第一张图片的路径
    @参数二: path_two: 第二张图片的路径
    @参数三: diff_save_location: 不同图的保存路径

    """

    image_one_src = src_img1.convert("RGBA")
    image_two_src = src_img2.convert("RGBA")

    size = image_one_src.size

    image_one_src_list = image_one_src.load()
    image_two_src_list = image_two_src.load()

    print(type(image_one_src_list))

    new_image = Image.new("RGBA", size=size, )

    for x in range(size[0]):
        for y in range(size[1]):
            data1 = image_one_src_list[x, y]
            data2 = image_two_src_list[x, y]

            if data1 == data2:
                # 两个像素点相同
                pass
            else:
                # 两个像素点不同
                new_image.putpixel((x, y), data2)
                pass

    image_one_src.close()
    image_two_src.close()
    new_image.save(output_img, "png")


if __name__ == '__main__':
    compare_images('1583551441.1074948.jpg',
                   '1583551443.551184.jpg',
                   '我们不一样.png')