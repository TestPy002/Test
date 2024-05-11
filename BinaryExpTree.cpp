#include <iostream>
#include <stack>
#include <string>
#include <cctype>

using namespace std;

// Node structure for binary expression tree
struct Node {
    char data;
    Node* left;
    Node* right;

    Node(char val) : data(val), left(nullptr), right(nullptr) {}
};

class ExpressionTree {
private:
    Node* root;

    // Utility function to check if character is an operator
    bool isOperator(char c) {
        return c == '+' || c == '-' || c == '*' || c == '/';
    }

    // Utility function to create a new node
    Node* createNode(char val) {
        return new Node(val);
    }

public:
    // Constructor
    ExpressionTree() : root(nullptr) {}

    // Function to build binary expression tree from postfix expression
    void buildTree(string postfix) {
        stack<Node*> s;

        for (char c : postfix) {
            if (isalnum(c)) { // Operand
                s.push(createNode(c));
            } else if (isOperator(c)) { // Operator
                Node* newNode = createNode(c);
                newNode->right = s.top(); s.pop();
                newNode->left = s.top(); s.pop();
                s.push(newNode);
            }
        }
        root = s.top(); s.pop();
    }

    int evaluate(Node* node) {
        if (!node) return 0;

        if (isdigit(node->data)) {
            return node->data - '0';
        }

        int leftVal = evaluate(node->left);
        int rightVal = evaluate(node->right);

        switch (node->data) {
            case '+': return leftVal + rightVal;
            case '-': return leftVal - rightVal;
            case '*': return leftVal * rightVal;
            case '/': return leftVal / rightVal;
            default: return 0; // Invalid operator
        }
    }

    // Function to evaluate the expression
    int evaluateExpression() {
        return evaluate(root);
    }

    // Function for inorder traversal (used for printing infix expression)
    void inorderTraversal(Node* node) {
        if (!node) return;
        inorderTraversal(node->left);
        cout << node->data << " ";
        inorderTraversal(node->right);
    }

    // Function to print infix expression
    void printInfixExpression() {
        inorderTraversal(root);
    }
};

int main() {
    // Example: Evaluate the postfix expression "3 4 * 5 +"
    ExpressionTree expTree;
    expTree.buildTree("34*5+");
    cout << "Infix Expression: ";
    expTree.printInfixExpression(); // Output: "3 * 4 + 5"
    cout << endl;
    cout << "Result: " << expTree.evaluateExpression(); // Output: 17
    cout << endl;
    return 0;
}
