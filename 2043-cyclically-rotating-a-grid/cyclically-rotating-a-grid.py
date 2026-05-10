class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m,n)//2
        for layer in range(layers):
            arr = []
            for c in range(layer, n-layer):
                arr.append(grid[layer][c])
            for r in range(layer+1, m-layer-1):
                arr.append(grid[r][n-layer-1])
            for c in range(n-layer-1, layer-1,-1):
                arr.append(grid[m-layer-1][c])
            for r in range(m-layer-2, layer, -1):
                arr.append(grid[r][layer])

            shift = k % len(arr)
            arr = arr[shift:] + arr[:shift]
            idx = 0

            for c in range(layer, n-layer):
                grid[layer][c] = arr[idx]
                idx += 1
            for r in range(layer+1, m-layer-1):
                grid[r][n-layer-1] = arr[idx]
                idx += 1
            for c in range(n-layer-1, layer-1,-1):
                grid[m-layer-1][c] = arr[idx]
                idx += 1
            for r in range(m-layer-2, layer, -1):
                grid[r][layer] = arr[idx]
                idx += 1
        return grid
