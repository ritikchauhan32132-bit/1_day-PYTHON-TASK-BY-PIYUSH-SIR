//  1. Write a function to print counting from 1 to 100

#include<iostream>
using namespace std;

int countOneToHundred(){

    for(int i = 1; i < 100; i++){
        cout<<i<<endl;
    }
    return 100;
}

int main(){

    int count = countOneToHundred();
    cout<<count;


}