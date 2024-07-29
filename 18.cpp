#include<iostream>
#include<fstream>
using namespace std;

int map[15][15];
int sum[200];
int count=0;
void display(){
	for(int i=0;i<15;i++){
		for(int j=0;j<15;j++){
			if(map[i][j]<10){
				cout<<"0"<<map[i][j]<<" ";
			}
			else{	
			cout<<map[i][j]<<" ";
			}
		}
		cout<<endl;
	}
}
int move(int x,int y);


int main(){
	ifstream list("18_text.txt");
	
	string buffer;
	
	for(int i=0;i<200;i++)
		sum[i]=0;
	for(int i=0;i<15;i++){
		for(int j=0;j<15;j++){
			map[i][j]=0;
		}
	}
	
	for(int i=0;i<15;i++){
		getline(list , buffer);
		for(int j=0;j<=i;j++){
			map[i][j] = (buffer[j*3]-48)*10 + buffer[j*3 +1]-48;
		}		
	}
	display();
	move(0,0);
	
	for(int i=0;i<200;i++)
		cout<<sum[i]<<endl;
	
}


int move(int x,int y){
	
	sum[count] += map[x][y];
	if(y==14){
		count++;
		cout<<count<<endl;		
	}
	else if(x!=0){
		move(x-1,y+1);
		move(x,y+1);
		move(x+1,y+1);
	}
	else if(x==0){
		move(x,y+1);
		move(x+1,y+1);
	}
	 
	
}




















