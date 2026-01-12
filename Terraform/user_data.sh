#!/bin/bash
set -eux

# Update system
apt-get update -y

# Install prerequisites
apt-get install -y ca-certificates curl gnupg lsb-release

# Install Docker
curl -fsSL https://get.docker.com | sh

# Enable and start Docker
systemctl enable docker
systemctl start docker

# Add ubuntu user to docker group
usermod -aG docker ubuntu

# Apply group changes immediately
newgrp docker <<EOF
docker --version
EOF
