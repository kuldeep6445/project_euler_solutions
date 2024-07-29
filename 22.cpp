#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream myfile("22_sorted_list.txt");
	string buffer;
	getline(myfile,buffer);
	
	int no_of_names=1;
	for(int i=0;i<buffer.size();i++){
		if(buffer[i]==','){
			no_of_names++;
		}
	}
	//cout<<no_of_names;
	//5163
	//2575402629801
	//2573886133413
	//850081394
	//849756858
	//850237017
	//850081394
	//871198282
	int count =0;
 	long long int sum =0;
	
	for(int i=0;i<buffer.size();i++){
		if(buffer[i]==','){
			count++;
		}
		else if(buffer[i]>64&&buffer[i]<91){
			sum += ((int(buffer[i]-64))*count);
			cout<<count<<"\t"<<sum<<endl;
		}
		
	}

}
