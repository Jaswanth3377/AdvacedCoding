int trap(int* height, int heightSize) {
    if (heightSize == 0) return 0;

    // Step 1: Create arrays for left max and right max
    int *left_max = (int*)malloc(sizeof(int) * heightSize);
    int *right_max = (int*)malloc(sizeof(int) * heightSize);

    // Step 2: Fill the left_max array
    left_max[0] = height[0];
    for (int i = 1; i < heightSize; i++) {
        left_max[i] = (height[i] > left_max[i - 1]) ? height[i] : left_max[i - 1];
    }

    // Step 3: Fill the right_max array
    right_max[heightSize - 1] = height[heightSize - 1];
    for (int i = heightSize - 2; i >= 0; i--) {
        right_max[i] = (height[i] > right_max[i + 1]) ? height[i] : right_max[i + 1];
    }

    // Step 4: Calculate the total trapped water
    int total_water = 0;
    for (int i = 0; i < heightSize; i++) {
        int water_at_i = (left_max[i] < right_max[i]) ? left_max[i] : right_max[i];
        if (water_at_i > height[i]) {
            total_water += water_at_i - height[i];
        }
    }

    // Free the allocated memory for the arrays
    free(left_max);
    free(right_max);

    return total_water;
}
