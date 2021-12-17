#include <cstdio>
#include <map>
#include <string>

using namespace std;
int main()
{
    map<string,string>m;
    char line[100000];
    while(gets(line)){
	if (line[0]=='\0') break;
	char a[50],b[50];
	sscanf(line,"%s %s",a,b);
	m[b]=a;
    }
    while(gets(line)){
	if (line[0]=='\0') break;
	if (m[line]=="\0") //map如果沒對應到，其內容為"\0"
	    printf("eh\n");
	else
       	     printf("%s\n",m[line].c_str()); //把C++字串換回C字串
    }
	return 0;
}