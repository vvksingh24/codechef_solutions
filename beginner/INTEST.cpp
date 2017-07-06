#include <iostream>
using namespace std;
 
int main() {
	int x,y,t,n;
	cin>>x;
	cin>>y;
	t=0;
	for(int i=0;i<x;i++)
	{
	    cin>>n;
	    if(n%y==0)
	    t++;
	}
	cout<<t;
	
	return 0;
}
 