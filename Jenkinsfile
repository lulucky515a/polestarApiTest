pipeline {
    agent {
        dockerfile {
//             filename "Dockerfile"
            dir 'Dockerfile' // Dockerfile 所在目录
            label 'docker' // 运行构建的标签（可选）
        }
    }

    stages {
        stage("build") {
            steps {
                sh "python3 main.py"
            }
        }

        stage("html") {
            steps {
                publishHTML(target: [allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: "reports",
                reportFiles: "*.html",
                reportName: "My Reports",
                reportTitles: "The Report"])
            }
        }
    }

//     stages{
//         stage("html"){
//             steps{
//                 publishHTML(target: [allowMissing: false,
//                 alwaysLinkToLastBuild: true,
//                 keepAll: true,
//                 reportDir: "reports",
//                 reportFiles: "*.html",
//                 reportName: "My Reports",
//                 reportTitles: "The Report"])
//             }
//         }
//     }

//     post{
//         always{
//             each "Pipeline 构建成功"
// //                 publishHTML(target : [allowMissing: false,
// //                 alwaysLinkToLastBuild: true,
// //                 KeepAll: true,
// //                 reportDir: "reports",
// //                 reportFiles: "*.html",
// //                 reportName: "My Reports",
// //                 reportTitles: "The Report"])
//
//                 publishHTML (target: [
//                 allowMissing: false,
//                 alwaysLinkToLastBuild: false,
//                 keepAll: true,
//                 reportDir: 'reports',
//                 reportFiles: '*.html',
//                 reportName: "My Reports"])
//         }
//     }
}