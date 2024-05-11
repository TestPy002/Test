#include<iostream>
using namespace std;
struct Node{
    int data;
    Node* left;
    Node* right;
    Node* parent;
    char color;
    Node(int data,int c='R'):data(data), left(nullptr), right(nullptr), parent(nullptr), color(c){}
};
class RedBlack{
    Node* root;
    void leftrotate(Node* node){
        Node* x = node->right;
        Node* y = node->parent;
        Node* z = x->left;
        x->left = node;
        node->right = z;
        x->parent=y;
        node->parent=x;
        if(z!=nullptr){
            z->parent = node;
        }
        if(y!=nullptr){
        if(x->data<y->data) y->left = x;
        else y->right = x;}
        else{
            root = x;
        }
    };
    void rightrotate(Node* node){
        Node* x = node->left;
        Node* y = node->parent;
        Node* z = x->right;
        x->right = node;
        node->left = z;
        x->parent=y;
        node->parent=x;
        if(z!=nullptr){
            z->parent = node;
        }
        if(y!=nullptr){
        if(x->data<y->data) y->left = x;
        else y->right = x;}
        else{
            root=x;
        }
    };
    public:
    RedBlack(){ root=nullptr; }
    void insert(int data);
    Node* deletenode(Node* node,int data);
    void remove(int data);
    void check(Node* node);
    void fix(Node* node);
    bool child(Node* node){
        if(node->left==nullptr && node->right==nullptr) return true;
        if(node->left==nullptr && node->right->color=='B') return true;
        if(node->right==nullptr && node->left->color=='B') return true;
        return false;
    }
    Node* finmin(Node* node){
    while(node->right!=nullptr) node = node->right;
    return node;
    }
    void print(Node* node){
        if(node->left!=nullptr) print(node->left);
        cout<<node->data<<" "<<node->color<<endl;
        if(node->right!=nullptr) print(node->right);
    }
    void print_tree(){
        Node* cur = root;
        if(cur==nullptr){
            return;
        }
        print(cur);
    }
};
void RedBlack::insert(int data){
    if(root==nullptr){
        Node* newNode= new Node(data,'B');
        root = newNode; return;
    }
    Node* cur = root;
    Node* prev = nullptr;
    while(cur!=nullptr){
        prev=cur;
        if(cur->data>data) cur = cur->left;
        else cur=cur->right;
    }
    Node* newNode = new Node(data);
    newNode->parent = prev;
    if(newNode->data<prev->data) prev->left = newNode;
    else prev->right = newNode;
    check(newNode);
}
void RedBlack::check(Node* node){
    if(node->parent->color=='B') return;
    else{
        if(node->parent->parent->left==node->parent){
            if(node->parent->parent->right!=nullptr && node->parent->parent->right->color=='R'){
                node->parent->color = 'B';
                node->parent->parent->right->color=='B';
                if(node->parent->parent==root) return;
                else{
                    node->parent->parent->color='R';
                    check(node->parent->parent);
                }
            }
            else{
                if(node->parent->parent->left==node->parent && node->parent->left==node){
                char tempColor = node->parent->color;
                node->parent->color = node->parent->parent->color;
                node->parent->parent->color = tempColor;
            rightrotate(node->parent->parent); //rightrotate(node->parent);
            }
            else if(node->parent->parent->right==node->parent && node->parent->right==node) {
            char tempColor = node->parent->color;
                node->parent->color = node->parent->parent->color;
                node->parent->parent->color = tempColor;
                leftrotate(node->parent->parent); //leftrotate(node->parent);
            }
            else if(node->parent->parent->left == node->parent && node->parent->right == node){
                char tempColor = node->color;
                node->color = node->parent->parent->color;
                node->parent->parent->color = tempColor;
                leftrotate(node->parent);
                rightrotate(node->parent);
            }
            else {
                char tempColor = node->color;
                node->color = node->parent->parent->color;
                node->parent->parent->color = tempColor;
                rightrotate(node->parent); 
                leftrotate(node->parent);
            }
            }
        }
        else{
            //if(node->parent->parent->left!=nullptr)
                //cout<<node->data<<node->color<<" "<<node->parent->parent->left->data<<node->parent->parent->color<<" iop"<<endl;
            if(node->parent->parent->left!=nullptr && node->parent->parent->left->color=='R'){
                node->parent->color = 'B';
                node->parent->parent->left->color='B';
                if(node->parent->parent==root) return;
                else{
                    node->parent->parent->color='R';
                    check(node->parent->parent);
                }
            }
            else{
            //cout<<"ko";
            
                if(node->parent->parent->left==node->parent && node->parent->left==node){
                    char tempColor = node->parent->color;
                node->parent->color = node->parent->parent->color;
                node->parent->parent->color = tempColor;
            rightrotate(node->parent->parent); //rightrotate(node->parent);
            }
            else if(node->parent->parent->right==node->parent && node->parent->right==node) {
                char tempColor = node->parent->color;
                node->parent->color = node->parent->parent->color;
                node->parent->parent->color = tempColor;
                leftrotate(node->parent->parent); //leftrotate(node->parent);
                //cout<<node->data;
            }
            else if(node->parent->parent->left == node->parent && node->parent->right == node){
                //node->parent->color='R';
                char tempColor = node->color;
                node->color = node->parent->parent->color;
                node->parent->parent->color = tempColor;
                leftrotate(node->parent);
                rightrotate(node->parent);
            }
            else {
                //cout<<node->parent->parent->data<<node->parent->parent->color<<endl;
            char tempColor = node->color;
                node->color = node->parent->parent->color;
                node->parent->parent->color = tempColor;
                rightrotate(node->parent); 
                leftrotate(node->parent);
                //cout<<node->left->data<<endl;
            }
            }
        }
    }
};
Node* RedBlack::deletenode(Node* node,int value){
    if(node==nullptr) return node;
    if(node->data>value){
        //cout<<node->data<<endl;
        node->left=deletenode(node->left,value);
    }
    else if(node->data<value){
        node->right=deletenode(node->right,value);
    }
    else{
        if(node->left==nullptr && node->right==nullptr){
            Node *temp=node;
            if(temp->color=='B') temp->color='D';
            cout<<temp->color;
            fix(temp);
            delete temp;
            return nullptr;
            }
        else if(node->left==nullptr){
            node->data = node->right->data;
            node->right = deletenode(node->right, node->data);
            return node;
        }
        else if(node->right==nullptr){
            node->data = node->left->data;
            node->left = deletenode(node->left, node->data);
            return node;
        }
        else{
            node->data = finmin(node->left)->data ;  
            node->left = deletenode(node->left , node->data);
            return node; 
        }
    }
    return node;
};
void RedBlack::remove(int data){
    root=deletenode(root,data);
};
void RedBlack::fix(Node* node){
    int i;
    if(node->color=='R') return;
    if(node->color=='D'){
        Node* sibling=nullptr;
        if(node->parent->left==node){
            sibling = node->parent->right;
            //Node* near= node->parent->right->
            i=0; //left is near child
            }
            else{
            sibling = node->parent->left; i=1; //right is near child
            }
            //cout<<i;
        if(sibling!=nullptr && sibling->color=='R'){
            node->parent->color='R';
            sibling->color = 'B';
            if(node->parent->left==node){
            leftrotate(node->parent);
            }
            else rightrotate(node->parent);
            fix(node);
        }
        else if(sibling==nullptr){
            node->color='B';
                sibling->color='R';
                if(node->parent->color=='R'){
                    node->parent->color='B'; return;
                }
                else{
                    node->parent->color='D';
                    fix(node->parent);
                }
        }
        else if(sibling->color=='B'){
            if(child(sibling)){
                node->color='B';
                sibling->color='R';
                if(node->parent->color=='R'){
                    node->parent->color='B'; return;
                }
                else{
                    node->parent->color='D';
                    fix(node->parent);
                }
            }
            else if(i==0){
                if(sibling->right!=nullptr && sibling->right->color=='R'){
                    cout<<node->data<<" "<<sibling->data<<endl; cout<<i;
                    char c= node->parent->color;
                    sibling->right->color='B';
                    node->parent->color = sibling->color;
                    sibling->color=c;
                    leftrotate(node->parent);
                    cout<<node->parent->parent->right->color;
                    return;
                }
                else{
                    char c= sibling->color;
                    sibling->color = sibling->left->color;
                    sibling->color=c;
                    rightrotate(sibling);
                    fix(node);
                }
            }
            else{
                if(sibling->left!=nullptr && sibling->left->color=='R'){
                    char c= node->parent->color;
                    node->parent->color = sibling->color;
                    sibling->color=c;
                    rightrotate(node->parent);
                    sibling->left->color='B';
                    return;
                }
                else{
                    char c= sibling->color;
                    sibling->color = sibling->left->color;
                    sibling->color=c;
                    leftrotate(sibling);
                    fix(node);
                }
            }
        }
    }

}
int main(){
    RedBlack tree;
    tree.insert(10);
    tree.insert(18);
    tree.insert(7);
    tree.insert(15);
    tree.insert(16);
    tree.insert(30);
    tree.insert(25);
    tree.insert(40);
    tree.insert(60);
    tree.insert(2);
    tree.insert(1);
    tree.insert(70);
    tree.remove(70);
    tree.remove(40);
    tree.remove(25);
    //tree.remove(30);
    tree.print_tree();
}