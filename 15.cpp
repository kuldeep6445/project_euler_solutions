#include<iostream>
#include<vector>
#include<fstream>
using namespace std;

int num[15][15];
vector<int> sum;
void display();
void assign();
void output();
int multiply(int x,int y);
long long int pro=1;


int main(){
	
	assign();
	display();
	
	multiply(0,0);
	output();	
}


int multiply(int x,int y){
	if(x==0){
		sum.push_back(num[x][y]);
		multiply(x,y+1);
		multiply(x+1,y+1);
	}
	else if(y==14){
		sum.push_back(num[x][y]);
		sum.push_back(1000);		
	}
	else{
		sum.push_back(num[x][y]);
		multiply(x,y+1);
		multiply(x+1,y+1);
		multiply(x-1,y+1);
	}
}


void output(){
	for(int i=0;i<sum.size();i++){
		cout<<sum[i]<<" ";
	}
	
}


void display(){
	for(int i=0;i<15;i++){
		for(int j=0;j<15;j++){
			if(num[i][j]<10){
				cout<<"0"<<num[i][j]<<" ";
			}
			else{
			
			cout<<num[i][j]<<" ";
		}}
		cout<<endl;
	}
}

void assign(){
	for(int i=0;i<15;i++){
		for(int j=0;j<15;j++){
			num[i][j]=0;
		}
	}
	ifstream myfile("15text.txt");
	string buffer;
	
	for(int i=0;i<15;i++){
		getline(myfile,buffer);
		for(int j=0;j<=i;j++){
			num[i][j] = (buffer[j*3]-48)*10 + buffer[j*3 +1]-48;
		}
	}
}
