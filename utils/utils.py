import numpy as np
from PIL import Image
from sklearn.cluster import KMeans


def extract_main_colors(image_path, n_colors):
    # Load the image
    image = Image.open(image_path)

    # Convert the image data to a NumPy array
    image_np = np.array(image)

    # Reshape the data to 2D (just RGB, ignore the position of the pixel)
    pixels = image_np.reshape(-1, 3)

    # Perform clustering to form n clusters
    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(pixels)

    # Get the RGB values of the cluster centers
    colors = kmeans.cluster_centers_

    # Convert each color to integer values
    colors = colors.round(0).astype(int)

    return colors


def extract_main_colors_rgb(image_path, n_colors):
    # Load the image
    image = Image.open(image_path)

    # Convert the image data to a NumPy array
    image_np = np.array(image)

    # Reshape the data to 2D (just RGB, ignore the position of the pixel)
    pixels = image_np.reshape(-1, 3)

    # Perform clustering to form n clusters
    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(pixels)

    # Get the RGB values of the cluster centers
    colors = kmeans.cluster_centers_

    # Convert each color to integer values and then to list
    colors = [list(map(int, color)) for color in colors.round(0)]

    return colors


def normalize_data(df):
    df_numeric = df.select_dtypes(include=[np.number])
    df_normalized = (df_numeric - df_numeric.min()) / (df_numeric.max() - df_numeric.min())
    return df_normalized
