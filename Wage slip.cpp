#include<iostream>
#include<stdlib.h>
#include<stdio.h>
#define n 10
using namespace std;
class sales{
    int sno;
    char sname[100];
    float whr,wage,totalwage;
    void calcwage(){
        totalwage=whr*wage;
    }
    public:
        void in_data(int);
        void out_data(int);
}sal[10];
void sales::in_data(int x){
    wage=100.28;
    totalwage=0.0;
    cout<<"\nEnter the id of employee";
    cin>>sal[x].sno;
    cout<<"Enter name of employee";
    gets(sal[x].sname);
    cout<<"\nEnter the total working hours";
    cin>>sal[x].whr;
    
    calcwage();
}
void sales::out_data(int y){
    cout<<"\n\t\t\t\t\t\t\t KK & co ";
    cout<<"\n\t\t\t\t\t\t\t ~~~~~~~"<<"\n";
    cout<<"\n\t\t\t\t\t\t\t ID:"<<sal[y].sno<<"\n";
    cout<<"\n\t\t\t\t\t\t\t Name:"<<sal[y].sname<<"\n";
    cout<<"\n\t\t\t\t\t\t\t wage per hour:"<<"$"<<sal[y].wage<<"\n";
    cout<<"\n\t\t\t\t\t\t\t Total hours worked:"<<sal[y].whr<<"\n";
    cout<<"\n\t\t\t\t\t\t\t Total Wages:"<<"$"<<sal[y].totalwage<<"\n";
}
    //sales sal[10];

int main(){

    for(int i=0;i<n;i++){
        sal[i].in_data(i);
    }
    for(int i=0;i<n;i++){
            sal[i].out_data(i);
    }
    return 0;
}