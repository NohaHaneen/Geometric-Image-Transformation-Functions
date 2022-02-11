# DIP - Image Geometric Transformation

![image](https://user-images.githubusercontent.com/14307773/145757544-f45fed1b-72c9-4f76-b899-7ef62304f6eb.png)

In this project, we have created a GUI application that performs transformation operations such as Scaling, Translation, Rotation, Affine, Perspective, Polar and Log-Polar Coordinate transformation. These operations are used to perform Geometric Transformations on images to manipulate them.
> Note: For UI Execution Steps, refer to the UI_Execution_Instructions.pdf file

## Team Members

1. Hardith Suvarna Murari
2. Namrata Gangaraju
3. Noha Hannen Syed Imran
4. Shobha Pallakonda
5. Sukrutha Panyala

## Tech Stack

React :electron:

Flask API :steam_locomotive:

Python :snake:

## Folder structure

```sh
bonus-project-team-2/
├── api                                       # API
     ├── Transformation
          ├── affineTransformation.py
          ├── logPolarTransformation.py
          ├── perspectiveTransformation.py
          ├── polarTransformation.py
          ├── rotationTransformation.py
          ├── scalingTransformation.py
          ├── transformation.py               # starter file
          ├── translationTransformation.py
          ├── utils.py                        
     ├── server.py                            # Flask API Server
├── frontend                                  # Front End
├── DIP_DEMO_PPT.ptx                          # PPT used in demo
├── Project Proposal Team 2.pdf               # Project Proposal Document
├── README.MD                                 
├── Team2-Final Report.pdf                    # Final Report PDF
├── UI_Execution_Instructions.pdf             # Steps regarding sample UI Execution workflow

```

## Installation

```
git clone https://github.com/UHCSDigitalImageProcessing/bonus-project-team-2.git
```

### Front End Installation
```
cd frontend
npm i
npm start
```
### API Installation
```
cd api
python3 -m venv venv
venv\Scripts\activate
pip install Flask
```
> For More Information on Flask Installation click [here](https://flask.palletsprojects.com/en/1.0.x/installation/)

## Branching :octocat:

> We create branches so we can work at the same time and then we merge those branches with the main one

1. `git branch {your-branch-name}`
2. `git checkout {your-branch-name}`
3. `git push --set-upstream origin {your-branch-name}`

## To push your work to the shared repo run in the root folder. 

> Never push if you haven't pull the latest code and solve the merging conflicts locally if any

1. `git add .`
2. `git commit -m "Your message, what you did in the code"`
3. `git push`

## To pull from main

> Always pull before starting to work for the day, or first verify that you have the latest code
> Make sure to know your origin

1. `git pull origin main`

## How to open a pull request

> Pull requests or PRs are basically how you merge your changes with the master code. They will be revised by a member of the group and that member will post comments on your code and ask you to fix those.

1. Once you push your code you will see a green message saying if you want to create a pull request. Always do a pull request to the main branch. Do not delete your own branch as you will continue to use it.
2. You can also click on Pull Request and open one there.
