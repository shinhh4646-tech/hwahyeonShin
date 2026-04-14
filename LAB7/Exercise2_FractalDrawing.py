import matplotlib.pyplot as plt
import numpy as np
import math

def draw_sierpinski(ax, x, y, size, depth):
    height = size * math.sqrt(3) / 2.0
    
    if depth == 0:
        triangle = plt.Polygon([
            [x, y], 
            [x + size, y], 
            [x + size / 2, y + height]
        ], edgecolor='black', facecolor='black')
        ax.add_patch(triangle)
    else:
        half_size = size / 2.0
        half_height = height / 2.0
        
        draw_sierpinski(ax, x, y, half_size, depth - 1)
        draw_sierpinski(ax, x + half_size, y, half_size, depth - 1)
        draw_sierpinski(ax, x + half_size / 2, y + half_height, half_size, depth - 1)

def draw_tree(ax, x, y, length, angle, depth):
    rad = math.radians(angle)
    nx = x + length * math.cos(rad)
    ny = y + length * math.sin(rad)
    
    ax.plot([x, nx], [y, ny], color='green', lw=max(1, depth))
    
    if depth > 0:
        new_length = length * 0.7
        
        draw_tree(ax, nx, ny, new_length, angle + 30, depth - 1)
        draw_tree(ax, nx, ny, new_length, angle - 30, depth - 1)

def fractal_dimension(fractal_image, box_sizes):
    counts = []
    
    img_height, img_width = fractal_image.shape
    
    for size in box_sizes:
        count = 0
        for y in range(0, img_height, size):
            for x in range(0, img_width, size):
                box = fractal_image[y : y + size, x : x + size]
                if np.any(box):
                    count += 1
        counts.append(count)
    
    x_vals = np.log(1.0 / np.array(box_sizes))
    y_vals = np.log(np.array(counts))
    
    coefficients = np.polyfit(x_vals, y_vals, 1)
    slope = coefficients[0]
    
    return slope

if __name__ == "__main__":
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    
    ax1 = axes[0]
    ax1.set_aspect('equal')
    ax1.set_title("Sierpinski Triangle (Depth 4)")
    draw_sierpinski(ax1, 0, 0, 100, 4)
    ax1.autoscale_view()
    
    ax2 = axes[1]
    ax2.set_aspect('equal')
    ax2.set_title("Fractal Tree (Depth 6)")
    draw_tree(ax2, 0, 0, 100, 90, 6)
    
    plt.tight_layout()
    plt.show()
    
    test_image = np.zeros((128, 128))
    test_image[64, :] = 1
    
    sizes = [2, 4, 8, 16, 32]
    dimension = fractal_dimension(test_image, sizes)
    print(f"Test Image (Straight Line) Fractal Dimension: {dimension:.2f}")