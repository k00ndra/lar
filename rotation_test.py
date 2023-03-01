from robolab_turtlebot import Turtlebot,Rate,get_time

turle = Turtlebot()
refresh_rate = 10 #Hz
time_limit = 10 #s
angular_speed = 0.8#rad/s
rate = Rate(refresh_rate)


start_time = get_time()
while get_time() - start_time <time_limit:
    turle.cmd_velocity(angular = angular_speed)
    rate.sleep()
    





