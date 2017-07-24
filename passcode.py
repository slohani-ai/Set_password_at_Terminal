import time
import os
import getpass
from termcolor import colored,cprint
import user_pass as up
import cv2
data_base = 'p.db'


def initial():
    cprint ('##########################################################################################','white','on_red')#,attrs=['blink'])
    cprint ('                                    Important Information                                 ','white','on_red')
    cprint ('        Personal computer, 3 consecutive failure leads to PHOTO ENFORCED and SHUTTING DOWN','white','on_red')
    cprint ('##########################################################################################','white','on_red')#,['blink'])
    print ''
    cprint ('|LOGIN INFORMATION REQUIRED','magenta')


def final_line(name):
            cprint ('                       -*-{}-*-                       '.format(name),'cyan',attrs=['bold'])
            cprint ('--------------------------------------------------------------------','cyan')
            hour = time.localtime()[3]
            if hour < 12:
                cprint ('          {0}:{1} am, Good Morning {2}, Have a nice day ahead                     '.format(time.localtime()[3],time.localtime()[4],name),'green')
            elif hour >= 12 and hour < 16:
                cprint ('          {0}:{1} pm, Good Afternoon {2}, Have a nice day ahead                     '.format(time.localtime()[3],time.localtime()[4],name),'green')
            else:
                cprint ('          {0}:{1} pm, Good Evening {2}, Have a nice night ahead                   '.format(time.localtime()[3],time.localtime()[4],name),'green')
                  



def req():
    initial()
    lists_of_users = up.extract(data_base)
    for i in range(100):
        user = raw_input(colored('|User ID: ','magenta'))
        line = getpass.getpass(colored('|Password:','magenta'))
	mask = []
	for j in range(len(lists_of_users)):
            if user == lists_of_users[j][3] and line == lists_of_users[j][4]:
	        final_line('{} {}'.format(lists_of_users[j][1],lists_of_users[j][2]))
		mask.append('1')
		break
            else:
	       pass
        if len(mask) == 1:
	    break
        else:

             cprint ('|*-* Authorization failed. Try Again *-*','red')
	     if (i+1)%3 == 0:
                cam = cv2.VideoCapture(0)
                time.sleep(2)
                s,im = cam.read()
                cv2.imwrite('Unknown_Host.png',im)
                cv2.imshow('UNKNOWN HOST',im)
                os.system('cp Unknown_Host.png Desktop')
                cv2.waitKey(2000)
                cv2.destroyAllWindows()
		#cprint ('#################################################################','cyan',attrs=['blink'])
		#cprint ('Terminal is shutting down for security reason......','cyan')
		#cprint ('#################################################################','cyan',attrs=['blink'])
		#time.sleep(5)		
		#os.system('killall Terminal')
             else:
                pass    




