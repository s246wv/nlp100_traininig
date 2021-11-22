/*
05. n-gramPermalink
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
*/
using System;
using System.Text;

class Sample{
    public List<string> Ngram(string str, int n, int mode){
        List<string> ret = new List<string>();
        if (mode == 0){ // 単語bi-gram
            string[] terms = str.Split(' ');
            if (terms.Length > n){
                for (int i=0; i<terms.Length-n+1; i++){
                    string temp = "";
                    for (int j=0; j<n; j++){
                        temp += terms[i+j];
                        temp += " ";
                    }
                    ret.Add(temp);
                }
            } else{
                Console.WriteLine("The number \"n\" is invalid.");
            }
        } else if (mode == 1){ // 文字bi-gram
            if (str.Length > n){
                for (int i=0; i<str.Length-n+1; i++){
                    List<char> temp = new List<char>();
                    for (int j=0; j<n; j++){
                        temp.Add(str[i+j]);
                    }
                    string temp2 = new string(temp.ToArray());
                    ret.Add(temp2);
                }
            }
        } else{
            /*NOP*/
        }
        return ret;
    }

    static void Main(string[] args){
        string str = "I am an NLPer";
        Sample sample = new Sample();
        var ret = sample.Ngram(str, 3, 0);
//        Console.WriteLine(ret.Count);
        foreach (var item in ret) {
            Console.WriteLine(item);
        }
    }
}