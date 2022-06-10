/*  
*   Solution to 528. Random Pick With Weight
*   https://leetcode.com/problems/random-pick-with-weight/
*/

/*
*   Constraints:
*   1 <= wSize <= 10^4
*   1 <= w[i] <= 10^5
*   pickIndex will be called at most 10^4 times
*/

/*-------------------------------------------------------------------------------------------------
*
*   The solution allocates an array of size 'wSize'. Each element holds the sum of the previous
*   elements' pick weights. 'pickIndex' generates a random number from 1 to total pick weight
*   (i.e. the last element of the solution's array). Then it returns an index ceiling where the
*   random number falls under its element range.
*
*   Time complexity:    O(N) where N is 'wSize', the time needed to store the pick weight sum.
*                       O(logN) to search for the pick index ceiling.
*
*   Space complexity:   O(N) the weight sum array.
*
*--------------------------------------------------------------------------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef struct {
    int *wArr;
    int wSize;
} Solution;

Solution *solutionCreate(int *w, int wSize) {
    int arr_i = 0;
    int wSum = 0;
    Solution *obj = NULL;
    
    obj = (Solution*)malloc(sizeof(Solution));
    if (!obj) {
        perror("malloc");
        return NULL;
    }

    obj->wSize = wSize;
    obj->wArr = (int*)malloc(obj->wSize * sizeof(int));
    if (!obj->wArr) {
        perror("malloc");
        free(obj);
        return NULL;
    }

    /*  Add current weight sum to each element  */
    for (; arr_i < obj->wSize; ++arr_i) {
        wSum += w[arr_i];
        obj->wArr[arr_i] = wSum;
    }

    return obj;
}

int findIndexCeiling(int *arr, int value, int base, int height) {
    if (value <= arr[base]) {
        return base;
    }
    else if (value > arr[height - 1] && value <= arr[height]) {
        return height;
    }

    /*  Compress search boundaries until value range found  */
    while (base < height) {
        int mid = (base + height) / 2;
        if (value > arr[mid]) {
            base = mid + 1;
        }
        else if (value == arr[mid]) {
            return mid;
        }
        else {
            height = mid;
        }
    }

    return base;
}

int solutionPickIndex(Solution *obj) {
    int randVal = 0;

    /*  Check if 0 is the only index    */
    if (obj->wSize <= 1) {
        return 0;
    }

    /*  Generate random value from 1 to weight sum  */
    randVal = (rand() % obj->wArr[obj->wSize - 1]) + 1;

    /*  Brute force approach O(N)   */
    /*
    *   int index = 0;
    *   for (; index < obj->wSize; ++index) {
    *       if (randVal <= obj->wArr[index]) {
    *           return index;
    *       }
    *   }
    * 
    *   return -1;
    */

    /*  Index ceiling approach O(logN)  */
    return findIndexCeiling(obj->wArr, randVal, 0, obj->wSize - 1);
}

void solutionFree(Solution *obj) {
    if (obj) {
        free(obj->wArr);
        obj->wArr = NULL;
        free(obj);
    }
}

/*  TEST CODE   */
const int PICK_MAX = 10;

int main() {
    int pickCount = 0;
    int arr[] = { 2, 2, 5, 10, 7 };
    Solution *obj = NULL;

    /*  Seed random number generator    */
    srand(time(NULL));
    
    /*  Create solution object  */
    obj = solutionCreate(arr, 5);
    if (!obj) {
        return 1;
    }

    /*  Pick random index   */
    for (; pickCount < PICK_MAX; ++pickCount) {
        printf("%d ", solutionPickIndex(obj));
    }
    printf("\n");

    /*  Free solution object    */
    solutionFree(obj);
    obj = NULL;

    return 0;
}
