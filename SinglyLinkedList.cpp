#include<iostream>
using namespace std;
struct Node{
    int data;
    Node* next;
};
class LinkedList {
private:
    Node* head;  // Pointer to the head of the linked list

public:
    LinkedList(){
        head = nullptr;
    }
    ~LinkedList(){
        Node* current = head;
        while(current!=nullptr){
            Node* next= current->next;
            delete current;
            current= current->next;
        }
    }
    bool isEmpty(){
        if(head==nullptr)
        {
            cout<<"List Empty";
            return true;
        }
        return false;
    }
    void insertBeg(int value);
    void insertEnd(int value);
    void insert(int value,int pos);
    int removeBeg();  
    void removeEnd();  
    void remove(int value);  
    bool search(int value); 
    void sort();
    void display(){
        Node* current = head;
        while(current!=nullptr){
            cout<<current->data<<"->";
            current=current->next;
        }
        cout<<"null"<<endl;
    }    
};
void  LinkedList::insertBeg(int value) {
    Node* newNode = new Node;
    newNode->data = value;
    newNode->next = head;
    head = newNode;
}
void  LinkedList::insertEnd(int value) {
    Node *newNode = new Node;
    newNode->data=value;
    newNode->next=nullptr;
    if(head==nullptr) {
        head=newNode;
    }
    else{
    Node *temp = head;
    while(temp->next != nullptr){
        temp=temp->next;
    }
    temp->next = newNode;
    }
}
void   LinkedList::insert(int value, int pos){
    if(pos<0) return;
    Node* newNode =  new Node;
    newNode->data = value;
    if(pos==0){
        newNode->next=head;
        head=newNode;
    }
    else{
        Node* current = head;
        for(int i=0;i<pos-1 && current!=nullptr;i++){
            current = current->next;
        }
        if(current != nullptr){
            newNode->next = current->next;
            current->next= newNode;
        }
    }
}
int   LinkedList::removeBeg(){
    if(isEmpty()) return -1;
    Node* temp = head;
    head = head->next;
    int value = temp->data;
    delete temp;
    return value;
}
void   LinkedList::removeEnd(){
    if(isEmpty()) return;
    if(head->next == nullptr) {
        removeBeg();
    }else{
        Node* temp = head;
        while(temp->next->next != nullptr){
            temp = temp->next;
        }
    delete temp->next;
    temp->next = nullptr;
    }
}
void   LinkedList::remove(int value){
    Node* current = head;
    Node* prev = nullptr;
    while(current != nullptr && current->data!=value){
        prev = current;
        current = current->next;
    }
    if(current!=nullptr){
        if(prev!=nullptr){
            prev->next = current->next;
            }
        else{
            head=current->next;
        }
            delete current;
    }
}
bool   LinkedList::search(int value){
    Node *current = head;
    while (current != nullptr)  { 
        if (current->data == value) {return true;}  
        current = current->next;  
    } 
    return false;
}
void LinkedList::sort() {
    if (head == nullptr || head->next == nullptr) return; // If list is empty or has only one node, it's already sorted

    bool swapped;
    int temp;
    do {
        swapped = false;
        Node* current = head;
        while (current->next != nullptr) {
            if (current->data > current->next->data) {
                // Swap data values of adjacent nodes if they are in the wrong order
                temp = current->data;
                current->data = current->next->data;
                current->next->data = temp;
                swapped = true;
            }
            current = current->next;
        }
    } while (swapped);
}

class Stack{
    LinkedList stack;
    public:
    void push(int value){
        stack.insertBeg(value);
    }
    int pop(){
        int value=stack.removeBeg();
        return value;
    }
    void display(){
    stack.display();
    }
};
int main(){
    LinkedList list;
    list.insertBeg(10);
    list.insertBeg(20);
    list.insertBeg(30);

    list.display();

    list.insert(40,2);
    list.insertEnd(50);

    list.display(); // Output: 30 20 10

    list.removeBeg();// remove the node with data 30
    list.remove(20);

    list.display(); // Output: 30 10

    cout << "Is 50 in the list? " << (list.search(50) ? "Yes" : "No") <<endl; // Output: Yes

    list.removeEnd();
    list.display();
    cout << "Is 50 in the list? " << (list.search(50) ? "Yes" : "No") <<endl; // Output: Yes
    
    list.sort();
    list.display();

    Stack s1;
    s1.push(1); s1.push(2); s1.push(3);
    s1.display();
    cout<<"popped value-"<<s1.pop()<<endl;
    s1.display();
}