/*
02. 「パトカー」＋「タクシー」＝「パタトクカシーー」Permalink
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
*/
using System;
using System.Text;

string str1 = "パトカー";
string str2 = "タクシー";
StringBuilder sb = new StringBuilder();
for(int i=0; i<str1.Length; i++){
    sb.Append(str1[i]);
    sb.Append(str2[i]);
}
string ret = sb.ToString();

Console.WriteLine(ret);