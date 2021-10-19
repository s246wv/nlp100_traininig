'''
05. n-gramPermalink
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
'''

def ngram(str,n,att):
    ret = []
    if att == "word":
        
    elif att == "char":
        for s in str:
            if str.index(s) != len(str)-1:
                ret.append(s+)
    else:
        print("Please provide the third variable as \"word\" or \"char\".")

str = "I am an NLPer"
