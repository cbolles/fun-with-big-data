# Getting Started
## Workspace Creation

### 1. Selected create a workspace
Go to c9.io and select "Create a new workspace"
![Cloud 9 workspace](docs/images/c9_screenshot.png)

### 2. Name it
Give the workspace a name and description, do not create the workspace yet
![Cloud 9 workspace options](docs/images/c9_workspace_options.png)

### 3. Copy Github URL
From github click on the green "Clone or download" button and copy the URL
![github url](docs/images/github_url.png)

### 4. Paste the url
In cloud 9, base the url in the text box titles "Clone from Git or Mercurial URL"
![github url c9](docs/images/git_url_c9.png)

### 5. Create workspace
At this point you can select to create workspace

### 6. Change Default version of python
In cloud 9, click on the gear in the top right corner of the screen
![c9 preferences](docs/images/c9_preferences.png)

Chose the sub menu "Python Support" on the left hand side
![c9 python settings](docs/images/python_settings.png)

Switch from Python 2 to Python 3 on the "Python Version" drop down menu
![python version](docs/images/python_version.png)

### 7. Install requirements
In the terminal at the bottom type in `sudo pip3 install -r requirements.txt`
![pip install](docs/images/pip%20install.png)

### 8. Updating
Some times I might make a change and will need you to get the changes, when that happens run `git pull origin master`
in the terminal
![git pull](docs/images/git_pull.png)