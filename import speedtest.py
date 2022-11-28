import speedtest

test = speedtest.Speedtest()

down_speed = test.download()
up_speed = test.upload()

print("Download Speed: ", down_speed)
print("Upload Speed: ", up_speed)
