#!/bin/bash

# Install ruby gem dependencies
# Ensure rbvmomi is installed with sudo or root access
if [ "$EUID" -eq 0 ]
  then echo "Installing rbvmomi gem"
    /opt/puppetlabs/bin/puppet resource package rbvmomi ensure=present provider=puppet_gem
  else echo "Installing RBVmomi with sudo, via Puppet package resource"
    sudo /opt/puppetlabs/bin/puppet resource package rbvmomi ensure=present provider=puppet_gem
    /opt/puppetlabs/bin/puppet resource package hocon ensure=present provider=puppet_gem
    /opt/puppetlabs/bin/puppet resource package json ensure=present provider=puppet_gem
  exit
fi