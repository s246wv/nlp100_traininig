'''
03. 円周率Permalink
“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
'''

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

# コンマとピリオドの除去
str = str.replace(",", "")
str = str.replace(".", "")
# 単語に分ける
terms = str.split(" ")

ret = []
for term in terms:
    ret.append(len(term))

print(ret)
