resource "docker_image" "ops_pilot" {
  name = "sarthakrajput17/ops-pilot:latest"
}

resource "docker_container" "ops_pilot" {
  name  = "ops-pilot"

  image = docker_image.ops_pilot.image_id

  ports {
    internal = 5001
    external = 5001
  }
}