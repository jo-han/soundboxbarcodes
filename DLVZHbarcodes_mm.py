# Dieren Laten Van Zich Horen barcodes generator
# barcodes consist of double-width bars with single-width whitespace (= 1) and
# single-width bars with double-width whitespace (= 0)
# barcodes encode the id through a 10-position binary representation followed by 2 check bits and a 1
# check bits are 01 if the number of bits is even and 10 if odd.
# ids and names are sourced from:
# https://static.ah.nl/binaries/ah/content/assets/ah-nl/core/campagnes/2024/dierenkaarten/dierenkaartjes-2024.pdf

def DLVZHbitcode(id):
	# bitcode starts with a 10-position binary representation of id
	bitcode = format(id, '010b')
	# add check bits and final 1
	countones = 10-len(bitcode.replace('1', ''))
	if (countones%2==0):
		bitcode += '011'
	else:
		bitcode += '101'

	bitcode_array = [int(bit) for bit in bitcode]
	return bitcode_array

def createSimpleBarcodeSvg(bitdata, bitwidth, barheight):
	# Start the SVG string
	svg_string = f'<svg width="{bitwidth * len(bitdata)}mm" height="{barheight}mm" xmlns="http://www.w3.org/2000/svg">'

	# Draw the black bars
	x = 0
	for bit in bitdata:
		if bit == 0:
			svg_string += f'\n<rect x="{x}mm" y="0" width="{bitwidth*1/3}mm" height="{barheight}mm" fill="black"/>'
		elif bit == 1:
			svg_string += f'\n<rect x="{x}mm" y="0" width="{bitwidth*2/3}mm" height="{barheight}mm" fill="black"/>'
		x += bitwidth

	# End the SVG string
	svg_string += '\n</svg>'

	return svg_string

def generateAllBarcodes(lastid=96, firstid=1):
	for i in range(firstid, lastid+1):
		bitcode_array = DLVZHbitcode(i)
		svgtext = createSimpleBarcodeSvg(bitcode_array, 4.5, 11.5)
		with open(f"svg/barcode{i:02}.svg", "w") as file:
			file.write(svgtext)

generateAllBarcodes()