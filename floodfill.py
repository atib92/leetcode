""" 
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:
1. Begin with the starting pixel and change its color to color.
2. Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
3. Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
4. The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.
"""
from collections import deque
from copy import deepcopy
class Solution:
    """ This is a standard BFS. At every step we enqueue connected pixels. 
        During the dequeu operation, if a pixel is detected to have the
        original color, its color is changed and its own connected pixels
        are further enqueued.
        Note: We do not need to mark pixels as visited. Since we change the
        pixel color after dequing and check color before enqueing more pixels,
        an already visited pixel is already colored and won't get enqueued again !
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        pixels = deque()
        orig_color = image[sr][sc]
        if orig_color == color:
            return image
        pixels.append((sr, sc))
        while(len(pixels) > 0):
            pixel = pixels.popleft()
            sr, sc = pixel[0], pixel[1]
            if image[sr][sc] == orig_color:
                image[sr][sc] = color
                directions = [(-1,0), (0,-1), (+1,0), (0,+1)]
                for r, c in directions:
                    row, col = sr + r, sc + c
                    if (0 <= row < R) and (0 <= col < C):
                        if image[row][col] == orig_color:
                            pixels.append((row, col))
        return image
