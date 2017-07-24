# Set_password_at_Terminal
Want to secure the terminal (Mac, Linux, windows not tested yet), give it a try. 

Req. Libraries: Anaconda, opencv

i. First, place all the scripts to the home directory

ii. Create a data-base. Run 'python acc_control.py open'. It creates p.db file in your home dir. Dont remove this file ever. IF you some how delete this then you need to create a new one.

iii. Insert User Information. Run 'python acc_control.py insert' and follow the instructions

iv. If you want to add another user account then again repeat step (iii)

v. Test run, Run 'python acc_control.py passcode' and give it user name and password that you have just created.

vi. Update: If you think you need to update any information (name, user account etc) then run 'python acc_control.py update' and follow the instructions. "you might need a personal 'key, default is 00000, you can change this any time (line 37 and 65 of acc_control.py).

vii. Delete: run 'python acc_control.py delete', and follow the instructions

viii. Display: If you want to read the data-base of your accounts, run 'python acc_control display' and follow the instructions

ix. After creating and inserting user account to data base file (p.db, after completing steps i to iii), edit your '.bashrc or .bash_profile' file and add a line 'python acc_control passcode' at the end.

x. Close the terminal and open again, you are supposed to see the password window. Type your password and enjoy.

xi. Note: There is alos a "Back Door" in case you completely forget your password (line 36 at passcode.py). 
