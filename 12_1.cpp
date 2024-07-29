#include<iostream>
#include<math.h>
using namespace std;
void refresh(int *arr);
int solve(int k,int * arr);
int main(){
/*	
	int x=28,count=0;
	for(int j=2;j<=x;j++){
		cout<<j<<" ";
			if(x%j==0){
				cout<<"i"<<j;
				x = x/j;
				count++;
				j=1;
			}
		}
		cout<<"\t\t\t\t"<<count<<endl;
*/
	long long int x,num =0;
	int count;
	int num1[500];
	int num2[500];
	refresh(&num1[0]);
	refresh(&num2[0]);
	
	for(int i=1;i<20;i++){
		count =0;
		num +=i;
		x = num;
		int k=0;
		for(int j=2;j<=sqrt(x);j++){
			if(x%j==0){
				x = x/j;
				
				if(num2[k]!=0){num1[k] = j;}
				else{num2[k]+=1;}
				
				k++;
				j=1;
			}
		}
		count = solve(k,&num2[0]);
		cout<<num<<"\t"<<count<<endl;
		if(count>=498){
			break;
		}
	}
	refresh(&num1[0][0]);
}




void refresh(int *arr){
	
	for(int i=0;i<500;i++){
		arr[i]=0;
		//cout<<arr[i];
	}
	
	
}


int solve(int k , int *arr){
int div[300];
int a=0;
	for(int i=0;i<500;i++){
		if(arr[i]!=0){
			div[a] = 
		}
	}

	
}
