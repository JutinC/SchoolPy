/*
Justin Choi
IDT period 3
PSET2
Methods
*/


#include <stdio.h>
/*argument count argument vector
make hello argument count 4 fred 17.4
argc = 4
argv = ["./hello", "4", "fred", "17.4"]
method gives values back or procedure to call it
*/

//Method headers
int add(int a, int b);
double divide(double a, double b);
void displayMath(int answer);
void displayMath2(double answer2);

//Main entry function
int main(int argc, char *argv[]){
    int answer = add(7,5);
    displayMath(answer);
    double answer2 = divide(7,0);
    displayMath2(answer2);
        //todo
}
//Function that returns sum of two integers
int add(int a, int b){
    return a + b;
}
double divide(double a, double b){
    if(b!=0){
        return a/b;
    }else{
        return 1;
    }
}

//procedure that displays 2 results
void displayMath(int answer){       //scoping in so same variables different
    printf("The answer is: %d.\n", answer);
}
void displayMath2(double answer2){   //no need for the 2 only for c
    printf("The answer is: %f.\n", answer2);
}