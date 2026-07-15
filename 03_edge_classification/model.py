import numpy as np
from image_processor import generate_synthetic_images, apply_sobel_edge_detection

def main():
    print("Simulating computer vision feature engineering extraction...")
    raw_images = generate_synthetic_images()
    
    processed_features = []
    for idx, img in enumerate(raw_images):
        edges = apply_sobel_edge_detection(img)
        mean_intensity = np.mean(edges)
        processed_features.append(mean_intensity)
        
    print(f"Successfully processed {len(processed_features)} structural feature maps.")
    print(f"Sample analytical mean tensor output: {processed_features[:3]}")

if __name__ == "__main__":
    main()
