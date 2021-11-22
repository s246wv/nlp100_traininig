/*
04. 元素記号Permalink
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
*/
using System;
using System.Text;

string str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.";
string[] terms = str.Split(' ');
int[] nums = new int[] {1, 5, 6, 7, 8, 9, 15, 16, 19};
Dictionary<string, string> ret = new Dictionary<string, string>();
for (int i=0; i<terms.Length; i++){
    StringBuilder temp1 = new StringBuilder();
    if (nums.Contains(i+1)){
        temp1.Append(terms[i][0]);
        string temp2 = temp1.ToString();
        ret.Add(temp2, terms[i]);
    } else{
        temp1.Append(terms[i][0]);
        temp1.Append(terms[i][1]);
        string temp2 = temp1.ToString();
        ret.Add(temp2, terms[i]);
    }
}
foreach (var item in ret){
    Console.WriteLine("{0}: {1}",item.Key, item.Value);
}