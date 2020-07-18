# Useful Git commands
The following are a collection of commonly used commands, for reference.

## Creating a local branch that tracks an existing remote branch:
***Do this when you create a branch on the Github repo first, and want to sync your local repo with it.***

Get branch list from remote:

    git fetch
    
Create a branch called "branch-name" that tracks the remote (which is assumed to be called "origin") branch called "branch-name":

    git branch --track branch-name origin/branch-name
    
Switch to the new branch:

    git checkout branch-name
    
## Creating a feature branch off of the *dev* branch locally
***Do this when you are creating a branch in your local repo, and want to push the new branch to the Github repo.***

Note: if the branch already exists on Github, use the instructions above to create a branch locally to track the
existing branch.

Create the branch *feature_branch* from the *dev* branch and switch to it:

    git checkout -b feature_branch dev  
    
Push the new branch to the remote, called "origin", with the -u flag:

    git push -u origin feature_branch
    
*feature_branch* should now appear in the Github repo. It should now also be tracked as the upstream branch for your
local version of *feature_branch*.

## Merging a feature branch with the *dev* branch
***Do this when you are done working on the features in the "feature_branch" and are ready to merge it with dev.
Alternatively, you can accomplish this by opening a pull request on Github.***

First, make sure your commits on your local version of *feature_branch* are pushed to the remote.

Switch to the *dev* branch:

    git checkout dev
    
Merge your *feature_branch* with the *dev* branch:

    git merge --no-ff feature_branch
    
*Note: the --no-ff option passed to merge disables the "fast-forward" feature in merge, which preserves historical data
by keeping the commit objects that come together to create the feature grouped together (or something like that).*

Finally, you can push the updated *dev* branch to the remote:

    git push origin dev
    
If you are done with *feature_branch* and want to delete it, you can do so locally and remotely with the following
commands:

    git branch -d feature_branch
    git push origin --delete feature_branch
    
