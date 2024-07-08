output "namespace" {
    value = kubernetes_namespace.flask_app.metadata[0].name
}