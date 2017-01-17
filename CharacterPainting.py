#coding = utf-8
######################################
#	Author			:	kalbertlee
#	Time			:	2017-01-16
#	chrset height	:	5
######################################
chrset = {
'a':"     \n     \n ___ \n| . |\n|_|_|",
'b':" _   \n| |  \n| |_ \n| . |\n|___|",
'c':"     \n     \n ___ \n| ._|\n|___|",
'd':"   _ \n  | |\n _| |\n| . |\n|___|",
'e':"     \n     \n ___ \n| ._|\n|__\ ",
'f':"   ___ \n _/ /_ \n|_   _|\n  | |  \n  |_|  ",
'g':"     \n ___ \n| . |\n|__ |\n /__|",
'h':" _   \n| |  \n| |_ \n|   |\n|_|_|",
'i':"   \n _ \n|_|\n| |\n|_|",
'j':"  _ \n |_|\n | |\n_| |\n\__|",
'k':" _    \n| | __\n| |/ /\n|   < \n|_|\_\\",
'l':" _  \n| | \n| | \n| | \n|__|",
'm':"       \n       \n _____ \n|     |\n|_|_|_|",
'n':"     \n     \n ___ \n|   |\n|_|_|",
'o':"     \n     \n ___ \n| . |\n|___|",
'p':"     \n ___ \n| . |\n|  _|\n|_|  ",
'q':"     \n ___ \n| . |\n|_  |\n  |_|",
'r':"     \n     \n _ _ \n| / /\n|__/ ",
's':"     \n     \n ___ \n|_ -|\n|___|",
't':"     \n  _  \n_| |_\n | |_\n |__/",
'u':"     \n     \n _ _ \n| | |\n|___|",
'v':"     \n     \n _ _ \n\ | /\n \_/ ",
'w':"       \n       \n _ _ _ \n| | | |\n \___/ ",
'x':"    \n    \n _  \n\ \/\n/\_\\",
'y':"     \n _   \n\ \//\n \ / \n //  ",
'z':"      \n      \n_____ \n\_  / \n /___\\",
'0':"     \n ___ \n|   |\n| | |\n|___|",
'1':"     \n __  \n|_ | \n | | \n|___|",
'8':"     \n ___ \n|   |\n|===|\n|___|",
' ':" \n \n \n \n ",
'_':" \n \n \n \n_",
':':" \n \n.\n.\n ",
'"':" \n\"\n \n \n "
}


def chrcat(s1,s2):
	st1 = s1.split('\n')
	st2 = s2.split('\n')
	return st1[0]+st2[0]+'\n'+st1[1]+st2[1]+'\n'+st1[2]+st2[2]+'\n'+st1[3]+st2[3]+'\n'+st1[4]+st2[4]


def chrcatx(s1,s2):
	st1 = s1.split('\n')
	st2 = s2.split('\n')
	inv = []
	if st1[0][-1] == ' ' and st1[1][-1] == ' ' and st1[2][-1] == ' ' and st1[3][-1] == ' ' and st1[4][-1] == ' ':
		return st1[0]+st2[0]+'\n'+st1[1]+st2[1]+'\n'+st1[2]+st2[2]+'\n'+st1[3]+st2[3]+'\n'+st1[4]+st2[4]
	if st2[0][0] == ' ' and st2[1][0] == ' ' and st2[2][0] == ' ' and st2[3][0] == ' ' and st2[4][0] == ' ':
		return st1[0]+st2[0]+'\n'+st1[1]+st2[1]+'\n'+st1[2]+st2[2]+'\n'+st1[3]+st2[3]+'\n'+st1[4]+st2[4]
	for i in range(5):
		if st1[i][-1] =='|' and st2[i][0] == '|' or st1[i][-1] =='|' and st2[i][0] == ' ' or st1[i][-1] ==' ' and st2[i][0] == '|':
			inv += ['|']
		elif st1[i][-1] ==' ' and st2[i][0] == ' ':
			inv += [' ']
		else:
			return st1[0]+st2[0]+'\n'+st1[1]+st2[1]+'\n'+st1[2]+st2[2]+'\n'+st1[3]+st2[3]+'\n'+st1[4]+st2[4]
		
	for i in range(5):
		st1[i] = st1[i][:-1]
		st2[i] = inv[i]+st2[i][1:]
	return st1[0]+st2[0]+'\n'+st1[1]+st2[1]+'\n'+st1[2]+st2[2]+'\n'+st1[3]+st2[3]+'\n'+st1[4]+st2[4]
		
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
	print chrpic("abcde:fghij \"klmn\" opqrstuvwxyz")
