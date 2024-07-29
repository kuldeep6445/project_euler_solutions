#include<iostream>
#include<fstream>
#include<vector>
using namespace std;



int main(){

ifstream file("13text.txt");

string buffer;
vector<int> sum(50);
for(int j=0;j<50;j++){sum[j]=0;}


while(!(file.eof())){
	
	getline(file,buffer);
	
	for(int i=0;i<50;i++){
		sum[i] += (buffer[i]-48);
	}
	
	//236
	//19360
	//4240
}

for(int i=49;i>=40;i--){
	sum[i-2] += (sum[i]/100);
	sum[i-1] += (sum[i]/10)%10;
	sum[i] = sum[i]%10;
}

for(int j=0;j<50;j++){cout<<sum[j]<<" ";}
	
}














