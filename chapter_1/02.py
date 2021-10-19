'''
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」Permalink
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
'''
str1 = "パトカー"
str2 = "タクシー"

tmp = []
for i,j in zip(str1, str2):
    tmp.append(i+j)

ret = "".join(tmp)
print(ret)