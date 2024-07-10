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
# Flask Application Folder Structure
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

## **V. Prepare Flask Application for Testing**

Ensure that your Flask application has a dedicated test directory. We'll use Python’s built-in unittest framework.

```
# Flask Test Folder Structure
Hello CICD
└─ tests
    ├── __init__.py                          
    └── test_views.py
```

```py
import unittest
from flask import url_for
from app import create_app

class FlaskTestCase(unittest.TestCase):
    
    def setUp(self):
        # Set up test client before each test.
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()
        
    def test_home_status_code(self):
        # Test that the homepage is accessible.
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_home_data(self):
        # Test the data returned by the home page.
        response = self.client.get('/')
        self.assertIn(b'Hello CI/CD!', response.data)
        
        
if __name__ =="__main__":
    unittest.main()
```

**Explanations**:

- Import the necessary libraries.
    - `unittest` is the Python's built-in module for creating and running tests.
    - `create_app` creates and configures an instance of the Flask application.
- We first create a test class that inherits from `unittest.Testcase`, providing a framework for writing tests.
    - The `setUp` is a special method that is run before each test method. It is used to set up the state that is shared among the test methods.
        - `self.app = create_app()`: Creates an instance of the Flask application using the create_app function.
        - `self.app.testing = True`: Puts the Flask app in testing mode, which provides better error messages and ensures that exceptions propagate rather than being handled by the Flask error handlers.
        - `self.client = self.app.test_client()`: Creates a test client that can be used to simulate HTTP requests to the Flask application. This client is used to interact with the application during testing.
    - The `test_home_status_code` is a test method to verify that the home page is accessible.
        - `self.assertEqual(response.status_code, 200)`: Asserts that the HTTP status code of the response is 200, indicating success.
    - The `test_home_data` is a test method to verify the content of the home page.
        - `self.assertIn(b'Hello CI/CD!', response.data)`: Asserts that the response data contains the byte string b'Hello CI/CD!'. This ensures that the expected content is present on the home page.

## **VI. Setting up Docker**

Now we will use Docker to build, test, and deploy applications quickly.

### **VI. I. Setting up Docker Desktop**

**Note**: I'm using WIndows (Yeah Yeah, I know. I hear you!)

1. Go to Docker website and download [Docker Desktop](https://www.docker.com/products/docker-desktop/) depending on the platform you use.
2. Double-click and run the Docker Desktop installer executable.
3. Once the installation is complete, click "Close" and "Restart" your computer if prompted.
4. After installation and reboot, launch Docker Desktop from the Start Menu.
5. Docker Desktop will complete the initial setup. Follow any on-screen instructions to finalize the configuration.
6. (Optional) Sign in to Docker Hub.

```sh
# Verify Installation
docker --version
```

```sh
# Run a test container.
docker run hello-world
```

This command will download a test image and run it in a container. If successful, you'll see a `"Hello from Docker!"` message. 

### **VI. II. Creating a Dockerfile**

A `Dockerfile` is a text file that contains collections of instructions and commands that will be automatically executed in sequence in the docker environment for building a new docker image.

```
# Dockerfile folder structure
Hello CICD
└─ Dockerfile
```

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Intall any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Defined environment variables
ENV NAME World

# RUN run.py when the container launches
CMD [ "python", "run.py" ]
```

**Explanations**:
- `FROM python:3.9-slim` specifies the base image for the Docker image. `python:3.9-slim` is an official Docker Image for Python 3.9 with a minimal footprint.
- `WORKDIR /app` sets the working directory inside the container to `/app`. All subsequent instructions will be run in this directory.
- `COPY . /app` copies all the contents of the current directory on the host machine into the `/app` directory in the container.
- `RUN pip install --no-cache-dir -r requirements.txt` installs all the Python packages specified in the `requirements.txt` using `pip`. The `--no-cache-dir` option prevents `pip` from caching the package files, which reduces the image size.
- `ENV NAME World` sets an environment variable `NAME` with the value `World` inside the container.
- `CMD [ "python", "run.py" ]` specifies the command to run when the container starts.

### **VI. III. Build and Run the Docker Container**

Now, we build and run the docker container and verify that the applications runs inside the container by accessing it via `localhost:5000`.

```sh
# Build the docker image.
docker build -t hello-cicd .
```

**Explanations**:

- `docker build` command is used to build a Docker image from a Dockerfile.
- `-t hello-cicd` is used to tag the image with the name hello-cicd.
- The dot `.` at th end of the command specifies the build context, which is the current directory. Docker will look for a `Dockerfile` in this directory and use it to build the image.

```sh
# Run the Docker Container
docker run -p 5000:5000 hello-cicd
```

**Explanation**:

- `docker run` is the command runs a Docker container from a specified Docker image.
- `-p 5000:5000` is used to publish a container's port to the host. The format is `host_port:container_post`.

Verify that the application runs by opening the web browser and navigate to `https://localhost:5000`.

## **VII. Setting Up Terraform**

### **VII. I. Install and Verify Terraform**

1. Download the appropriate [Terraform](https://developer.hashicorp.com/terraform/install) for your OS from the website.
2. Extract the binary to a directory included in your system's PATH, such as `C:\Windows\System32` or add the binary location to the environment variables `PATH` variable or manually add it.
3. Open terminal/command prompt and enter `terraform -v` to ensure it's correctly installed and variables are set.

### **VII. II. Create Terraform Configuration Files**

1. Navigate to your project directory and create a subdirectory named terraform.
2. Inside this directory, create the following files:
    - `main.tf`: Main configuration file where you will define the provider and resources.
    - `variables.tf`: File to declare variables.
    - `outputs.tf`: File to declare outputs.

```
# Terraform Folder Structure
Hello CICD
└─ terraform
    ├── main.tf                     
    ├── outputs.tf
    └── variable.tf
```

**main.tf** file

```hcl
terraform {
    required_providers {
        kubernetes = {
            source = "hashicorp/kubernetes"
        }
    }
}

provider "kubernetes" {
    config_path = "~/.kube/config"
}

resource "kubernetes_namespace" "hello-cicd" {
    metadata {
        name = "hello-cicd-namespace"
    }
}
```
**Explanations**:

- `terraform` is the block is used to specify settings related to Terraform itself, including provider requirements.
    - `required_providers`: This block specifies the providers that are required for this configuration.
        - `kubernetes` is the name of the provider.
            - `source = "hashicorp/kubernetes"`: This specifies the source of the provider, indicating that the Kubernetes provider plugin should be downloaded from the HashiCorp repository.
- `provider "kubernetes"` block configures the Kubernetes provider.
    - `config_path = "~/.kube/config"`: This specifies the path to the Kubernetes configuration file (kubeconfig). 
- `resource "kubernetes_namespace" "hello-cicd"`: This block defines a resource of type kubernetes_namespace with the identifier hello-cicd.
    - `metadata` block specifies metadata for the Kubernetes namespace.
        - `name = "hello-cicd-namespace"`: This sets the name of the namespace to hello-cicd-namespace.

**outputs.tf** file

```
output "namespace" {
    value = kubernetes_namespace.hello-cicd.metadata[0].name
}
```

**Explanations**:

- `output "namespace"`: This declares an output block named namespace. Outputs are used to make information about your infrastructure available after the configuration has been applied. 
    - `value`: This specifies the value that the output will contain. In this case, the value is being set to kubernetes_namespace.hello-cicd.metadata[0].name.

### **VII. III. Initialize and apply Terraform Configurations**

1. Navigate to the `Terraform` folder inside the main directory.
2. Run `terraform init` to initialize the directory with necessary Terraform configurations.
3. Execute terraform plan to see the execution plan.
4. Run terraform apply to apply the configurations and create the resources in your cluster.

## **VIII. Setting up Container Orchestration with Kubernetes**

Kubernetes can be used to automatically provisions, deploys, scales, and manages containerized applications without worrying about the underlying infrastructure.

### **VIII. I. Enabling Kubernetes in Docker Desktop**

1. Open Docker Desktop.
2. Go to Settings > Kubernetes.
3. Check "Enable Kubernetes" and apply changes.

### **VIII. II. Creating Kubernetes Configuration files**

1. Navigate to your project directory and create a subdirectory named k8s.
2. Inside this directory, create files such as deployment.yaml, service.yaml, and ingress.yaml.

```
# Terraform Folder Structure
Hello CICD
└─ k8s
    ├── deployment.yaml
    ├── ingress.yaml
    └── service.yaml
```

**deployment.yaml** file

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-cicd
spec:
  replicas: 3
  selector:
    matchLabels:
      app: hello-cicd
  template:
    metadata:
      labels:
        app: hello-cicd
    spec:
      containers:
        - name: hello-cicd
          image: {username}/hello-cicd:latest
          ports:
            - containerPort: 5000
```

**Explanations**:
- `apiVersion: apps/v1` specifies the API version for the Kubernetes Deployment object. `apps/v1` is the stable API version for managing deployments.
- `kind: Deployment` indicates that the resource being defined is a Deployment. A Deployment ensures that a specified number of pod replicas are running at any given time.
- `metadata` provides metadata about the deployment.
- `spec` describes the desired state of the Deployment.
    - `replicas: 3` specifies that three replicas (pods) of the application should be running.
    - `selector` defines how to identify the pods managed by this Deployment.
        - `matchLabels` specifies that pods with the label app: hello-cicd are selected.
    - `template` describes the pod that will be created by the Deployment.
        - `containers` specifies the containers that will run in the pods.
            - `name: hello-cicd` is the name of the container.
            - `image: {username}/hello-cicd:latest` is the Docker image to use for the container. 
            - `ports` specifies the ports that the container will expose.
                - `containerPort: 5000` mentions that the container will listen on port 5000.

**service.yaml** file

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello-cicd-service
  namespace: hello-cicd-namespace
spec:
  type: LoadBalancer
  ports:
    - port: 5000
      targetPort: 5000
      protocol: TCP
  selector:
    app: hello-cicd

```

**Explanations**:

- `kind: Service` indicates that the resource being defined is a Service. A Service is an abstraction that defines a logical set of pods and a policy to access them.
- `spec` describes the desired state of the Service.
    - `type: LoadBalancer` specifies that the Service should be of type LoadBalancer, which exposes the Service externally using a cloud provider’s load balancer.
    - `ports` defines the ports that the Service will expose.
        - `port: 5000` si the port on which the Service will be exposed.
        - `targetPort: 5000` is the port on the container that the traffic will be forwarded to.
        - `protocol: TCP` is the protocol used by the Service. In this case, it’s TCP.
    - `selector` defines how the Service will identify the pods it routes traffic to.

### **VIII. III. Deploy and Access the Application**

1. On the terminal, use `kubectl apply -f k8s/` to apply your Kubernetes configurations.
2. Since you’re using Docker Desktop, your service type can be LoadBalancer.
3. Run `kubectl get services -n hello-cicd-namespace` to find the IP and port to access your Flask application.

## **IX. Setting Up Continuous Integration and Continuous Deployment (CI/CD) with Jenkins**

First, you need to have Jenkins installed on your server or local machine.

### **IX. I. Setting up Jenkins**

1. Download [Jenkins](https://www.jenkins.io/download/) for your platform.
2. Install Jenkins based on the instructions specific to the OS.
3. After installation, navigate to `https://localhost:8080`.
4. Follow the on-screen installation to complete the setup, which includes unlocking Jenkins using the initial admin password found in the installation logs or file.   

### **IX. II. Configure Jenkins for the Project**

After installation, we need to set up the project in Jenkins.

1. Create a New Job:
    - On the Jenkin's dashboard, click New Item.
    - Enter the name for the job. For Example, `hello-cicd`.
    - Select `Pipeline` and click OK.
2. Configure Source Code Management:
    - In the job configurations, scroll to the "`pipeline`" section.
    - You can choose either "`Pipeline script`" to write the Jenkinsfile script directly in the UI, or "`Pipeline script from SCM`" to load it from your source control. `Git` in my case.

### **IX. III. Creating a Jenkinsfile**

A `Jenkinsfile` defines the steps that Jenkins should follow as part of the CI pipeline. 

```groovy
pipeline {
    agent any
    environment {
        // Update this with your Docker Hub username and the repository name
        DOCKER_IMAGE = '{username}/hello-cicd'

        // Specify the path to your kubeconfig file correctly for a Windows machine.
        KUBECONFIG = 'C:\\Users\\user\\.kube\\config'
    }
    stages {
        stage('Build') {
            steps {
                script {
                    bat "docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} ."
                    bat "docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}"
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Now using 'hello-cicd' as the container name as per your deployment details
                    bat "kubectl set image deployment/hello-cicd hello-cicd=${DOCKER_IMAGE}:${BUILD_NUMBER} -n hello-cicd-namespace"
                }
            }
        }
    }
}
```

**Explanation**:

- `pipeline` declares the beginning of the Jenkins pipeline.
- `agent any` specifies that the pipeline can run on any available Jenkins agent.
- `environment` defines the environment variables that are accessible throughout the pipeline.
    - `DOCKER_IMAGE` is the docker image name.
    - `KUBECONFIG` is the path to Kubernetes configuration file (`kubeconfig`)
- `stages` consists of two stages: `Build` and `Deploy`.
    - `stage("Build")` defines a stage named "Build".
        - `bat "docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} ."` uses the `bat` command to execute a batch script on the Windows machine. It builds a Docker image with a tag that includes the Docker image name and the Jenkins build number.
        - `bat "docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}"` pushes the docker image to the Docker Hub using the tag created in the previous step.
    - `stage("Deploy")` defines a stage named "Deploy".
        - `bat "kubectl set image deployment/hello-cicd hello-cicd=${DOCKER_IMAGE}:${BUILD_NUMBER} -n hello-cicd-namespace"` uses the `bat` command to execute a batch script to update the Kubernetes deployment named `hello-cicd` in the `hello-cicd-namespace` to use the new Docker image tagged with the current build number.

### **IX. IV. Build the Pipeline**

Configure the Jenkins pipeline to pull the code from the GitHub repository, build the Docker image, run tests, and deploy the application.

1. On the Jenkins dashboard, Click on the job you just created.
2. Click `Build Now` to start the pipeline.
3. After clicking Build Now, you'll see a new build appear under the Build History.
4. Click on the build number or the progress bar icon to open the build status page.
5. Here you can monitor the progress and see the console output by clicking Console Output. This will show you real-time logs of the build process, including any tests run, Docker build steps, and deployment actions.

### **IX. V. Viewing your application**

1. If your Jenkins server and Flask app are deployed on the same network or machine, you can access your Flask application by navigating to `http://<jenkins-host-ip>:5000` in your web browser.
2. If it’s running as a Docker container directly on the Jenkins host, and you've mapped the ports correctly as in the example, http://localhost:5000 should display your Flask app.

