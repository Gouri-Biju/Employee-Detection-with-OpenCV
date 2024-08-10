import cv2

def employee_finder(image):
    lab_image = cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
    blurred = cv2.GaussianBlur(lab_image,(5,5),None)

    lower_range_in_lab = (0,85,115)
    upper_range_in_lab = (255,115,135)

    binary = cv2.inRange(blurred,lower_range_in_lab,upper_range_in_lab)

    cnts, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if(len(cnts) ==0):
        cv2.putText(image, 'Employee NOT Found', (30, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        print('employee not found')
        return image
    biggest_contour=max(cnts, key = cv2.contourArea)
    biggest_contour_area = cv2.contourArea(biggest_contour)

    print('area :',biggest_contour_area)

    if biggest_contour_area > 100:
        print('Found Employee')
        cv2.putText(image, 'Employee Found',(30,30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.drawContours(image,[biggest_contour],0,(255,0,0),-1)
        cv2.imshow('output', image)
        cv2.waitKey(1)
        return  image
    else:
        cv2.putText(image, 'Employee NOT Found', (30, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
        print('employee not found')
        return image
