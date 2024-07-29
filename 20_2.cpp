#include<iostream>
#include<vector>
using namespace std;


int main(){
	int fact = 100,size =1;
	
	vector<int> num;
	num.push_back(1);
	
	for(int i=fact;i>1;i--){
		for(int j=0;j<size;j++){
			num[j] *= i;
		}
		if(num.back()>=100&&num.back()<1000){
			num.push_back(0);
			num.push_back(0);
			size+=2;
		}
		
		else if(num.back()<100&&num.back()>=10){
			num.push_back(0);
			size+=1;
		}
		for(int j=0;j<size;j++){
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
	
	cout<<size;
	
	
	
	
	
	
	
}
