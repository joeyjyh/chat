def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		if name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen傳了', allen_word_count,'個字, ', allen_sticker_count, '張貼圖, ', allen_image_count, '張圖片。')
	print('Viki傳了', viki_word_count, '個字, ', viki_sticker_count, '張貼圖, ', viki_image_count, '張圖片。')





def main():
	lines = read_file('line_viki.txt')
	convert(lines)
main()