#include <iostream>
#include <vector>

using namespace std;

class MinHeap {
private:
    vector<int> heap;

    // Utility function to maintain heap property by swapping nodes upward
    void heapifyUp(int index) {
        while (index > 0 && heap[parent(index)] > heap[index]) {
            swap(heap[index], heap[parent(index)]);
            index = parent(index);
        }
    }

    // Utility function to maintain heap property by swapping nodes downward
    void heapifyDown(int index) {
        int smallest = index;
        int left = leftChild(index);
        int right = rightChild(index);

        if (left < heap.size() && heap[left] < heap[smallest]) {
            smallest = left;
        }

        if (right < heap.size() && heap[right] < heap[smallest]) {
            smallest = right;
        }

        if (smallest != index) {
            swap(heap[index], heap[smallest]);
            heapifyDown(smallest);
        }
    }

public:
    // Constructor
    MinHeap() {}

    // Utility functions to get parent, left child, and right child indices
    int parent(int index) { return (index) / 2; }
    int leftChild(int index) { return 2 * index + 1; }
    int rightChild(int index) { return 2 * index + 2; }

    // Function to insert a new element into the heap
    void insert(int value) {
        heap.push_back(value);
        heapifyUp(heap.size() - 1);
    }

    // Function to extract the minimum element from the heap
    int extractMin() {
        if (heap.empty()) {
            throw runtime_error("Heap is empty");
        }

        int minVal = heap.front();
        heap[0] = heap.back();
        heap.pop_back();
        heapifyDown(0);
        return minVal;
    }

    // Function to get the minimum element from the heap without removing it
    int peek() {
        if (heap.empty()) {
            throw runtime_error("Heap is empty");
        }
        return heap.front();
    }

    // Function to check if the heap is empty
    bool isEmpty() {
        return heap.empty();
    }
};

int main() {
    MinHeap minHeap;

    // Insert elements into the heap
    minHeap.insert(5);
    minHeap.insert(3);
    minHeap.insert(8);
    minHeap.insert(2);
    minHeap.insert(4);
    minHeap.insert(6);
    minHeap.insert(1);

    // Extract and print the minimum element
    cout << "Min element: " << minHeap.extractMin() << endl;

    // Peek the minimum element without removing it
    cout << "Min element after extraction: " << minHeap.peek() << endl;

    return 0;
}
