# This is my first project, lets work together and improve on this and make it better.
# Please be sure to install speedtest-cli, so you can properly use this code. 

import speedtest

test = speedtest.Speedtest()

down_speed = test.download()
up_speed = test.upload()

print("Download Speed: ", down_speed)
print("Upload Speed: ", up_speed)
