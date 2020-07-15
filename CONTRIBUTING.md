# Workflow

The workflow used in this project is based on the suggestions in the "Branching Workflows" chapter of Pro Git: https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows

Further reading with more detail on this works: https://nvie.com/posts/a-successful-git-branching-model/

## Branching

As described in the readings linked above, the following branching structure will be used: 

1. ***master* branch**
  - Contains the current most stable version of the project
2. ***dev* branch**
  - Contains the version of the project that is actively in development, and not necessarily stable. 
  - Most merging will happen on this branch. 
3. **Topic branches**
  - These branches are for active development of specific features, bug fixes, etc.
  - Topic branches should have names that pertain to what is being worked on, and should be deleted when work is completed and merged with the *dev* branch. 
  - Developers should only push code to topic branches, and merge with *dev* through pull requests.  
  
### Merging

**Merging Topic branches with *dev***
- Topic branches may be merged to the dev branch once work on the topic is complete. 
- This merge will require a pull request for documentation purposes, but no review required. 
- Good practice is to notify other developers when merging to *dev*.

**Merging *dev* with *master***
- The *dev* branch should only be merged with the *master* branch when testing on new features/fixes is complete and the current version is considered stable. 
- This merge will require a pull request and code review by another developer. 

## Issues

Issues should be used to plan new features and to document identified bugs. 

Topic branches may be created to tackle specific issues. 

