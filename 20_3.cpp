#include<iostream>
using namespace std;

void fact(int x);

int main(){
	fact(100);
}


void fact(int x){
	
	int num[200];
	
	for(int i=0;i<200;i++)
	num[i]=0;
	
	num[0]=1;
	
	for(int i=x;i>1;i--){
		for(int j=0;j<200;j++){
			num[j] *= i;
		}
		for(int j=0;j<200;j++){
			if(num[j]>=100&&num[j]<1000){
				num[j+2] += num[j]/100;
				num[j+1] += (num[j]/10)%10;
				num[j] = num[j]%10;
			}
			else if(num[j]>=1000){
				num[j+3] += num[j]/1000;
				num[j+2] += (num[j]/100)%10;
				num[j+1] += (num[j]/10)%10;
				num[j] = num[j]%10;
			}
			else if(num[j]<100&&num[j]>=10){
				num[j+1] += num[j]/10;
				num[j] = num[j]%10;
			}
		}
		
	}
	int sum =0;
	for(int i=199;i>=0;i--)
	sum+=num[i];
	
	cout<<sum;
}
