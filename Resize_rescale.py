import cv2 as cv
#resize height & width of given frames or photos
def rescaleFrame(frame, scalewidth = .75, scalehight = .75):
    width = int(frame.shape[1] * scalewidth)
    height = int(frame.shape[0] * scalehight)
    dimensions = (width,height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
