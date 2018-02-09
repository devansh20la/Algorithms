
//  main.cpp
//  Algorithms
//
//  Created by Devansh Bisla on 1/31/18.
//  Copyright © 2018 Devansh Bisla. All rights reserved.
//

#include <iostream>

using namespace std;

int insertion_sort(int A[]){
	for (int j=1;j<5;j++){
		int key = A[j];
		int i = j-1;
		while (i>=0 and A[i]>key) {
			A[i+1] = A[i];
			i = i-1 ;
		}
		A[i+1] = key;
	}
	return 0;
}

int main(){
	int A[] = {5,40,3,2,1};
	insertion_sort(A);
	for (int i =0;i<sizeof(A)/sizeof(A[0]);i++)
		cout<<A[i]<<endl;
}
