import user_pass as up
import sys
import passcode
name = 'p.db'
argv = sys.argv[1]
if argv == 'open':
    up.open_account(name)
elif argv == 'update':
    up.update(name)
elif argv == 'display':
    up.display(name)
elif argv == 'insert':
    up.insert(name)
#elif argv == 'extract':
#    up.extract(name)
elif argv == 'delete':
    up.delete(name)
elif argv == 'passcode':
    passcode.req()
else:
   print ('No operation for {}'.format(argv))
   sys.exit()
