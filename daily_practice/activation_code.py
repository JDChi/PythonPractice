import random


#激活码的生成
#这里撇去一些字母和数字，比如 i 和 l ， 0 和 O 可能发生混淆
def genCode(size , count):
	chars = ['a' , 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'j' , 'k' , 'm' , 'n' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y']
	nums = ['1', '3' , '4' , '5' , '6' , '7' , '8' , '9']
	init = chars + nums

	s = set([])

	if(len(s) != count):
		for each in range(count):
			code = random.choices(init , k=size)
			code_convert = ''.join(code)
			s.add(code_convert)

	
	return s

def write_to_file(codes):

	with open('activation_code.txt' , 'w') as f:
		for each in codes:
			f.write(each + "\n")

def main():
	
	code = genCode(8 , 200)
	write_to_file(code)
	

	
if __name__ == '__main__' :
	main()
