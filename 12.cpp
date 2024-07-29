#include<iostream>
#include<math.h>
using namespace std;



int main(){

	long long int x,num =0;
	int count;
	for(int i=1;i<20;i++){
		count =0;
		num +=i;
		x = num;
		
		for(int j=2;j<=x;j++){
		
			if(x%j==0){
				x = x/j;
				count++
				;
				j=1;
			}
		}
		cout<<num<<"\t"<<count<<endl;
		if(count>=498){
			break;
		}
	}
}		
	




