#include<iostream>
using namespace std;
int main(){
 
//  1-100 print 

    int i = 1;

    while(i <= 100){
        cout<<i<<endl;
        i++;
    }


//  100 - 0 print

    int j = 100;

    while(j > 0){
        cout<<j<<endl;
        j = j - 1;
    }


// 50 times name print

    string name;
    cout<<"Enter Your Name: ";
    cin>>name;

    int k = 1;

    while (k <= 50) {
        cout<<name<<endl;
        k = k + 1;
    }

// 0 - (-10) print

    int l = 0;

    while(l >= (-10)){
        cout<<l<<endl;
        l = l - 1;
    }

// 7 table

    int m = 7;
    
    while(m <= 70){
        cout<<m<<endl;
        m = m + 7;
    }

// A - Z Alphabet

    char ch = 'A';
    while(ch <= 'Z'){
        cout<<ch<<" ";
        ch++;
    }

// a - z alphabet

    char n = 'a';
    while(n <= 'z'){
        cout<<n<<" ";
        n++;
    }


}