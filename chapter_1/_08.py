'''
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''

def cipher(input):
    if type(input) != str:
        print("please input string.")
    else:
        out = []
        for i in input:
            if i.isalpha() and i.islower():
                o = chr(219-ord(i))
                out.append(o)
            else:
                out.append(i)
    return "".join(out)
def main():
    message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. ウェブページのレイアウトの例。"
    print(cipher(message))

if __name__ == "__main__":
    main()