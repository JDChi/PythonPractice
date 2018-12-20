import string
import re

#统计数量
def count_words(content):

	dict = {}
	for each in content:
		if each != '':
			dict[each] = dict.get(each , 0) + 1

	return dict

#写入文件
def write_to_file(content):

	with open('count_words_result.txt' , 'w') as f:
		for each in content:
			f.write(each + ":" + '{}'.format(content[each]) + "\n")



def main():
  
	with open('eng_article.txt' , 'r') as f:
		content = f.read()
		#字母全部转为小写
		content = content.replace('\n' , '').lower()

		#将标点符号替换成空格
		for word in content:
			if word in string.punctuation or word.isdigit():
				content = content.replace(word , ' ')


        #通过空格分割出单词
		split_content = content.split(' ')
		#print(split_content)

	result = count_words(split_content)

	write_to_file(result)
	#print(result)




if __name__ == '__main__':
	main()