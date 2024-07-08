output "namespace" {
    value = kubernetes_namespace.hello-cicd.metadata[0].name
}