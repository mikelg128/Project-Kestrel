# Useful Git commands
The following are a collection of commonly used commands, for reference.

## Creating a branch that tracks a remote branch:

Get branch list from remote:

    git fetch
    
Create a branch called "branch-name" that tracks the remote (which is assumed to be called "origin") branch called "branch-name":

    git branch --track branch-name origin/branch-name
    
Switch to the new branch:

    git checkout branch-name
    
    
##