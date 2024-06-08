#include <stdio.h>

int main(){
	int N,H, numberOfRides=0;

	scanf("%d %d", &N, &H);

	int A[N];

	for(int i=1; i<=N; i++){
		scanf("%d", &A[i]);
		if(A[i] <= H)
			numberOfRides++;
	}
	printf("%d\n", numberOfRides);
	return 0;
}