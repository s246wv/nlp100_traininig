/*
00. 文字列の逆順Permalink
文字列”stressed”の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
*/
string str = "stressed";
char[] ret = new char[str.Length];
for(int i=0;i<str.Length;i++){
    ret[str.Length-i-1]=str[i];
}
Console.WriteLine(ret);


