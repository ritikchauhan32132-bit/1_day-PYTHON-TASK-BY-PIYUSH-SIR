#include<iostream>
using namespace std;

int main(){
    
//  1 - 100 counting print

    for(int i = 1; i <= 100; i = i+1){
        cout<<i<<endl;
    }

// 100-1 Reverse counting

    for(int i = 100; i >= 1; i--){
        cout<<i<<endl;
    }

// Name printing 50 times

    string name = "Ritik Kumar";
    for(int i = 0; i <= 50; i++){
        cout<<name<<endl;
    }

// 0 - (-10) counting 

    for(int i = 0; i >= (-10); i--){
        cout<<i<<endl;
    }

// 7 table print
    
    for(int i = 7; i <= 70; i = i + 7){
        cout<<i<<endl;
    }

// A - Z  ALPHABET PRINT

    for(char i = 'A'; i <= 'Z'; i++){
        cout<<i<<endl;
    }

// a - z alphabet print

    for (char i = 'a'; i < 'z'; i++){
       cout<<i<<endl;
    }
    

    return 0;
}