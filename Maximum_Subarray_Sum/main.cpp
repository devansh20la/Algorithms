//
//  main.cpp
//  Algorithms
//
//  Created by Devansh Bisla on 11/20/17.
//  Copyright © 2017 Devansh Bisla. All rights reserved.
//

#include <iostream>

using namespace std;

// Function to define maximum of two and three numbers
int max(int a, int b) { return (a > b)? a : b; }
int max_th(int a, int b, int c){
    return max(a,max(b,c));
}

//Max crossing function
int maximum_crossing(int arr[],int l, int m, int h){
    
    int left_sum = INT_MIN;
    int sum=0;
    
    // Iterate over all values in the left half of the array to find maximum sum
    for (int i=m;i>=l;i--){
        sum = sum + arr[i];
        if (sum > left_sum){
            left_sum = sum;
        }
    }
    sum = 0;
    int right_sum=INT_MIN;
    
    // Iterate over all values in the right half of the array to find maximum sum
    for (int i=m+1;i<=h;i++){
        sum = sum + arr[i];
        if (sum > right_sum){
            right_sum = sum;
        }
    }
    
    return (left_sum + right_sum);
}

//max sub_array function that recursively calls every other function
int maximum_subarray(int inp_arr[], int l,int h){
    
    if (l==h){
        return inp_arr[l];
    }
    int m = (l + h)/2;
    
    // Recursive call to max in left, max crossing, max in right :)
    
    return max_th(maximum_subarray(inp_arr, l, m),
            maximum_subarray(inp_arr, m+1, h),
            maximum_crossing(inp_arr, l, m, h)
               );
    
    return 0;
}

// Testing
int main(int argc, const char * argv[]) {
    int A[5] = {-1,9,1,-2,2};
    int o = maximum_subarray(A, 0, 4);
    cout<<o;
    return 0;
}

