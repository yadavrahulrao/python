#include <stdio.h>
#include <stdbool.h>

#define P 5  // Number of processes
#define R 3  // Number of resources

// Function to check if a process can finish
bool isSafeState(int avail[], int max[][R], int allot[][R], int need[][R], int safeSeq[]) {
    int work[R], finish[P] = {0};
    int count = 0;

    // Initialize work array to the available resources
    for (int i = 0; i < R; i++) {
        work[i] = avail[i];
    }

    // Check if the system is in a safe state
    while (count < P) {
        bool found = false;

        for (int i = 0; i < P; i++) {
            if (!finish[i]) {
                // Check if process can be executed
                int j;
                for (j = 0; j < R; j++) {
                    if (need[i][j] > work[j]) {
                        break;
                    }
                }

                // If all needs can be satisfied
                if (j == R) {
                    for (int k = 0; k < R; k++) {
                        work[k] += allot[i][k];  // Allocate resources back
                    }
                    safeSeq[count++] = i;
                    finish[i] = 1;
                    found = true;
                }
            }
        }

        if (!found) {
            return false;  // If no process can proceed, the system is not in a safe state
        }
    }
    return true;  // If all processes can be finished
}

// Function to request resources
bool requestResources(int pid, int request[], int avail[], int max[][R], int allot[][R], int need[][R], int safeSeq[]) {
    // Check if the request is valid
    for (int i = 0; i < R; i++) {
        if (request[i] > need[pid][i]) {
            printf("Error: Process has exceeded its maximum claim.\n");
            return false;
        }
        if (request[i] > avail[i]) {
            printf("Resources are not available.\n");
            return false;
        }
    }

    // Pretend to allocate the requested resources
    for (int i = 0; i < R; i++) {
        avail[i] -= request[i];
        allot[pid][i] += request[i];
        need[pid][i] -= request[i];
    }

    // Check if the system is still in a safe state and print the safe sequence if granted
    if (isSafeState(avail, max, allot, need, safeSeq)) {
        printf("Request granted.\n");
        printf("Safe Sequence is: ");
        for (int i = 0; i < P; i++) {
            printf("P%d ", safeSeq[i]);
        }
        printf("\n");
        return true;
    } else {
        // Rollback the allocation (undo the request)
        for (int i = 0; i < R; i++) {
            avail[i] += request[i];
            allot[pid][i] -= request[i];
            need[pid][i] += request[i];
        }
        printf("Request denied. System would be in an unsafe state.\n");
        return false;
    }
}

int main() {
    // Process IDs
    int processes[] = {0, 1, 2, 3, 4};  

    // Available resources
    int avail[] = {3, 3, 2};  

    // Maximum resources needed by each process
    int max[][R] = {
        {7, 5, 3},
        {3, 2, 2},
        {9, 0, 2},
        {2, 2, 2},
        {4, 3, 3}
    };

    // Resources allocated to each process
    int allot[][R] = {
        {0, 1, 0},
        {2, 0, 0},
        {3, 0, 2},
        {2, 1, 1},
        {0, 0, 2}
    };

    // Resources needed by each process
    int need[P][R];
    for (int i = 0; i < P; i++) {
        for (int j = 0; j < R; j++) {
            need[i][j] = max[i][j] - allot[i][j];
        }
    }

    // Request example (process 1 requesting 1 unit of resource 0, 0 units of resource 1, and 2 units of resource 2)
    int request[] = {1, 0, 2};

    // Request resources for process 1
    int pid = 1;
    int safeSeq[P];  // Array to hold the safe sequence
    requestResources(pid, request, avail, max, allot, need, safeSeq);

    return 0;
}

