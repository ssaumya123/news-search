# STA Deployment Using Ansible
The following steps can be followed in order to install and setup ansible for STA Deployment process.

## Pre-requisites

1. Supported OS is Ubuntu 16.04 LTS for control machine (that triggers installation and configuration of STA).
2. Setup ssh connection from control machine to installer and rack clients, for reference, please follow the steps mentioned in the link as:
   https://linuxize.com/post/how-to-setup-passwordless-ssh-login/
3. Please use root user for any command installation or configuration on control machine.

## Steps to be executed only on clients.

1. Please do the cleanup of previously existing mount points (created using Rack Public IP addresses), by executing following command.
   ```
   umount -f /UDA_basic/<Public IP address of the rack>
   ```

2. Remove the existing local UDA_basic directories, by executing the following command.
   ```
   rm -rf /UDA_basic*
   ```

## How to configure Ansible and Deploy STA:

1. Install Ansible on a control machine (that triggers the STA Deployment on installer (orchestrator) and rack clients.
   ```
   apt-get install ansible
   ```

2. Edit the `/etc/ansible/hosts` file, with the following content.
   ```
   [OrchestratorAndClientsNodes:children]
   OrchestratorNodes
   ClientsNodes
   [OrchestratorNodes]
   10.206.124.151 ansible_user=root1
   [ClientsNodes]
   10.206.121.87 ansible_user=root1
   Do not change the headers, and only specify the IP addresses of the nodes where STA orchestrator components needs to be installed under orchestrator-nodes header and respectively add the client IP addresses for STA clients components under clients-nodes headers.
   (For further reference, please refer to hosts file present in the STA_Deployment_Ansible/ansible_config/ directory.)
   ```

3. To disable extra warnings (that creates ambiguous information, please set the following values to False in `/etc/ansible/ansible.cfg` file:
   ```
   system_warnings = False
   deprecation_warnings = False
   command_warnings = False
   And please remove # before the above mentioned keys, if exists.
   (For further reference, please refer to ansible.cfg file present in the STA_Deployment_Ansible/ansible_config/ directory.)
   ```

4. To test the connectivity of control machine to all the orchestrators and clients nodes, please execute the following command:
   ```
   ansible 'OrchestratorAndClientsNodes' -m ping
   You will notice that all the connected nodes comes in green color with success as response.
   ```
   
5. For better installation, we need to have password less connection from control machines to all the nodes, please execute the following command.
   ```
   ansible-playbook set_sudoer.yml -b -K
   That will prompt for one time password for the root user.
   ```

6. Now we need to execute the following command to start the STA deployment over installer and clients nodes.
   ```
   ansible-playbook master.yml -e "gitlabuser=<gitlab-user>" -e "gitlabpassword=<gitlab-password>"
   ``` 
   
## Please Note: All the mentioned set_sudoer.yml and master.yml playbooks are existing in STA_Deployment_Ansible directory.
