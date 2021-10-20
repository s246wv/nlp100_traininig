'''
04. 元素記号Permalink
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
'''

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = str.replace(",","")
str = str.replace(".","")
terms = str.split(" ")

keys = []
values = []
for term in terms:
    i = terms.index(term)
    if i == 0 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 14 or i == 15 or i == 18:
        keys.append(term[0])
        values.append(terms.index(term)+1)
    else:
        keys.append(term[0]+term[1])
        values.append(terms.index(term)+1)
dict = {}
dict.update(zip(keys, values))
print(dict)
