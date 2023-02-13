#include <mpi/mpi.h>
#include <stdio.h>
#include <stdlib.h>

int factorial(int n){
	if (n==1)
			return 1;
	else 
		return n*factorial(n-1);
}

int main(int argc, char *argv[]){
	int rank, size, N,*A,*Arr, c, i, fact, sum = 0;

	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);

	if(rank == 0){
		N = size;
		fprintf(stdout, "Enter %d values: \n", N);
		fflush(stdout);
		A = (int *)calloc(N, sizeof(int));
		for(int i=0;i<N;i++)
			scanf("%d", &A[i]);
	}
	MPI_Scatter(A,1,MPI_INT, &c, 1, MPI_INT, 0, MPI_COMM_WORLD);
	c=factorial(c);
	Arr= (int *)calloc(N, sizeof(int));
	MPI_Gather(&c,1,MPI_INT,Arr,1,MPI_INT,0,MPI_COMM_WORLD);

	if(rank == 0){
		for(int i=0;i<N;i++){
			sum=sum+Arr[i];
		}
		fprintf(stdout, "The Sum is %d\n", sum);
		fflush(stdout);
		free(A);
	}
	MPI_Finalize();
	return 0;
}                                        
