#include<iostream>
using namespace std;

void carry_refresh(int *arr,int k);


int main(){
	
	int arr[200];
	for(int i=0;i<200;i++){arr[i]=0;}
	arr[0] = 1;
	
		
	for(int j=2;j<=200;j++){
		for(int i=0;i<200;i++){
			arr[i] *= j;
		}
		carry_refresh(&arr[0],200);
		
	
		
	}
	
	
	for(int i=0;i<200;i++){
		cout<<arr[i]<<" ";
	}

}

void carry_refresh(int *arr, int k){
	
	
	for(int i=0;i<k;i++){
		
		if(arr[i]==0){continue;}
	
		if(arr[i]>9){
			arr[i+3] += (arr[i]/1000)%10;
			arr[i+2] += (arr[i]/100)%10;
			arr[i+1] += (arr[i]/10)%10;
			arr[i] = arr[i]%10;
		}
		
		}
	}
	

	

