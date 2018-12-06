# git_notes
Compendium of basic git commands.

See more in the official documentation of GIT : https://git-scm.com/docs

## Global configurations ##

List configurations :
`$ git config --list`

Most commonly used (required) are :
* Set *username* : `$ git config --global user.name "Álvaro Sánchez Palacio"`
* Set *email* : `$ git config --global user.email "alvaro.sanchez.palacio@gmail.com"`

## Basic commands ##

Most commonly used commands are :
* Obtain GIT version : `$ git --version`.
* Initialize GIT in a project : `$ git init`.
* Obtain GIT status : `$ git status`.

### Adding files ###
You can add files to the staging area using the `add` command : 
    
    $ git add config.py

There are also a number of ways to refine the scope :
* Add __a single__ file in the staging area : `$ git add config.py`.
* Add __all__ files in the __current directory__ in the staging area : `$ git add .`.
* Add _all_ files in the staging area : `$ git add -A`.

_NB : Note the dot (.) making the difference for the __current__ directory._

### Removing files ###
You can remove files to the staging area using the `add` command : 
    
    $ git reset config.py

There are also a number of ways to refine the scope :
* Remove __a single__ file from staging area : `$ git reset config.py`.
* Remove __all__ files in the __current directory__ from staging area : `$ git reset .`.
* Remove __all__ files from staging area : `$ git reset`.

_NB : Note the dot (.) making the difference for the __current__ directory._

### Commit files ###
Commit your changes from the staging area by using the `commit` command :

    $ git commit -m "Initial Commit"

### Accessing the log ###
Accessing the logs with `log` command will provide with information of the commmits.

    $ git log

The returned result will contain :
* _hash_ (c6d3b1c68e4a29e1040a97a35b0b8685feaacaae)
* _branch_
* _Author_
* _Date_

Example :

    commit c6d3b1c68e4a29e1040a97a35b0b8685feaacaae (HEAD -> master, origin/master, origin/HEAD)
    Author: Álvaro Sánchez Palacio <alvaro.sanchez.palacio@gmail.com>
    Date:   Wed Dec 5 00:57:20 2018 +0100

### Clone ###
Clone allows for copying the content of a remote repository into a local repository.

The command `clone` has two required parameters, two paths :
1. Remote repository : Path to the remote repository, usually something like https://github.com/Alvaro-Sanchez-Palacio/git_notes.git.

1. Local repository : Path to the folder to create the local copy of the remote repository (.).
```
$ git clone https://github.com/Alvaro-Sanchez-Palacio/git_notes.git .
```

_NB : Usually - Local repository - is dot (.) as it `clone` is invoked after navigating to the "target" folder._

_See : [git-clone](https://git-scm.com/docs/git-clone)._

### Pull ###
Downloads (`fetch`) and merges to current repository the master of the specified __repository__ and/or specified __reference__ : `git pull <repository> <reference>`

    $ git pull origin master

_See : [git-pull](https://git-scm.com/docs/git-pull)._

### Push ###
Uploads the commit of the specified __reference__ to a remote __repository__ : `git push <repository> <reference>`

    $ git push origin master

_See : [git-push](https://git-scm.com/docs/git-push)._

### Branch ###
Displays existing branches in the local and / or remote repository :

    $ git branch -a

_NB : `-a` is used to display also remote branchs._

List of usefull commands :
* See merged branches : `$ git branch --merged`
* Delete a local branch : `$ git branch -d doc`


_See : [git-branch](https://git-scm.com/docs/git-branch)._

### Checkout ###
Swtiches from the current branch to the specified branch :

    $ git checkout master

_See : [git-checkout](https://git-scm.com/docs/git-checkout)._

### Merge ###
Merges specified branch with the current branch :

    $ git merge calc-add

As output of the `merge` command, GIT will expose the results occurred during the merge, or the conflicts found.

_NB : merge command is usually invoked from the master in order to merge the activity in a certain branch, however it is possible to merge two different (non-master) branches as well._

_See : [git-merge](https://git-scm.com/docs/git-merge)._

## Special features ##
Ignore files :
1. Create a .gitignore file :
    `$ touch .gitignore`
    
1. Add in the document : 
    * the name of any file on the document :
    `config.py`
    * the name of any folder on the document :
    `config/`

## Help! ##
Get help using git `git <verb> --help` or `git help <verb>`. For example :
```
$ git help config
```
Or :
```
$ git config --help
```
_NB : Dependin on OS, GIT version and console, this command might provide the output in the console or open an HTML generated on the browser._