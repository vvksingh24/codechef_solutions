#include <iostream>
using namespace std;
#define size 100000
int main() {
		int n,x,y,t[size],i,j;
	cin>>n;
	for(i=0;i<n;i++)
	{
	    cin>>x;
	    t[i]=0;
	    for(j=0;x>=5;j++)
	    {
	        y=x/5;
	        t[i]=t[i]+y;
	        x=x/5;
	    }
	    
	}
	for(i=0;i<n;i++)
	{
	    cout<<t[i]<<endl;
	}
	return 0;
}
 