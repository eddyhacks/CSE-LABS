#include "mpi.h"
#include<stdio.h>
#include<string.h>

void toggle(int length, char* word)
{
	for(int i=0;i<length;i++)
	{
		if(word[i]>='a' && word[i]<='z')
			word[i]-=32;
		else if(word[i]>='A' && word[i]<='Z')
			word[i]+=32;
	}
}


int main(int argc, char* argv[])
{
	int rank , size,x;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	MPI_Status status;
	if (rank==0)
	{
		// Taking input from keyboard 
		char str[100];
		printf("Enter a value in master process: " );
		gets(str);
		
		// length variable
		long int length = strlen(str);
		printf("Before toggle: %s",str);
		


		// sending the length
		MPI_Send(&length,1,MPI_INT,1,1,MPI_COMM_WORLD);

		// sending in processor 1
		MPI_Ssend(&str,length,MPI_CHAR,1,1,MPI_COMM_WORLD);
		//fprintf(stdout,"I have sent %s from process 0\n",str);
		
		// receiving in processor 0
		MPI_Recv(&str,1,MPI_CHAR,1,1,MPI_COMM_WORLD,&status);
		//fprintf(stdout,"I have received %s in process 0\n",str);

		printf("\nAfter toggle: %s\n",str);
		

		fflush(stdout);
	}
	else{
		// str varialbe
		char str[100];

		// length receiving in processor 1
		MPI_Recv(&x,1,MPI_INT,0,1,MPI_COMM_WORLD,&status);
		//printf("\n%d\n",x);


		// string receiving in processor 1
		MPI_Recv(&str,x,MPI_CHAR,0,1,MPI_COMM_WORLD,&status);
		//fprintf(stdout,"I have received %s in process 1\n",str);


		// calling toggle function
		toggle(x,str);

		// sending in processor 0
		MPI_Ssend(&str,1,MPI_CHAR,0,1,MPI_COMM_WORLD);
		//fprintf(stdout,"I have sent %s from process 1\n",str);
		
		fflush(stdout);
	}
	MPI_Finalize();
	return 0;
}