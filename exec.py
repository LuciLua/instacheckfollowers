import instaloader
import argparse
import getpass

import rich

# Get instance
L = instaloader.Instaloader()

# Args
parser = argparse.ArgumentParser(
    description="Welcome to Insta get_Followers and Followings",
    prog='tool',
    formatter_class=lambda prog: argparse.HelpFormatter(
        prog,
        max_help_position=100, 
      )
  )

args = [
        ('-u', '--username', 'defines username', {}),
        ('-w', '--who', 'who', {})
       ]

for args1, args2, description, options in args:  
     parser.add_argument(args1, args2, help=description, **options, required='true')

args = parser.parse_args()


# Login or load session
passw = getpass.getpass('password for login in {}: '.format(args.username))
L.login('{}'.format(args.username), passw)
L.interactive_login('{}'.format(args.username))      # (ask password on terminal)
L.load_session_from_file('{}'.format(args.username)) # (load session created w/  
# `instaloader -l USERNAME`)

# # Obtain profile metadata
# profile = instaloader.Profile.from_username(L.context, 'tamiyukie')
profile = instaloader.Profile.from_username(L.context, '{}'.format(args.who))

rich.print('[green] FullName: {}'.format(profile.full_name))
rich.print('[#333] Biograph: {}'.format(profile.biography))
rich.print('[#333] External Url: {}'.format(profile.external_url))
rich.print('[blue] Verify Status: {}'.format(profile.is_verified))
rich.print('[green] Profile Pic Url: {}'.format(profile.profile_pic_url))

# Gera lista Seguindo
with open('seguindo.txt', 'w') as arquivo:
    arquivo.write('followers:\n')
    for followee in profile.get_followees():
        arquivo.write('"{:}"\n'.format(followee.username))
with open('seguindo.txt') as arquivo:
    print(arquivo.read())
    
    
# Gera lista Seguidores
with open('seguidores.txt', 'w') as arquivo:
    arquivo.write('followers:\n')
    for followers in profile.get_followers():
        arquivo.write('"{:}"\n'.format(followers.username))
with open('seguidores.txt') as arquivo:
    print(arquivo.read())
