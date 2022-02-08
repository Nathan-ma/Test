import argparse
import git

import os
from git import Repo

repo_path = '/Users/darvos/Documents/Freelancer/Toradex/repo_test'
# Repo object used to programmatically interact with Git repositories
repo = Repo(repo_path)
# check that the repository loaded correctly

COMMITS_TO_PRINT = 5

def print_commit(commit):
  print('----')
  print(str(commit.hexsha))
  print("\"{}\" by {} ({})".format(commit.summary,
                                    commit.author.name,
                                    commit.author.email))
  print(str(commit.authored_datetime))
  print(str("count: {} and size: {}".format(commit.count(),
                                            commit.size)))

def print_repository(repo):
  print('Repo description: {}'.format(repo.description))
  print('Repo active branch is {}'.format(repo.active_branch))
  for remote in repo.remotes:
      print('Remote named "{}" with URL "{}"'.format(remote, remote.url))
  print('Last commit for repo is {}.'.format(str(repo.head.commit.hexsha)))

def boo(args):
  if args.update:
    print("Argument is True")
    Repo.remotes['origin'].fetch()
    Repo.git.reset('--hard')
    Repo.remtes['origin'].pull()
    
  elif args.update == False:
    print("Argument is False")

    
if __name__ == "__main__":
  my_parser = argparse.ArgumentParser()
  my_parser.version = '1.0'
  my_parser.add_argument('--update', help="Updates",
                        action="store_true", default=False, dest='update')
  my_parser.set_defaults(func=boo)

  args = my_parser.parse_args()

  args.func(args)
  
  if not repo.bare:
      print('Repo at {} successfully loaded.'.format(repo_path))
      print_repository(repo)
      # create list of commits then print some of them to stdout
      commits = list(repo.iter_commits('master'))[:COMMITS_TO_PRINT]
      for commit in commits:
          print_commit(commit)
          pass
  else:
      print('Could not load repository at {} :('.format(repo_path))
