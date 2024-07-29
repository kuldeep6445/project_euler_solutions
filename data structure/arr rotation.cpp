#include<iostream>
#include<vector>
//#include<unordered_map>
using namespace std;
class solution
{
    vector<int>vect;
    unordered_map<int,int> chk;
		public:
		solution(vector<int>&vect)
		{    this->vect=vect;  }
		long no_ways(int n)
		{
			if(n<0)
			 return 0;
			if(n==0)
			  return 1;
			long long ways=0;
			if(chk[n]!=0)
			{  if(chk[n]==-1)
			    return 0;
			    else 
			    chk[n];
			}
			for(int num:vect)
			ways=ways+no_ways(n-num);
			cout<<ways<<' ';
			if(ways==0)
			chk[n]=-1;
			else
			chk[n]=ways;
			return ways;
		}
};
int main()
{
		vector<int>vect{1,2,5,10,20,50,100};
    solution Sol(vect);
	long n=Sol.no_ways(200);
	cout<<endl<<n<<endl;
}


