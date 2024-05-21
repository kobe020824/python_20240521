
# 일반적인 언어활용(파이썬)
my_string = "python"
x = 0

for i in my_string :
    x = x + 1
    print(my_string[0:x])

for i in my_string:
     x = x - 1
     print(my_string[0:x])


pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                echo 'building the application...'
            }
        }
        stage('test') {
            steps {
                echo 'testing the application...'
            }
        }
        stage('deploy') {
            steps {
                echo 'deploying the application...'
            }
        }
    }
}
