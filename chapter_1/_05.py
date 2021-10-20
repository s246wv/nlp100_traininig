'''
05. n-gramPermalink
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
'''

def ngram(str,n,att):
    ret = []
    if att == "word":
        wind = 0
        # 単語は数字で区切られているという勝手な前提。
        words = str.split(" ")
        for word in words:
            if wind != len(words)-(n-1):
                gram = ""
                for i in range(0,n):
                    gram += words[wind+i]
                    if i != n-1:
                        gram += " "
                ret.append(gram)
                wind += 1
    elif att == "char":
        sind = 0
        for s in str:
            if sind != len(str)-(n-1):
                gram = ""
                for i in range(0,n):
                    gram += str[sind+i]
                ret.append(gram)
                sind += 1
    else:
        print("Please provide the third variable as \"word\" or \"char\".")

    return ret

str = "I am an NLPer"
# print(ngram(str,2,"word"))
print(ngram(str,2,"char"))