from PIL import Image
import ast


def readRGBfile(file_path):
	with open(file_path, 'r') as file:
		file_content = file.read().strip()
		tuples = ast.literal_eval(file_content)
		result = [list(tpl) for tpl in tuples]
	return result


def printImage(RGBArr):
	## print image
	width = 536
	height = 70
	blank_image = Image.new("RGB", (width, height))
	pixelNum = 0
	for x in range(width):
		for y in range(height):
			colors = RGBArr[pixelNum]
			blank_image.putpixel((x, y), (int(colors[0] * 255), int(colors[1] * 255), int(colors[2] * 255), 255))
			pixelNum += 1
	blank_image.show()
	return


def main():
	width = 365
	height = 70
	filename = "rgbs.txt"
	parsedRgbs = readRGBfile(filename)
	print(parsedRgbs)
	printImage(parsedRgbs)
	return


if __name__ == "__main__":
    main()