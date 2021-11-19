import sys
# import create
import itertools

CNF = []

def clean(fileName):
	result = []
	#remove spaces and explode on ";"
	rawRulse = fileName.replace('\n','').split(';')
	
	for rule in rawRulse:
		#Explode evry rule on "->" and make a couple
		leftSide = rule.split(' -> ')[0].replace(' ','')
		rightTerms = rule.split(' -> ')[1].split(' | ')
		for term in rightTerms:
			result.append( (leftSide, term.split(' ')) )
	return result

if __name__ == '__main__':
    fileName = 'grammar/cfg.txt'
    file = open(fileName).read()
    CFG = clean(file)
    print(CNF)
