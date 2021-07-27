# flood fill algo

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        n, m = len(image), len(image[0]) # taking the dimensions
        vis = [[False for _ in range(m)] for _ in range(n)]

        oldColor = image[sr][sc]
        def fill(row, col, image):
            # if the pixel is inside the image or not
            if row < 0 or col < 0 or row >= n or col >= m: return
            
            # if the pixel is already visited or the color of the pixel is different from the origianal color
            if vis[row][col] or image[row][col] != oldColor: return

            # the current pixel is visited and updated the color of the pixel
            vis[row][col] = True
            image[row][col] = newColor
            
            # moving the direction to find the same adjacent colors
            fill(row + 1, col, image)
            fill(row - 1, col, image)
            fill(row, col + 1, image)
            fill(row, col - 1, image)
        
        fill(sr, sc, image)
        return image

