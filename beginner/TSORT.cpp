#include <iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
 
int main() {
	int t,i;
	cin>>t;
    int a[1000001];
	for( i=0;i<t;i++)
	{
	    cin>>a[i];
	}
   sort(a,a+t);
	for(i=0;i<t;i++)
	{
	    cout<<a[i]<<"\n";
	}
	
	return 0;
}
 