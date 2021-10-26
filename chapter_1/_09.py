'''
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．
'''
import random

def main():
    str = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    words = str.split(" ")
    out = []
    for word in words:
        lastNum = len(word)
        if lastNum <= 4:
            out.append(word + " ")
        else:
            o = ""
            mid = random.sample(word[1:-1],len(word[1:-1]))
            for ind in range(lastNum):
                if ind == 0:
                    o += word[ind]
                elif ind == lastNum-1:
                    o += word[lastNum-1]
                else:
                    o += mid[ind-1]
            out.append(o + " ")
    outStr = "".join(out)
    print(outStr.rstrip())


if __name__ == "__main__":
    main()