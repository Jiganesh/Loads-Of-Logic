#include <iostream>
using namespace std;
void arrayEvenAndOdd(int arr[], int n)
{
    int a[n], index = 0;
    for (int i = 0; i < n; i++)
    {
        if (arr[i] % 2 == 0)
        {
            a[index] = arr[i];
            index++;
        }
    }
    for (int i = 0; i < n; i++)
    {
        if (arr[i] % 2 != 0)
        {
            a[index] = arr[i];
            index++;
        }
    }
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}
 
// Driver code
int main()
{
    int arr[] = { 1, 3, 2, 4, 7, 6, 9, 10 };
    int n = sizeof(arr) / sizeof(int);
 
    // Function call
    arrayEvenAndOdd(arr, n);
    return 0;
}
