#include<bits/stdc++.h>
using namespace std;

// Function to find number of subarrays 
// having product equal to 1. 
long long int countOne(long long int arr[], long long int n){ 
	 long long int i = 0; 
	
	// To store number of ones in 
	// current segment of all 1s. 
	 long long int len = 0; 
	
	// To store number of subarrays 
	// having product equal to 1. 
	long long int ans = 0; 
	
	while(i < n){ 
		
		// If current element is 1, then 
		// find length of segment of 1s 
		// starting from current element. 
		if(arr[i] == 1){ 
			len = 0; 
			while(i < n && arr[i] == 1){ 
				i++; 
				len++; 
			} 
			
			// add number of possible 
			// subarrays of 1 to result. 
			ans += (len*(len+1)) / 2; 
		} 
		i++; 
	} 
	
	return ans; 
} 

/// Function to find number of subarrays having 
/// product exactly equal to k. 
long long int findSubarrayCount(long long int arr[], long long int n, int k) 
{ 
	long long int start = 0, endval = 0, p = 1, countOnes = 0;
	long long int res = 0; 

	while (endval < n) 
	{ 
		p *= (arr[endval]); 

		// If product is greater than k then we need to decrease 
		// it. This could be done by shifting starting point of 
		// sliding window one place to right at a time and update 
		// product accordingly. 
		if(p > k) 
		{ 
			while(start <= endval && p > k) 
			{ 
				p /= arr[start]; 
				start++; 
			} 
		} 
		
		
		if(p == k) 
		{ 
			// Count number of succeeding ones. 
			countOnes = 0; 
			while(endval + 1 < n && arr[endval + 1] == 1) 
			{ 
				countOnes++; 
				endval++; 
			} 

			// Update result by adding both new subarray 
			// and effect of succeeding ones. 
			res += (countOnes + 1); 

			// Update sliding window and result according 
			// to change in sliding window. Here preceding 
			// 1s have same effect on subarray as succeeding 
			// 1s, so simply add. 
			while(start <= endval && arr[start] == 1 && k!=1) 
			{ 
				res += (countOnes + 1); 
				start++; 
			} 

			// Move start to correct position to find new 
			// subarray and update product accordingly. 
			p /= arr[start]; 
			start++; 
		} 

		endval++; 
	} 
	return res; 
} 

int main()
{
	int t;
	cin>>t;
	long long int arr[100000+5];
	while (t--)
	{
		long long int n;
		cin>>n;
		long long int total, result; 
		for (int i = 0; i<n; i++)
		{
		    arr[i] = 0;
		}
		long long int ele;
		for (int i = 0; i<n; i++)
		{   
			cin>>ele;
			if (ele == 0)
			    arr[i] = 4;
			else if (ele%4 == 0 )
				{
				    arr[i] = 4;
				}
			else if (ele%2 == 0 and ele%4 != 0)
				{
				    arr[i] = 2;

				}
			else
				arr[i] = 1;
			
		}
		result = findSubarrayCount(arr, n, 2);
		total =(n*(n+1))/2;
		cout<<total-result<<"\n";
		
	}
	return 0;
}