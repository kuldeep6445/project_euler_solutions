#include<iostream>
#include<math.h>
using namespace std;


int main(){
	
bool prime;
long long int sum = 5;

for(int i = 5; i<2000000 ; i+=2){
	
	prime = true;
	
	for(int j = 2 ; j<=sqrt(i) ; j++){
		
		if(i%j==0){
		
			prime = false;
			break;
		}
	}
	
	if(prime){
		
		sum+=i;
		//cout<<i<<endl;
	}
	
}
cout<<"\n\n\n"<<sum;

	
	
}
