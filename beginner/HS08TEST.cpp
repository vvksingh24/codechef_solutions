#include <iostream>
using namespace std;
 
int main() {
	int x;
	float y;
	cin>>x;
	cin>>y;
	if(x%5==0 && y>(x+0.5))
	{
	    y=y-x-0.5;
	}
	cout<<y;
	return 0;
}