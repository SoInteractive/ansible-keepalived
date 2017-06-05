<p><img src="http://www.sebastien-han.fr/images/keepalived.png" alt="keepalived logo" title="keepalived" align="right" height="60" /></p>

Ansible Role: keepalived
========================

[![Build Status](https://ci.devops.sosoftware.pl/buildStatus/icon?job=SoInteractive/keepalived/master)](https://ci.devops.sosoftware.pl/blue/organizations/jenkins/SoInteractive%2Fkeepalived/activity) [![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT) [![Ansible Role](https://img.shields.io/ansible/role/18267.svg)](https://galaxy.ansible.com/SoInteractive/keepalived/) [![Twitter URL](https://img.shields.io/twitter/follow/sointeractive.svg?style=social&label=Follow%20%40SoInteractive)](https://twitter.com/sointeractive)

Role will install and configure keepalived daemon used for automated Virtual IP address supervision

Example usage
-------------

Use it in a playbook as follows:
```yaml
- hosts: all
  become: true
  roles:
    - SoInteractive.keepalived
```

Have a look at the [defaults/main.yml](defaults/main.yml) for role variables
that can be overridden.
