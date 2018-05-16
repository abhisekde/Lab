#include <iostream>
#include <string.h>
#include <malloc.h>

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

char* format_space(char* str, const int length)
{
	int j = 0;
	char* output = (char*) malloc(sizeof(char)* 1000);
	for(int i = 0; i < length; i++, j++)
	{
		if(str[i] == ' ') 
		{
			output[j] = '0';
			output[++j] = '2';
			output[++j] = '%';
		}
		else
			output[j] = str[i];
	}
	output[j] = '\0';
	return output;
}
char* format_url(char* str, const int length)
{
	return 	reverse(format_space(reverse(str), length));	
}

int main(int argc, char** argv)
{
	if(argc != 2)
		return 1;
	cout<<format_url(argv[1], strlen(argv[1]))<<endl;
	return 0;
}

/*added comments only*/
