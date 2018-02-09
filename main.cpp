//
//  main.cpp
//  Bubble
//
//  Created by Devansh Bisla on 2/8/18.
//  Copyright © 2018 Devansh Bisla. All rights reserved.
//

#include "main.hpp"
#include <iostream>

using namespace std;

int swap(int& A,int& B){
    int temp = A;
    A = B;
    B = temp;
    return 0;
}

int bubble_sort(int A[],int N){
    for (int i=0;i<N;i++){
        for (int j=N-1;j>0;j--)
        {
            if (A[j] < A[j-1]){
                swap(A[j],A[j-1]);
            }
        }
    }
    return 0;
}

int main(){
    int A[] = {5,4,30,2,10,10};
    bubble_sort(A,sizeof(A)/sizeof(A[0]));
    for (int i=0;i<sizeof(A)/sizeof(A[0]);i++){
        cout<<A[i];
    }
    
    return 0;
}
