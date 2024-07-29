#include<iostream>
#include<fstream>
using namespace std;
//5163

string names[5163];
string buffer;
string final;
int count =0;

void name_alloc();
void sorting();
void display();
void output();

int main(){
	
	ifstream myfile("p022_names.txt");
	getline(myfile , buffer);
	myfile.close();
	
	name_alloc();
	sorting();
	display();
	output();
	
	
	
	
}

void name_alloc(){
	for(int i=0;i<buffer.size();i++){
		if(buffer[i]==','){
			count++;
		}
		else if(buffer[i]>64&&buffer[i]<91){
			names[count]+=buffer[i];
		}
	}
	cout<<"allocation complete\n";
}

void display(){
	for(int i=0;i<5163;i++){
		cout<<names[i]<<endl;
	}
}

void sorting(){
	string abc;
	int count=0;
	bool flag =true;
	while(1){
		count =0;
		for(int i=0;i<5162;i++){
			if(names[i]>names[i+1]){
				count++;
				abc = names[i];
				names[i] = names[i+1];
				names[i+1] = abc;
			}
		}
		if(count == 0){
			break;
		}
		cout<<count<<endl;
	}
}


void output(){
	
	ofstream ksb("22_sorted_list.txt");
	ksb<<" ,";
	for(int i=0;i<5163;i++){
		ksb<<names[i]<<" , ";
	}
	
	
}







































