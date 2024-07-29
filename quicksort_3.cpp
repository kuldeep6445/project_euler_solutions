#include<iostream>
#include<vector>
using namespace std;

void swap(long *a,long *b){
	long temp = *b;*b=*a;*a=temp;
}

int partition(vector<long> &arr, int low, int high, int piv[])  
{  
    if (arr[low] > arr[high])  
        swap(&arr[low], &arr[high]);  
    int j = low + 1;  
    int g = high - 1, k = low + 1, p = arr[low], q = arr[high];  
    while (k <= g)  
    {   
        if (arr[k] < p)  
        {  
            swap(&arr[k], &arr[j]);  
            j++;  
        }   
        else if (arr[k] >= q)  
        {  
            while (arr[g] > q && k < g)  
                g--;  
            swap(&arr[k], &arr[g]);  
            g--;  
            if (arr[k] < p) 
            {  
                swap(&arr[k], &arr[j]);  
                j++;  
            }  
        }  
        k++;  
    }  
    j--;  
    g++;  
    swap(&arr[low], &arr[j]);  
    swap(&arr[high], &arr[g]);  
    piv[0] = j; 
    piv[1] = g;  
}  

void quicksort(vector<long> &num,int start,int end){
	if(end>start){
		int piv[2];
		partition(num,start,end,piv);
		quicksort(num,start,piv[0]-1);
		quicksort(num,piv[0]+1,piv[1]-1);
		quicksort(num,piv[1]+1,end);
	}
}

int main(){
	vector<long> num(5);
	num[0]=4;num[1]=7;num[2]=3;num[3]=6;num[4]=8;
	quicksort(num,0,4);
	for(int i=0;i<5;i++)
		cout<<num[i]<<" ";
}