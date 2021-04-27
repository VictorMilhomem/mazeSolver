#include <iostream>
#include <stdlib.h>
#include<string.h>
#include<time.h>
using namespace std;

int n, xi, yi, xf, yf;
char L[101][101];

void Initialize(){
    int i, j, k, l, p;
    srand(time(NULL));
    memset(L, ' ', sizeof(L));
    //Creating the maze
    for (i=1; i<=n; i++){
        L[1][i]=L[n][i]='#';  L[i][1]=L[i][n]='#';
    }
    //Creating the obstacles
    for (k=1; k<=(n/3)-2; k++){
        l= 3*k+1;  i = rand()%(n/2-4)+ 3;
        if (k%2==0) 
		    for (p=i; p<=n; p++) {if (rand()%100 > 10) L[p][l]='#';  }
        else 
		    for (p=1; p<=i; p++) {if (rand()%100 > 10) L[p][l]='#';  }
    }
    xi= rand()%(n-2)+2; yi = rand()%(n-2)+2;  xf = rand()%(n-2)+2;  yf = n;
    L[xi][yi] = 'A';  L[xf][yf]='B';
}

void CreateMazeFile()
{
    FILE *fp;
    fp = fopen("./mazes/maze.txt", "w");
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
            fputc(L[i][j], fp);
        fputc('\n', fp);
    }
    fflush(fp);
    fclose(fp);
}

int main(){
	srand(time(NULL));
    while (true){
        cout<<"Mazes Dimensions:  n =";  cin >>n;
        if (n > 0)
        {
    	    Initialize();
            CreateMazeFile();  
		    cin.get();
            break;
        }
        else
        {
            break;
        }
    }
    return 0;
}
