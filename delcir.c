#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* deleteFirstNode(struct Node* last) {
    if (last == NULL) {
        // If the list is empty
        printf("List is empty\n");
        return NULL;
    }

    struct Node* head = last->next;

    if (head == last) {
        // If there is only one node in the list
        free(head);
        last = NULL;
    } else {
        // More than one node in the list
        last->next = head->next;
        free(head);
    }

    return last;
}

void printList(struct Node* last) {
    if (last == NULL) return;

    struct Node* head = last->next;
    while (1) {
        printf("%d ", head->data);
        head = head->next;
        if (head == last->next) break;
    }
    printf("\n");
}

struct Node* createNode(int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = NULL;
    return newNode;
}

int main() {
    struct Node* first = createNode(2);
    first->next = createNode(3);
    first->next->next = createNode(4);

    struct Node* last = first->next->next;
    last->next = first;

    printf("Original list: ");
    printList(last);

    last = deleteFirstNode(last);

    printf("List after deleting first node: ");
    printList(last);

    return 0;
}

