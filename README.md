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
Hello CICD
├── .git                            // git folder
├── app                             // flask application
│   ├── __pycache__
│   ├── static                      // flask static files
│   │   ├── css
│   │   │   └── style.css
│   │   └── img
│   │       └── ci-cd.png
│   ├── templates                   // flask templates
│   │   └── index.html
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

```sh
# Initialize git in this folder.
git init
```

**Note**: The following commands will only work if there are files in the folder as Git tracks files, not folders. But since we mentioned the initialization, I'm mentioning the rest of the process below here.

For this purpose, create a `.gitignore` file in the project folder.

```sh
# Add files to git
git add .
```

where **.** represents all files. if you want to push a single file, just mention the name of the file. For example:

```sh
# Add the .gitignore file to git
git add .gitignore
```

```sh
# Check the status of git.
git status
```

```sh
# Commit the changes made. Use -m to write a message. It helps.
git commit -m "Created .gitignore file"
```

```sh
# Create a connection to the repository.
git remote add origin <remote_repository_URL>
```

```sh
# Push the git commits to the main branch.
git push -u origin main
```

```sh
# Pull any changes to confirm that the changes were updated correctly.
git pull origin main
```

## **III. Setting up the Virtual Environment (env) folder**

Inside the folder, we need to set up the virtual environment (env) for this project, so that any installs or updates done for the libraries used in this project won't impact the global python system.

```sh
# Creating a virtual environment.
python.exe -m venv env
```

```sh
# Activating the virtual environment.
./env/Scripts/activate
```

**Note**: Add the `env/` folder to the .gitignore file. You really don't want to forget this step.

```sh
# If you accidentally forgot to add it to .gitignore and did git add. You can remove it from git
git rm -r --cached env
```

```sh
# Create a requirements file and do this command each time you download a library to stay up to date.
pip freeze > requirements.txt
```

## **IV. Setting up the Flask Application**

### **IV. I: Setting up the app folder**

For creating a flask application, we create an `app` folder and inside we create folders for `static` and `templates`.

- The `static` files will contain the img, css, (js...) and any assets for the project.
- The `templates` folder will contain static data as well as placeholder for dynamic data, usually HTML files that uses Jinja template.

```
# Flask Folder Structure
Hello CICD
├─ app 
│   │   
│   ├── static                          
│   │   ├── css
│   │   │   └── style.css
│   │   └── img
│   │       └── ci-cd.png
│   ├── templates                      
│   │   └── index.html
│   ├── __init__.py
│   └── views.py
└─ run.py
```

### **IV. II. Creating the HTML Template**

We'll start with the `./app/templates/index.html` file. This is just going to be a small HTML document just for the purpose of running it.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Hello CICD</title>
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/style.css') }}"
    />
  </head>
  <body>
    <h1>Hello CI/CD!</h1>
    <p>This is a test application being done to learn DevOps.</p>
    <p>Author: Edwin Ronald Lambert</p>
    <p>Last Updated: July 8, 2024</p>
    <img
      src="{{ url_for('static', filename='img/ci-cd.png') }}"
      alt="Sample Image for CI/CS pipeline"
    />
  </body>
</html>
```

**Explanations**:

- `<!DOCTYPE html>` declares the document type and the version of HTML used (HTML5).
- The `<html>` tags wraps the entire HTML document.
- The `<head>` section contains the meta-information of the document.
    - `{{ url_for('static', filename='css/style.css') }}` is a Jinja2 template syntax used in Flask to dynamically generate the URL for the CSS file located in the static folder.
- The `<body>` section contains the content of the HTML document.
    - `src="{{ url_for('static', filename='img/ci-cd.png') }}"` dynamically generates the URL for the image file located in the static folder using Jinja2 syntax.
    - `alt="Sample Image for CI/CD pipeline"` provides alternative text for the image, which is useful for accessibility and if the image fails to load.

**Note**: Create the `./static/css/style.css` to add stylesheet and design to the HTML file.

### **IV. III. Create views.py**

Since we're using the [Flask](https://pypi.org/project/Flask/) library. Let's install that into our virtual env.

```sh
# Install Flask
pip install Flask
```

We then create the `views.py` file. 

```py
from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")
```

**Explanations**:

- Import the necessary libraries.
    - `Blueprint` helps organize the application into modules, making it easier to manage large applications.
    - `render_template` is used to render HTML templates.
- Using the `Blueprint()` method, we create a new Blueprint instance.
    - `main` is the name of the blueprint.
    - `__name__` is the name of the current module.
- `@main.route("/")` is a route decorator that is associated with the path '/' with the home function.
- The `home()` function handles request to the root URL and renders the index.html template.

### **IV. IV. Creating the __init__.py file**

```py
from flask import Flask

def create_app():
    app = Flask(__name__)
    from .views import main
    app.register_blueprint(main)
    return app
```

**Explanations**:

- Import the necessary libraries.
    - `Flask` module is necessary to create flask applications.
- `app = Flask(__name__)` creates an instance of the Flask application. `__name__` is passed to `Flask` constructor to determine the root path of the application, which it needs to location resources like static and template files.
- `from .views import main` import the `main` blueprint from `views` module. The dot (`.`) indicates that `views` module is within the same package as the current module.
- `app.register_blueprint(main)` registers the `main` blueprint with the Flask application instance.
- The `create_app()` function returns the Flask application instance.

### **IV. V. Creating the run.py file**

We now create the `run.py` file to run this on the terminal.

```py
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
```

**Explanations**:

- `from app import create_app` imports the `create_app` function from the `app` module.
- `app = create_app()` creates an instance of the Flask application and assigns it to app.
- `app.run(host="0.0.0.0", port = 5000)` run the Flask application with the following settings:
    - `host="0.0.0.0"` makes the server public available, listening on all available IP addresses. This is make sure that the application is accessible from other devices on the network.
    - `port=5000` is the default port for Flask where the app will listen for incoming connections.
    - `debug=True` was the previous command. Mentioned to make sure that the application enables debugging.

### **IV. VI. Running the Flask application**

We run the application first for testing using the command.

```sh
# Run the run.py file.
py run.py
```

This will run the Flask application on your web browser at `localhost:5000`.