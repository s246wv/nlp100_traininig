/*
03. 円周率Permalink
“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
*/
using System;
using System.Text;

string str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.";
string[] terms = str.Split(' ');
List<int> ret = new List<int>();
foreach(string term in terms){
    ret.Add(term.Length);
}
foreach (var item in ret)
{
    Console.WriteLine(item);
}
