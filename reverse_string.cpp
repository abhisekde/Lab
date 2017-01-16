#include <iostream>
#include <string.h>

using namespace std;

char* reverse(char* str)
{
	char t;
	int len = strlen(str);
	int i = 0, j = len-1;
	for(; i < j; i++, j--) 
	{
		t = str[i];
		str[i] = str[j];
		str[j] = t;
	}
	return str;
}

int main(int argc, char** argv)
{
	if(argc != 2)
		return 1;
	cout<<reverse(argv[1])<<endl;
	return 0;
}
