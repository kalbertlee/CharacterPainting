#coding = utf-8
######################################
#	Author			:	kalbertlee
#	Time			:	2017-01-16
#	chrset height	:	6
######################################
chrset = {
'a':"     \n     \n ___ \n| . |\n|_|_|\n     ",
'b':" _   \n| |  \n| |_ \n| . |\n|___|\n     ",
'c':"     \n     \n ___ \n| ._|\n|___|\n     ",
'd':"   _ \n  | |\n _| |\n| . |\n|___|\n     ",
'e':"     \n     \n ___ \n| ._|\n|__\ \n     ",
'f':"   ___ \n _/ /_ \n|_   _|\n  | |  \n  |_|  \n       ",
'g':"     \n     \n ___ \n| . |\n|__ |\n /__|",
'h':" _   \n| |  \n| |_ \n|   |\n|_|_|\n     ",
'i':"   \n _ \n|_|\n| |\n|_|\n   ",
'j':"    \n  _ \n |_|\n | |\n_| |\n\__|",
'k':" _    \n| | __\n| |/ /\n|   < \n|_|\_\\\n      ",
'l':" _  \n| | \n| | \n| | \n|__|\n    ",
'm':"       \n       \n _____ \n|     |\n|_|_|_|\n       ",
'n':"     \n     \n ___ \n|   |\n|_|_|\n     ",
'o':"     \n     \n ___ \n| . |\n|___|\n     ",
'p':"     \n     \n ___ \n| . |\n|  _|\n|_|  ",
'q':"     \n     \n ___ \n| . |\n|_  |\n  |_|",
'r':"     \n     \n _ _ \n| / /\n|__/ \n     ",
's':"     \n     \n ___ \n|_ -|\n|___|\n     ",
't':"     \n  _  \n_| |_\n | |_\n |__/\n     ",
'u':"     \n     \n _ _ \n| | |\n|___|\n     ",
'v':"     \n     \n _ _ \n\ | /\n \_/ \n     ",
'w':"       \n       \n _ _ _ \n| | | |\n \___/ \n       ",
'x':"    \n    \n _  \n\ \/\n/\_\\\n    ",
'y':"     \n     \n _   \n\ \//\n \ / \n //  ",
'z':"      \n      \n_____ \n\_  / \n /___\\\n      ",
'0':" ____ \n|    |\n| || |\n| || |\n|____|\n      ",
'1':" __   \n|_ |  \n  ||  \n _||_ \n|____|\n      ",
'2':" ____ \n|_   |\n _| _|\n|  |_ \n|____|\n      ",
'3':" ____ \n|__  |\n __| |\n __| |\n|____|\n      ",
'4':"  _ _ \n / / |\n/ /| |\n|__  |\n   |_|\n      ",
'5':" ____ \n|   _|\n|_ |_ \n _|  |\n|____|\n      ",
'6':"    _ \n  / / \n / /_ \n| () |\n|____|\n      ",
'7':" ____ \n|__  |\n  / / \n / /  \n/_/   \n      ",
'8':" ____ \n|    |\n| () |\n| () |\n|____|\n      ",
'9':" ____ \n|    |\n|_() |\n  / / \n /_/  \n      ",
' ':" \n \n \n \n \n ",
'_':" \n \n \n \n \n_",
'-':" \n \n \n-\n \n ",
':':" \n \n.\n.\n \n ",
'"':" \n\"\n \n \n \n "
}


def chrcat(s1,s2):
	st1 = s1.split('\n')
	st2 = s2.split('\n')
	return st1[0]+st2[0]+'\n'+st1[1]+st2[1]+'\n'+st1[2]+st2[2]+'\n'+st1[3]+st2[3]+'\n'+st1[4]+st2[4]+'\n'+st1[5]+st2[5]


def chrcatx(s1,s2):
	st1 = s1.split('\n')
	st2 = s2.split('\n')
	inv = []
	if st1[0][-1] == ' ' and st1[1][-1] == ' ' and st1[2][-1] == ' ' and st1[3][-1] == ' ' and st1[4][-1] == ' ':
		return st1[0]+st2[0]+'\n'+st1[1]+st2[1]+'\n'+st1[2]+st2[2]+'\n'+st1[3]+st2[3]+'\n'+st1[4]+st2[4]+'\n'+st1[5]+st2[5]
	if st2[0][0] == ' ' and st2[1][0] == ' ' and st2[2][0] == ' ' and st2[3][0] == ' ' and st2[4][0] == ' ':
		return st1[0]+st2[0]+'\n'+st1[1]+st2[1]+'\n'+st1[2]+st2[2]+'\n'+st1[3]+st2[3]+'\n'+st1[4]+st2[4]+'\n'+st1[5]+st2[5]
	for i in range(6):
		if st1[i][-1] =='|' and st2[i][0] == '|' or st1[i][-1] =='|' and st2[i][0] == ' ' or st1[i][-1] ==' ' and st2[i][0] == '|':
			inv += ['|']
		elif st1[i][-1] ==' ' and st2[i][0] == ' ':
			inv += [' ']
		else:
			return st1[0]+st2[0]+'\n'+st1[1]+st2[1]+'\n'+st1[2]+st2[2]+'\n'+st1[3]+st2[3]+'\n'+st1[4]+st2[4]+'\n'+st1[5]+st2[5]
		
	for i in range(6):
		st1[i] = st1[i][:-1]
		st2[i] = inv[i]+st2[i][1:]
	return st1[0]+st2[0]+'\n'+st1[1]+st2[1]+'\n'+st1[2]+st2[2]+'\n'+st1[3]+st2[3]+'\n'+st1[4]+st2[4]+'\n'+st1[5]+st2[5]
		
def chrpic(s):
	pic = ""
	if s == "":
		return pic
	if len(s) == 1:
		try:
			pic = chrset[s]
		except KeyError:
			print "'"+s+"' not found in chrset"
			return pic 
	pic = chrset[s[0]]
	for i in range(1,len(s)):
		try:
			pic = chrcatx(pic,chrset[s[i]])
		except KeyError:
			print "'"+s[i]+"' not found in chrset"
			return pic 
	return pic 

if __name__ == '__main__':
	print chrpic("sqlmap from:\"0123456789\"")
