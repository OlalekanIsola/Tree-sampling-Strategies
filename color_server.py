import rospy, cv2, cv_bridge
import numpy as np
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist


class ColorDetect:
        def __init__(self):
                self.bridge = cv_bridge.CvBridge()
                self.image_sub = rospy.Subscriber('camera/rgb/image_raw',Image, self.image_callback)
                # self.image_sub = rospy.Subscriber('raspicam_node/image', Image, self.image_callback)


        def image_callback(self, data):
                cv_image = self.bridge.imgmsg_to_cv2(data,desired_encoding='bgr8')
                # convert from RGB to HSV
                hsv = cv2.cvtColor(cv_image, cv2.COLOR_BGR2HSV)
                #This is for the red RGB [255,0,0] and HSV = [0,100,100]
                # lower_red = np.array([0,50,50])
                # upper_red = np.array([10,255,255])

                lower_red = np.array([0,10,120])
                upper_red = np.array([15,255,255])

                # remove all the things i dont need and the things i dont need
                mask = cv2.inRange(hsv, lower_red, upper_red)

                height, width, channels = cv_image.shape
                # calculates the centroid of the blob of binary image using ImageMoments

                M = cv2.moments(mask)
                if M['m00'] > 0:
                        cx = int(M['m10']/M['m00'])
                        cy = int(M['m01']/M['m00'])
                        IsRed = True
                else:
                        IsRed = False

                print(IsRed)
                rospy.set_param('is_red', IsRed)

rospy.init_node('line_follower')
follower = ColorDetect()
rospy.spin()