import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

class RecursivePatternGenerator:
    def __init__(self, size=512):
        self.size = size
        self.terrain_grid = None
        self.dimension_D = 0
        self.artifacts = []
        self.dense_regions = []

    def generate_terrain(self, roughness=1.0):
        self.terrain_grid = np.zeros((self.size, self.size))
        
        def divide_and_displace(x, y, w, h, noise_scale):
            if w <= 1 or h <= 1:
                return
            
            mx, my = x + w // 2, y + h // 2
            
            displacement = random.uniform(-1, 1) * noise_scale
            self.terrain_grid[my, mx] += displacement
            
            new_scale = noise_scale * 0.5
            divide_and_displace(x, y, w // 2, h // 2, new_scale)
            divide_and_displace(mx, y, w // 2, h // 2, new_scale)
            divide_and_displace(x, my, w // 2, h // 2, new_scale)
            divide_and_displace(mx, my, w // 2, h // 2, new_scale)

        divide_and_displace(0, 0, self.size, self.size, noise_scale=roughness * 100)
        self.terrain_grid = np.abs(self.terrain_grid) 
        print("1. Terrain Generated.")

    def measure_fractal_dimension(self):
        if self.terrain_grid is None:
            return
        
        threshold_val = np.mean(self.terrain_grid)
        binary_terrain = self.terrain_grid > threshold_val
        
        box_sizes = [2, 4, 8, 16, 32, 64]
        counts = []
        
        for size in box_sizes:
            count = 0
            for y in range(0, self.size, size):
                for x in range(0, self.size, size):
                    if np.any(binary_terrain[y:y+size, x:x+size]):
                        count += 1
            counts.append(count)
            
        x_vals = np.log(1.0 / np.array(box_sizes))
        y_vals = np.log(np.array(counts))
        slope = np.polyfit(x_vals, y_vals, 1)[0]
        self.dimension_D = slope
        
        print(f"2. Fractal Dimension measured: D = {self.dimension_D:.3f}")
        if self.dimension_D < 1.8 or self.dimension_D > 2.5:
            print("   [WARNING] Unnatural fractal dimension detected!")

    def find_dense_regions(self, min_size=32, density_threshold=0.6):
        self.dense_regions = []
        threshold_val = np.percentile(self.terrain_grid, 80)
        binary_points = self.terrain_grid > threshold_val
        
        def split_region(x, y, w, h):
            if w <= min_size or h <= min_size:
                return
            
            region = binary_points[y:y+h, x:x+w]
            density = np.sum(region) / (w * h)
            
            if density > density_threshold:
                self.dense_regions.append((x, y, w, h))
            else:
                hw, hh = w // 2, h // 2
                split_region(x, y, hw, hh)
                split_region(x + hw, y, hw, hh)
                split_region(x, y + hh, hw, hh)
                split_region(x + hw, y + hh, hw, hh)
                
        split_region(0, 0, self.size, self.size)
        print(f"3. Split View: Found {len(self.dense_regions)} dense regions.")

    def detect_artifacts(self, threshold=15):
        self.artifacts = []
        
        dy = np.abs(np.diff(self.terrain_grid, axis=0))
        dx = np.abs(np.diff(self.terrain_grid, axis=1))
        
        for y in range(self.size - 1):
            for x in range(self.size - 1):
                if dy[y, x] > threshold or dx[y, x] > threshold:
                    self.artifacts.append((x, y))
                    
        print(f"4. Artifacts Detected: Found {len(self.artifacts)} suspicious points.")

    def show_dashboard(self):
        fig, axes = plt.subplots(1, 3, figsize=(15, 5))
        
        ax1 = axes[0]
        im = ax1.imshow(self.terrain_grid, cmap='terrain')
        ax1.set_title(f"1. Generate Terrain\n(Dimension: {self.dimension_D:.2f})")
        fig.colorbar(im, ax=ax1, shrink=0.5)
        
        ax2 = axes[1]
        ax2.imshow(self.terrain_grid, cmap='terrain', alpha=0.5)
        for (x, y, w, h) in self.dense_regions:
            rect = patches.Rectangle((x, y), w, h, linewidth=1.5, edgecolor='red', facecolor='none')
            ax2.add_patch(rect)
        ax2.set_title("2. Split View\n(Red boxes = Dense Peaks)")
        
        ax3 = axes[2]
        ax3.imshow(self.terrain_grid, cmap='terrain', alpha=0.5)
        if self.artifacts:
            arts_x = [p[0] for p in self.artifacts]
            arts_y = [p[1] for p in self.artifacts]
            ax3.scatter(arts_x, arts_y, color='magenta', s=5, label='Artifacts')
            ax3.legend()
        ax3.set_title("3. Find Artifacts\n(Unnatural changes)")

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    app = RecursivePatternGenerator(size=512)
    app.generate_terrain(roughness=1.2)
    app.measure_fractal_dimension()
    app.find_dense_regions(min_size=16, density_threshold=0.5)
    app.detect_artifacts(threshold=20.0)
    app.show_dashboard()