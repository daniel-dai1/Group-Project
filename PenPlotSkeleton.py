#Skeleton of PenPlotter Program

def potentiometer_input():
    """
    Collects user inputs from potentiometers & button. Contains
    definitions of servos and buttons. Calls lowpass(). Compares
    inputs against low pass band and sends passing values to
    calculate(X, Y):
    :return None:
    """
def lowpass(real, post):
    """
    Processes potentiometer inputs to reduce noise. Outputs low band
    that is 85% (alpha variable) the previous value and 15% the current
    value. Returns low pass band.
    :return alpha * previous + (1 - alpha) * current:
    """

def calculate(x_pos, y_pos):
    """
    Calls hypotenuse_length(): returns a vector. Cuts vector in half
    and calls angles(half_hypo): returning angle_a and angle_b.
    Calls translate(angle_a, angle_b):
    :return:
    """

def hypotenuse_length(x_point, y_point):
    """
    Uses origin point and desired point to calculate hypotenuse. ((X_origin
    - X_desired)^2 + (Y_origin - Y_desired)^2)sqrt. Return the hypotenuse.
    :return hypotenuse:
    """

def angles(half_hypotenuse):
    """
    Calculates angle of hypotenuse & arm as angle_a. Returns angle in
    degrees. Calls forearm_angle(angle_a): returns angle of arm &
    forearm angle in degrees as angle_b.
    :return angle_a, angle_b:
    """

def forearm_angle(angle_a, angle_b):
    """
    Calculates angle of forearm & arm as angle_a. Using sum of angles of
    a triangle, (2 * angle_a) - 180. Returns angle in degrees.
    :return angle_b:
    """

def translate(Shoulder, Elbow):
    """
    Calls servo_calibration(Shoulder, Elbow): returns tuned_shoulder,
    tuned_elbow. Translates angles in degrees into duty cycle values.
    Sends values to Shoulder and Elbow servos for motion.
    :return:
    """

def servo_calibration(shoulder_servo, elbow_servo):
    """
    Reads text file of listed calibrations, determines which terms
    angle falls under before calling
    linear_regression(shoulder_servo, upper bound, lower bound): &
    linear_regression(elbow_servo, upper bound, lower bound):
    both returning calibrated angles
    :return calibrated_shoulder, calibrated_elbow:
    """

def linear_regression(value):
    """
    Uses upper and lower bounds to linearly interpolate angle value.
    Returns a calibrated angle for servo
    :return interpolated_angle:
    """