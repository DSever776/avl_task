#!/bin/sh

#!/bin/bash

# Default version values
service1_version=""
service2_version=""

function usage {
    echo "Usage: $0 [--service1_version=VERSION] [--service2_version=VERSION]"
    echo ""
    echo "Example: ./deploy --service1_version=v1.0 --service2_version=v1.0"
    exit 1
}

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --service1_version=*) service1_version="${1#*=}" ;;
        --service2_version=*) service2_version="${1#*=}" ;;
        *) echo "Invalid option: $1" >&2
           usage ;;
    esac
    shift
done

if [[ -z "$service1_version" || -z "$service2_version" ]]; then
    echo "Error: you didn't write the version of one or more services"
    echo ""
    usage
fi

echo "Service 1 version: $service1_version"
echo "Service 2 version: $service2_version"


