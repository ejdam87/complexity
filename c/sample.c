
int sum(int *array, int n){

    int res = 0;
    for (int i = 0; i < n; i++){
        res += array[i];
    }

    return res;

}
