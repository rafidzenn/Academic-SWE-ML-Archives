#include <iostream>
using namespace std;

// Node structure for the Binary Search Tree
struct Node {
    int data;
    Node* left;
    Node* right;
    
    Node(int val) {
        data = val;
        left = NULL;
        right = NULL;
    }
};

class BST {
private:
    Node* root;

    Node* insertRecursive(Node* node, int val) {
        if (node == NULL) {
            return new Node(val);
        }
        if (val < node->data) {
            node->left = insertRecursive(node->left, val);
        } else if (val > node->data) {
            node->right = insertRecursive(node->right, val);
        }
        return node;
    }

    void inorderRecursive(Node* node) {
        if (node != NULL) {
            inorderRecursive(node->left);
            cout << node->data << " ";
            inorderRecursive(node->right);
        }
    }

public:
    BST() { root = NULL; }

    void insert(int val) {
        root = insertRecursive(root, val);
    }

    void displayInorder() {
        inorderRecursive(root);
        cout << endl;
    }
};

int main() {
    BST tree;
    cout << "Inserting elements into the BST..." << endl;
    tree.insert(50);
    tree.insert(30);
    tree.insert(20);
    tree.insert(40);
    tree.insert(70);
    tree.insert(60);
    tree.insert(80);

    cout << "Inorder Traversal (Sorted Output): ";
    tree.displayInorder();

    return 0;
}
