import numpy as np

def generate_synthetic_images(num_images=10, size=28):
    """Generates artificial synthetic pixel matrices simulating basic geometric shapes."""
    np.random.seed(7)
    images = np.random.randint(0, 50, (num_images, size, size))
    # Draw a distinct bright line artifact (simulating an edge structural pattern)
    for img in images:
        img[10:18, 12:16] = 255
    return images

def apply_sobel_edge_detection(image):
    """Applies basic mathematical convolution primitives natively in NumPy."""
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    Ky = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    
    height, width = image.shape
    edge_matrix = np.zeros((height-2, width-2))
    
    for i in range(height-2):
        for j in range(width-2):
            region = image[i:i+3, j:j+3]
            Gx = np.sum(region * Kx)
            Gy = np.sum(region * Ky)
            edge_matrix[i, j] = np.sqrt(Gx**2 + Gy**2)
            
    return edge_matrix
