#include<iostream>
using namespace std;

const char days[7] = {'m' ,'T' ,'w','t','f','s','S'};
char find (int x);
bool leap_check(int x);
int count(char first_day);


int main(){
	
	int year[100];
	char days1[100];
	for(int i=0;i<100;i++)
	year[i]= 1901+i;
	
	days1[0] = days[1];
	
	
	for(int i=0;i<100;i++)
	cout<<year[i]<<"\t"<<days1[i]<<"\n";
	
	
}

char find (int x,char prev_year_first_day){
	int y;
	if(leap_check(x-1)){
		for(int i=0;i<7;i++){
			if(prev_year_first_day==days[i]){
			 y = i+2;
			break;}
		}
		
		
		if(y>6){ y-=7;
		}
		return days[y];
		
	}
	else{
		int y;
		for(int i=0;i<7;i++){
			if(prev_year_first_day==days[i]){
			 y = i+1;
			break;}
		}
		
		
		if(y>6){ y-=7;
		}
		return days[y];
	}
}

bool leap_check(int x){
	if(x%100==0){
		if(x%400==0){
			//cout<<"true";
			return true;
		}
		else {
			//cout<<"false";
			return false;
		}
	}
	else if(x%4==0){
		//cout<<"true";
		return true;
	}
	else {
		//cout<<"false";
		return false;
	}
}
