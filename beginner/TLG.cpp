
#include <iostream>
using namespace std;
#define size 10000
int main()
{
    int a[size],b[size],lead[size],flag[size];
    int n,x=0,y=0,maxlead,temp,i;
    cin>>n;
    for(i=0;i<n;i++)
    {
        cin>>a[i]>>b[i];
    }
    for(i=0;i<n;i++)
    {
        x+=a[i];
        y+=b[i];
        if(x>y)
        {
            lead[i]=x-y;
            flag[i]=0;
        }
        else
        {
            lead[i]=y-x;
            flag[i]=1;
        }
    }
    maxlead=lead[0];
    for(i=0;i<n;i++)
    {
        if(lead[i]>maxlead)
        {
            maxlead=lead[i];
            temp=i;
            
        }
    }
    if(flag[temp]==0)
    {
        cout<<1<<"\t"<<maxlead;
    }
    else
    cout<<2<<"\t"<<maxlead;
   
    
    
	return 0;
}