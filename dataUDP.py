import struct, socket, math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
#struct OutSimPack
#{
#   unsigned	Time;		// time in milliseconds (to check order)
#	Vector		AngVel;		// 3 floats, angular velocity vector
#	float		Heading;	// anticlockwise from above (Z)
#	float		Pitch;		// anticlockwise from right (X)
#	float		Roll;		// anticlockwise from front (Y)
#	Vector		Accel;		// 3 floats X, Y, Z
#	Vector		Vel;		// 3 floats X, Y, Z
#	Vec	    	Pos;		// 3 ints   X, Y, Z (1m = 65536)
#	int		    ID;		    // optional - only if OutSim ID is specified
#};
UDP_IP = "169.254.9.218"
UDP_PORT = 4123
outsim = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # Cai dat Internet va UDP
outsim.bind((UDP_IP,UDP_PORT))
outsimstr= struct.Struct('I3ffff3f3f3i')         # dinh dang kieu du lieu goi
f = open("roll_data.txt", 'w')
fig = plt.figure()
ax = fig.add_subplot(1,2,1)
xs = []
ys = []
def animate(i,xs,ys):
    (packet,addr) = outsim.recvfrom((64))
    data = outsimstr.unpack(packet)
    # Add x and y to lists
    xs.append(data[0])
    ys.append(math.degrees(data[4]))
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)
    # Format plot
    plt.subplots_adjust(bottom=0.30)
    plt.title('Du Lieu Yaw')
    plt.xlabel('time')
    plt.ylabel('Yaw')
def main():
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1)
    plt.show()
   # while time in range(10000):
    #    (packet,addr) = outsim.recvfrom(64)		   # Do dai goi du lieu la 64 bytes
     #   data = outsimstr.unpack(packet)              # Chuyen tu bytes sang kieu du
    #print('du lieu:',data)
    #    time = data[0]
    #    heading, pitch, roll = data[4], data[5], data[6]
      #  heading,pitch, roll = math.degrees(heading),math.degrees(pitch), math.degrees(roll)
      #  print("time (millis):",time)
       # print("Yaw: ",heading)
       # print("pith: ",pitch)
      #  print("roll: ",roll)
      #  rolldata=[str(roll),'\n']
       # f.writelines(rolldata)
if __name__ == '__main__':
   main()