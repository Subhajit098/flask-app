pipeline{
    
    agent any
    
    stages {
        // mention the repo to be cloned
        stage("Code-clone-stg") {
            steps{
                echo "Cloning from the branch"
                // this syntax 
                git url: "https://github.com/Subhajit098/flask-app.git", branch: "main"
            }
        } 
        stage("Build-stg") {
            steps{
                // Install docker completed on host machine
                echo "code build stg using docker build"
                sh "docker build -f Dockerfile-multi -t my-app:latest ."
            }
        }

        stage("Push-to-dockerhub"){
            steps{
                withCredentials([usernamePassword(credentialsId: 'DOCKER_CREDENTIALS', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                    echo "Pushing to dockerhub"
                    sh "docker login -u ${env.DOCKER_USERNAME} -p ${env.DOCKER_PASSWORD}"
                    sh "docker tag my-app:latest ${env.DOCKER_USERNAME}/my-app:latest"
                    sh "docker push ${env.DOCKER_USERNAME}/my-app:latest"
                }
            }
        }
        
        stage("Deploy") {
            steps{
                echo "Deploy stage"
                sh "docker compose up -d"
            }
        }
        
    }
    
}
