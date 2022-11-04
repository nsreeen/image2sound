import cv2
from matplotlib import pyplot

from blob import Blob

def process_image(image_file_name):
    image = cv2.imread(image_file_name)
    small = cv2.resize(image, (0,0), fx=0.1, fy=0.1)
    blurred = cv2.GaussianBlur(small,(7,7),cv2.BORDER_DEFAULT)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    threshold, black_and_white_image = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    num_labels, labelled_image, label_stats, centroids = cv2.connectedComponentsWithStats(black_and_white_image, 2, cv2.CV_32S)

    blobs = []
    for l,c in zip(label_stats[1:], centroids[1:]):
        blob = Blob(x=l[cv2.CC_STAT_LEFT],
                    y=l[cv2.CC_STAT_TOP],
                    width=l[cv2.CC_STAT_WIDTH],
                    height=l[cv2.CC_STAT_HEIGHT],
                    area=l[cv2.CC_STAT_AREA],
                    density=int(l[cv2.CC_STAT_AREA]/l[cv2.CC_STAT_WIDTH]),
                    center_x=int(c[0]),
                    center_y=int(c[1]))
        blobs.append(blob)

    return image, labelled_image, blobs
