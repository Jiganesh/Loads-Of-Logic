// Time Complexity:
// Worst Case O(n ^ 2)
// Average Case O(n * log n)
// Best Case O(n * log n)

// Space Complexity:
// O(n)

#include <iostream>

using namespace std;

int partition(int arr [], int low, int high) {
	int pivot = arr[low];
	int i = low;
	int j = high;
	while(i < j) {
		while(arr[i] <= pivot) i++;
		while(arr[j] > pivot) j--;

		if(i < j){
			int temp = arr[j];
			arr[j] = arr[i];
			arr[i] = temp;
		}
	}
	arr[low] = arr[j];
	arr[j] = pivot;
	return j;
}

void quickSort(int arr [], int low, int high) {
	if(low < high) {
		int pivot = partition(arr, low, high);
		quickSort(arr, low, pivot - 1);
		quickSort(arr, pivot + 1, high);
	}
}

void display(int arr [], int size){
	for (int i = 0; i < size; ++i){
		cout << arr[i] << " ";
	}
	cout << endl;
}

int main(){
	int arr [] = {56, 23, 83, 43, 72, 27, 78, 39, 45, 27, 19};
	int len = sizeof(arr) / sizeof(int);
	display(arr, len);
	quickSort(arr, 0, len - 1);
	display(arr, len);
	return 0;
}
