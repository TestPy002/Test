#include <iostream>
using namespace std;
class AVLNode {
public:
    int data;
    AVLNode* left;
    AVLNode* right;
    int height;

    AVLNode(int value) : data(value), left(nullptr), right(nullptr), height(1) {}
};

class AVLTree {
private:
    AVLNode* root;

    // Helper function to calculate height of a node
    int getHeight(AVLNode* node) {
        if (node == nullptr) return 0;
        return node->height;
    }

    // Helper function to get balance factor of a node
    int getBalanceFactor(AVLNode* node) {
        if (node == nullptr) return 0;
        return getHeight(node->left) - getHeight(node->right);
    }

    // Perform right rotation
    AVLNode* rightRotate(AVLNode* y) {
        AVLNode* x = y->left;
        AVLNode* T2 = x->right;

        x->right = y;
        y->left = T2;

        // Update heights
        y->height = 1 + max(getHeight(y->left), getHeight(y->right));
        x->height = 1 + max(getHeight(x->left), getHeight(x->right));

        return x;
    }

    // Perform left rotation
    AVLNode* leftRotate(AVLNode* x) {
        AVLNode* y = x->right;
        AVLNode* T2 = y->left;

        y->left = x;
        x->right = T2;

        // Update heights
        x->height = 1 + max(getHeight(x->left), getHeight(x->right));
        y->height = 1 + max(getHeight(y->left), getHeight(y->right));

        return y;
    }

public:
    AVLTree() : root(nullptr) {}

    // Insert a new node into the AVL tree
    AVLNode* insert(AVLNode* node, int value) {
        // Perform standard BST insertion
        if (node == nullptr) return new AVLNode(value);

        if (value < node->data) {
            node->left = insert(node->left, value);
        } else if (value > node->data) {
            node->right = insert(node->right, value);
        } else {
            // Duplicate values are not allowed in AVL tree
            return node;
        }

        // Update height of the current node
        node->height = 1 + max(getHeight(node->left), getHeight(node->right));

        // Get balance factor to check if node is unbalanced
        int balance = getBalanceFactor(node);

        // Perform rotations if necessary to restore balance
        if (balance > 1 && value < node->left->data) {
            return rightRotate(node);
        }
        if (balance < -1 && value > node->right->data) {
            return leftRotate(node);
        }
        if (balance > 1 && value > node->left->data) {
            node->left = leftRotate(node->left);
            return rightRotate(node);
        }
        if (balance < -1 && value < node->right->data) {
            node->right = rightRotate(node->right);
            return leftRotate(node);
        }

        return node;
    }

    // Helper function to insert a value into the AVL tree
    void insert(int value) {
        root = insert(root, value);
    }

    // Function to perform inorder traversal of the AVL tree
    void inorderTraversal(AVLNode* node) {
        if (node != nullptr) {
            inorderTraversal(node->left);
            cout << node->data << " ";
            inorderTraversal(node->right);
        }
    }

    // Wrapper function to perform inorder traversal of the AVL tree
    void inorderTraversal() {
        inorderTraversal(root);
    }
    void deletion(int value);
    AVLNode* deletenode(AVLNode* node,int value);
    AVLNode* finmin(AVLNode* node);
};
void AVLTree::deletion(int value){
    root= deletenode(root,value);
}
AVLNode* AVLTree::deletenode(AVLNode* node,int value){
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
            AVLNode *temp=node;
            delete temp;
            return nullptr;
            }
        else if(node->left==nullptr){
            AVLNode *temp=node;
            delete temp;
            return node->right;
        }
        else if(node->right==nullptr){
            AVLNode *temp=node;
            delete temp;
            return node->left;
        }
        else{
            node->data = finmin(node->right)->data ;  
            node->right = deletenode(node->right , node->data);
            return node; 
        }
    }
    node->height = 1 + max(getHeight(node->left),getHeight(node->right));
    int balance = getBalanceFactor(node);
        // Perform rotations if necessary to restore balance
        if (balance > 1 && value < node->left->data) {
            return rightRotate(node);
        }
        if (balance < -1 && value > node->right->data) {
            return leftRotate(node);
        }
        if (balance > 1 && value > node->left->data) {
            node->left = leftRotate(node->left);
            return rightRotate(node);
        }
        if (balance < -1 && value < node->right->data) {
            node->right = rightRotate(node->right);
            return leftRotate(node);
        }
        return node;
}
AVLNode* AVLTree::finmin(AVLNode* node){
    while(node->left!=nullptr) node = node->left;
    return node;
}
int main() {
    AVLTree avlTree;
    avlTree.insert(10);
    avlTree.insert(20);
    avlTree.insert(30);
    avlTree.insert(40);
    avlTree.insert(50);
    avlTree.insert(25);

    cout << "Inorder traversal of AVL tree: ";
    avlTree.inorderTraversal();
    cout<<endl;

    avlTree.deletion(30);
    cout << "Inorder traversal of AVL tree: ";
    avlTree.inorderTraversal();
    cout<<endl;
    return 0;
}
