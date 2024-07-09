# Hello CICD

## **Introduction**

This project is a hands-on learning experience I undertook to understand how DevOps works and to get familiar with some of the essential tools used in DevOps workflows.

Here is the high-level process of this project:
1. **Create a Flask Web Application:**
    
    Developed a small web application using Flask to understand the basics of web app development.

2. **Run the Flask Application:**

    Ensured the Flask application was up and running smoothly on the local environment.

3. **Docker Integration:**

    Created a DockerFile to containerize the Flask application, then built and ran the project using Docker for consistent and isolated environments.

4. **CI/CD Pipeline with Jenkins:**

    Set up Jenkins to create a CI/CD pipeline, automating the build, test, and deployment processes for the Flask application.

5. **Infrastructure Management with Terraform:**

    Utilized Terraform for efficient infrastructure provisioning, deployment, scaling, and monitoring. This allowed me to manage infrastructure as code.

6. **Container Orchestration with Kubernetes:**

    Employed Kubernetes to automate the operational tasks of container management. This included deploying applications, rolling out updates, scaling as needed, and monitoring the application to maintain optimal performance.

7. **Expose Services with Ngrok:**

    Used Ngrok to expose the local development environment to the internet securely, facilitating external access for testing and demonstrations.

8. **Source Code Management with Git:**

    Managed the source code using Git, keeping track of changes and maintaining version control throughout the project lifecycle.

9. **Repository Hosting with GitHub:**

    Stored, tracked, and version controlled the project on GitHub, utilizing its robust platform for collaborative development and project management.

10. **Automation with GitHub Webhooks:**

    Implemented GitHub Webhooks to automatically trigger actions in response to specific events within the repository, streamlining the workflow and integrating various DevOps tools.

### **Project Tree Structure**

```
.
├── .git                            // git folder
├── app                             // flask application
│   ├── __pycache__
├── static                          // flask static files
│   ├── css
│   │   └── style.css
│   ├── img
│       └── ci-cd.png
├── templates                       // flask templates
│   ├── index.html
│   ├── __init__.py
│   └── views.py
├── env                             // environment variables
├── k8s                             // kubernetes files
│   ├── deployment.yaml
│   ├── ingress.yaml
│   └── service.yaml
├── terraform                       // terraform files
│   ├── .terraform
│   ├── .terraform.lock.hcl
│   ├── terraform.tfstate.backup
│   ├── main.tf
│   ├── outputs.tf
│   ├── variable.tf
│   └── terraform.tfstate
├── tests                           // python tests
│   ├── __pycache__
│   ├── __init__.py
│   └── test_views.py
├── .gitignore
├── Dockerfile                      // Docker file
├── Jenkinsfile                     // Jenkins file
├── README.md
├── run.py
└── requirements.txt
```

## **I. Setting up the Folder for the Project**

The first step for this project was to set up the main folder for this project. Let's name it `Hello CICD`.

## **II. Initialize Git in the folder**

Inside the folder, we first initialize git to keep track of changes made within the directory.

**Note**: Go to [GitHub](https://github.com/) and create a repository for this project.

```
# Initialize git in this folder.
> git init
```

**Note**: The following commands will only work if there are files in the folder as Git tracks files, not folders. But since we mentioned the initialization, I'm mentioning the rest of the process below here.

For this purpose, create a `.gitignore` file in the project folder.

```
# Add files to git
> git add .
```

where **.** represents all files. if you want to push a single file, just mention the name of the file. For example:

```
# Add the .gitignore file to git
> git add .gitignore
```

```
# Check the status of git.
> git status
```

```
# Commit the changes made. Use -m to write a message. It helps.
> git commit -m "Created .gitignore file"
```

```
# Create a connection to the repository.
> git remote add origin <remote_repository_URL>
```

```
# Push the git commits to the main branch.
> git push -u origin main
```

```
# Pull any changes to confirm that the changes were updated correctly.
> git pull origin main
```

## **III. Setting up the Virtual Environment (env) folder**

Inside the folder, we need to set up the virtual environment (env) for this project, so that any installs or updates done for the libraries used in this project won't impact the global python system.

```
# Creating a virtual environment.
> python.exe -m venv env
```

```
# Activating the virtual environment.
> ./env/Scripts/activate
```

**Note**: Add the `env/` folder to the .gitignore file. You really don't want to forget this step.

```
# Create a requirements file and do this command each time you download a library to stay up to date.
> pip freeze > requirements.txt
```