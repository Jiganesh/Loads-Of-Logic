// Time Complexity
// Worst Case O(n * log n)
// Average Case O(n * log n)
// Best Case O(n * log n)

// Space Complexity O(1)

#include<bits/stdc++.h>
using namespace std;

void file_i_o() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);
  #ifndef ONLINE_JUDGE
    freopen("../Input.txt","r",stdin);
    freopen("../Output.txt","w",stdout);
  #endif
}

void merge(vector<int>&arrayInt, int left, int mid, int right) {
	int n1 = mid - left + 1;
	int n2 = right - mid;

	vector<int>arrayLeft(n1), arrayRight(n2);
	for(int i=0; i<n1; i++) 
		arrayLeft[i] = arrayInt[left+i];
	for(int j=0; j<n2; j++)
		arrayRight[j] = arrayInt[mid+1+j];

	int i=0, j=0, k=left;

	while(i<n1 && j<n2) {
		if(arrayLeft[i] <= arrayRight[j]) {
			arrayInt[k] = arrayLeft[i];
			i++;
		} else {
			arrayInt[k] = arrayRight[j];
			j++;
		}
		k++;
	}

	while(i<n1) {
		arrayInt[k] = arrayLeft[i];
		i++;
		k++;
	}

	while(j<n2) {
		arrayInt[k] = arrayRight[j];
		j++;
		k++;
	}
}

void mergeSort(vector<int>&arrayInt, int left, int right) {
	if(left >= right)
		return;
	auto mid = left + (right - left)/2;
	mergeSort(arrayInt, left, mid);
	mergeSort(arrayInt, mid+1, right);
	merge(arrayInt, left, mid, right);
}

void printArray(vector<int>arrayInt) {
	for(int i=0; i<arrayInt.size(); i++)
		cout<<arrayInt[i]<<" ";
}

int main(int argc, char** argv) {   
  file_i_o();
  //write your code here Als
  int size;
  cin>>size;
  vector<int>arrayInt(size); 
  for(int i=0; i<size; i++)
  	cin>>arrayInt[i];

  mergeSort(arrayInt, 0, size-1);

  printArray(arrayInt);
  return 0;
}