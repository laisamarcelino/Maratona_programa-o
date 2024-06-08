#include <iostream>
using namespace std;

int main(){
	int N,H, numberOfRides=0;

	cin >> N;
	cin >> H;

	int A[N];

	for(int i=1; i<=N; i++){
		cin >> A[i];
		if(A[i] <= H)
			++numberOfRides;
	}

	cout << numberOfRides << endl;

	return 0;
}