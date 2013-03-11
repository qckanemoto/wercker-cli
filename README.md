[![Wercker status](https://app.wercker.com/status/841531b16e709d25f4ae566af33193cf/m)](https://app.wercker.com/project/bykey/841531b16e709d25f4ae566af33193cf)
# wercker-cli #

A cli tool for <http://wercker.com/> - Continuous deployment made easy.

Usage:

    $ wercker
    -----------------------
    welcome to wercker-cli
    -----------------------

    Usage:
        wercker create
        wercker status
        wercker deploy
        wercker login
        wercker logout
        wercker open targets
        wercker apps list
        wercker apps link
        wercker apps create
        wercker apps checkrepo
        wercker apps build
        wercker builds list
        wercker builds deploy
        wercker targets list
        wercker targets add
        wercker --version

## Commands
### create
Starts a wizard like setup, to get your application fully working on wercker. In detail it:
* adds a new application based on your current git repository
* checks for permissions on github or bitbucket
* triggers a build
* tries to find and add a heroku deploy target.

The newly created application information is stored in a .wercker file in the root of your repository. You don't need to add this file to your git repository, if a user has access to the project, a user can run `wercker app link` to rebuild the .wercker file

### status
Shows the status of the latest build.

### deploy
Starts a simple wizard like setup for deploying your latest build to a deploy target.

### login
Retrieves a login token for wercker and stores it in the .netrc in the users' home folder.

### logout
Removes the login token from the .netrc file

### open targets
Opens a webpage showing a deploy target's details

### apps list
Shows a list of all applications available to the user

### list app jobs
Shows a list of all builds and deploys that are still scheduled.

### apps create
This is an alias for `wercker create`

### apps link
Retrieve application information for storing in the .wercker file.

### apps checkrepo
Check the permissions for the current repository. If werckerbot has access to the repository through a group (on bitbucket) or the linked bitbucket/github account does not have sufficient rights to check permissions the tool will be unable to verify.

### builds list
Shows a list of the most recent builds

### builds deploy
An alias for `wercker deploy`

### targets add
Add a new deploy target to your application. Currently only supports heroku targets.

### targets list
Lists all deploy targets

### targets details
This is an alias for `wercker open targets`
