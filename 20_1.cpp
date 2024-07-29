#include<iostream>
#include<vector>
using namespace std;

void factorial(int x);

int main(){
	factorial(100);	
}

void factorial(int x){
	
	vector<int> num;
	
	num.push_back(1);
	
	for(int j=2;j<=x;j++){
		
		for(int i=0;i<num.size();i++){num[i] *= j;}
		if(num.back() >=10){num.push_back(0);}
		
		for(int i=0;i<num.size();i++){
		
		if(num[i]==0){continue;}
	
		if(num[i]>9){
			num[i+3] += (num[i]/1000)%10;
			num[i+2] += (num[i]/100)%10;
			num[i+1] += (num[i]/10)%10;
			num[i] = num[i]%10;
		}
		
		}
		
			
	}
	num.push_back(0);
	int sum=0;
	for(int i=num.size()-1;i>=0;i--){
		cout<<num[i]<<" ";
		sum+=num[i];
	}
	cout<<"\n\n"<<num.size();

	
	
}
