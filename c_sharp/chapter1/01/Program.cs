/*
01. 「パタトクカシーー」Permalink
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
*/
using System;
using System.Text;

string str = "パタトクカシーー";
// string ret = str[0] + str[2] + str[4]+ str[6];
StringBuilder sb = new StringBuilder();
for (int i=0;i<7;i++){
    if(i==0){
        sb.Append(str[i]);
    } else if(i%2==0){
        sb.Append(str[i]);
    } else{
        //NOP
    }
}
string ret = sb.ToString();
Console.WriteLine(ret);