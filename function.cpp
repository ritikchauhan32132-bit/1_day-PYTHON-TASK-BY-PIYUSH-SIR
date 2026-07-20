#include<iostream>
using namespace std;

void namePrint(){
    for(int i = 0; i <= 10; i++){
        cout<<"Ritik"<<" ";
    }
}

int twoNumberSum(int a, int b){
    int number = a + b;
    return number; 
}


int main(){

    // namePrint();

    int sum = twoNumberSum(3,5);
    cout<<sum;

}