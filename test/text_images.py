import cv2
import numpy as np

from img_utils.images import put_text


def test_put_text():
    img = np.zeros((100, 100, 3), dtype=np.int32)
    put_text(img, 'OK', (10, 60), background_color=(0, 0, 255))
    cv2.imwrite('test_put_text.jpg', img)


if __name__ == '__main__':
    test_put_text()
