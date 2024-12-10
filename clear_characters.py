import sys
import os

#array to check for removable characters
removables = ['#', '"', '/', '`', '=', '*', '!', '-', '|', '.']

#function that removes the hashtag
def changeHashtag(string):
	#removes three hashtags if present
	if '###' in string:
		string = string.replace('###', '')
	#removes only two if else
	elif '##' in string:
		string = string.replace('##', '')
	#performs these actions if otherwise
	else:
		if 'SBATCH' in string:
			pass
		elif '!#' in string:
			pass
		elif '/#' in string:
			pass 
		else:
			string = string.replace('#', '')
	return string

#function that removes slashes that repeat more than twice
def removeSlashes(string):
	if '//////' in string:
		text = string.replace('//////', '')
	elif '/////' in string:
		text = string.replace('/////', '')
	elif '////' in string:
		text = string.replace('////', '')
	elif '///' in string:
		text = string.replace('///', '')
	else:
		text = string
	return text

#function that removes slanted single quotes
def removeSingleQuotes(string):
	text = string.replace('`', '')
	return text

#function that removes equals sign 
def removeEquals(string):
	if 'class' in string:
		return string
	else:
		text = string.replace('=', '')
	return text

#function that removes star character
def removeStar(string):
	text = string.replace('*', '')
	return text

#function that removes excessive exclamation points
def reclaimExclaim(string):
	if '!---' in string:
		text = string.replace('!---', '')
	else:
		text = string.replace('!', '')
	return text

#removes extra dashlines
def extraDashlines(string):
	if '---' in string:
		text = string.replace('---', '')
	elif '--' in string:
		text = string.replace('--', '')
	else:
		text = string
	return text 

#removes vertical dashlines
def removeVline(string):
	text = string.replace('|', '')
	return text

#removes ...
def threeDots(string):
	if '...' in string:
		text = string.replace('...', '')
	else:
		text = string
	return text

#function that cleans string of extra characters
def clearString(string):
	#initalizes an iterator
	i = 0
	#loops until end of string
	while i < len(string):
		#assigns c to current character in string
		c = string[i]
		#checks if c is equal to element
		if c == removables[0]:
			#checks if i -1 is larger than 0
			if i - 1 > 0:
				#passes if character is a forwardslash
				if string[i-1] == '/':
					pass
				#calls changeHashtag if otherwise
				else:
					string = changeHashtag(string)
			#checks if i + 1 less than the string length if else
			elif i + 1 < len(string):
				#passes if conditions are met
				if string[i+1] == '!' or string[i+1] == 'S':
					pass
				#calls changeHashtag if otherwise
				else:
					string = changeHashtag(string)
		#removes doublequotes if present
		elif c == removables[1]:
			string = string.replace('"', '')
		#checks if c is equal to element
		elif c == removables[2]:
			#checks if i + 1 is less than string length
			if i + 1 < len(string):
				#executes code if conditions are met
				if string[i+1] == '/':
					string = removeSlashes(string)
				#passes otherwise
				else:
					pass
		#calls removeSingleQuotes
		elif c == removables[3]:
			string = removeSingleQuotes(string)
		#calls removeEquals
		elif c == removables[4]:
			string = removeEquals(string)
		#calls removeStar
		elif c == removables[5]:
			string = removeStar(string)
		#calls reclaimExclaim
		elif c == removables[6]:
			string = reclaimExclaim(string)
		#calls extraDashlines
		elif c == removables[7]:
			string = extraDashlines(string)
		#calls removeVline
		elif c == removables[8]:
			string = removeVline(string)
		#calls threeDots
		elif c == removables[9]:
			string = threeDots(string)
		#increments i by one
		i += 1
	#returns string value
	return string

#main function
def main():
	#iterator variable to count lines
	iterated = 0
	#sets empty list
	arr = []
	#assigns filename with command line argument
	filename = sys.argv[1]
	#opens file
	file = open(filename, 'r')
	#loops through file
	for n in file:
		#calls clearString
		text = clearString(n)
		#appends text to arr
		arr.append(text)

	#closes file
	file.close()

	#opens a new file called check_test.txt to write in
	with open('check_test.txt', 'w') as fit:
		#loops through list
		for n in arr:
			#writes element in list to file
			fit.write(n)

#calls main function
if __name__ == "__main__":
	main()
