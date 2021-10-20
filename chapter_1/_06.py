'''
06. 集合Permalink
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''

#import _05
from _05 import ngram

strX = "paraparaparadise"
strY = "paragraph"

X = ngram(strX,2,"char")
Y = ngram(strY,2,"char")

#print(X)
#print(Y)
#print(X and Y)
