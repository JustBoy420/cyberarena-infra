
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_network" "cyberarena_net" {
  name = "cyberarena_network"
}

resource "docker_container" "nginx" {
  image = "nginx:latest"
  name  = "cyberarena-nginx"
  ports {
    internal = 80
    external = 8080
  }
  networks_advanced {
    name = docker_network.cyberarena_net.name
  }
}