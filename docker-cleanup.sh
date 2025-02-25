#!/bin/bash

# Check if script is run as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run this script as root (using sudo)"
    exit 1
fi

# Function to safely execute docker commands
docker_exec() {
    command="$1"
    docker $command || echo "Warning: Failed to execute: docker $command"
}

echo "Stopping all containers..."
for container in $(docker ps -aq); do
    docker stop $container || true
done

echo "Removing all containers..."
for container in $(docker ps -aq); do
    docker rm -f $container || true
done

echo "Removing all images..."
for image in $(docker images -aq); do
    docker rmi -f $image || true
done

echo "Removing all volumes..."
for volume in $(docker volume ls -q); do
    docker volume rm $volume || true
done

echo "Removing all networks..."
for network in $(docker network ls -q -f type=custom); do
    docker network rm $network || true
done

echo "Pruning system..."
docker system prune -a --volumes --force

echo "Cleanup completed"
docker system prune -af

