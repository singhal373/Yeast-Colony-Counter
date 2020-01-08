import skimage
import skimage.feature
import skimage.viewer
import sys

# read command-line arguments
# filename = sys.argv[1]
# sigma = float(sys.argv[2])
# low_threshold = float(sys.argv[3])
# high_threshold = float(sys.argv[4])
sigma = 2.0
low_threshold = 0.1
high_threshold = 0.3

# load and display original image as grayscale
image = skimage.io.imread("image.jpg", as_gray=True)
viewer = skimage.viewer.ImageViewer(image)

viewer.show()

edges = skimage.feature.canny(
    image=image,
    sigma=sigma,
    low_threshold=low_threshold,
    high_threshold=high_threshold,
)


# display edges
viewer = skimage.viewer.ImageViewer(edges)
viewer.show()
