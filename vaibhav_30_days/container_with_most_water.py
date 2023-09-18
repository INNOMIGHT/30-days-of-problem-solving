def container_with_most_water(height: list) -> int:

    l_ptr = 0
    r_ptr = len(height) - 1

    max_area = 0

    while l_ptr != r_ptr:
        curr_area = min(height[l_ptr], height[r_ptr]) * (r_ptr-l_ptr)
        if height[l_ptr] < height[r_ptr]:
            l_ptr += 1
        else:
            r_ptr -= 1

        max_area = max(curr_area, max_area)

    return max_area


print(container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
