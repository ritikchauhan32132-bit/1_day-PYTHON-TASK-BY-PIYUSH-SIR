// 2. Write a function to find Simple Interest

#include<iostream>
using namespace std;

float simpleIntrest(){

    float si;
    float p;
    float r;
    float t;

    cout<<"Enter Principal ammount: ";
    cin>>p;

    cout<<"Enter interest rate: ";
    cin>>r;

    cout<<"Enter time in year: ";
    cin>>t;

    si = (p * t * r)/100;

    cout<<"Your Total Intrest: "<<si<<endl;


    return si;

}


int main(){

    float in = simpleIntrest();
    cout<<in;


}
