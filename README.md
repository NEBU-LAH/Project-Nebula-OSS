# Project Nebula OSS (Open-Source Software)

## Welcome to the Project Nebula’s Playbooks Repository

This project is an open-source initiative by **THENEBU.COM** aimed at building a comprehensive collection of DevOps playbooks. We are open to contributions from the NEBU community and beyond, as we strive to automate and streamline infrastructure management and deployment. For the phase 1 of the project, the main engine will be RED HAT’s Ansible.

If you are not familiar with Ansible’s playbook, you may find further reading at https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_intro.html

In the heart of nebulas, dust and energy come together, sparking the creation of new stars. Our project, Nebula, is much like these cosmic nurseries—it's built from the time, knowledge, and passion of those who contribute. Every piece of code, every idea, every bit of effort you share helps us shape something brighter. Let's come together, ignite our creativity, and build something truly stellar.

## Learn and give back to the Community

As you contribute to this project either by using or building playbooks, you would be playing a role in improving the cloud configuration and DevOps experience for all.

We welcome and encourage contributions from the community to enhance this open-source software project! To ensure proper credit and alignment with the MIT License, please follow the guidelines below when contributing.
Please leave your credits on the playbooks you create using the following format

---

- Playbook Name: [filename]
- Author(s): [Your Name/Nickname] <[Your Email]>
- Creation Date: [YYYY-MM-DD]
- Description: [Short description of the contribution]
- Latest Version: vX.X
- Update date: [YYYY-MM-DD]
- Contributors: [List of additional contributors, if any]
- This code is licensed under the MIT License.
- Copyright (c) [Year] [Project Owner(s) or Organization].

---

### Get Started with the Project

We are excited to have you onboard as a contributor! Follow the steps below to get started:

1. **Fork the Repository**  
   Start by forking this repository to your GitHub account. This allows you to make changes without affecting the main repository.

2. **Clone the Repository**
   Clone the forked repository to your local machine using the appropriate command.
   ```
   git clone https://github.com/<Your-User-Name>/ansible-marketplace.git
   ```
3. **Set Up Your Environment**
   Make sure you have Ansible installed on your local machine. You can install it using the relevant package manager. Or for other operating systems, follow the Ansible installation

   ```
   sudo apt-get install ansible
   ```

4. **Install Required Roles**  
   Navigate to the project directory and install the required roles by running the necessary command (if any)

   ```
   ansible-galaxy install -r requirements.yml
   ```

5. **Explore Existing Playbooks**  
   Explore the `playbooks/` directory to see the existing playbooks. Each playbook is designed to install and configure a specific DevOps tool across multiple operating systems.

6. **Contribute New Playbooks**  
   We welcome contributions for new DevOps tools. Please follow the existing structure for adding new playbooks:

   - Create a new role under `roles/`
   - Add tasks, handlers, and any required templates
   - Create or update a playbook under `playbooks/`

7. **Test Your Contributions**  
   Ensure your playbooks work as expected by testing them using GitHub Actions. Refer to the `.github/workflows/` directory for the CI/CD setup.

8. **Submit a Pull Request**  
   Once you’re satisfied with your contribution, submit a pull request to the main repository. Our team will review your changes and merge them into the project.

#### To help generate files for a new feature or tool, use:

`python3 helper.py <tool-name>
`

#### To install using Docker:

##### run this command to build:

`docker build -t ansible-ubuntu-bash`

##### and then run:

`docker run --rm -it ansible-ubuntu-bash`

### Our mission: Top 50 DevOps Tools to Add

Together, we are building a comprehensive collection of playbooks for the top 50 DevOps tools that are widely used in the industry. Here are the tools we are focusing on:

The ones struck-through are already available, feel free to review it and share feedback.

1. **Grafana** - Monitoring and analytics platform.
2. **Prometheus** - Monitoring system and time-series database.
3. **SonarQube** - Continuous inspection of code quality.
4. **Netdata** - Real-time performance monitoring.
5. **Jenkins** - Automation server for continuous integration and delivery.
6. **Docker** - Containerization platform for developing and running applications.
7. **Kubernetes** - Container orchestration platform.
8. **Terraform** - Infrastructure as Code (IaC) tool for building, changing, and versioning infrastructure.
9. **Ansible** - Configuration management, application deployment, and task automation tool.
10. **Nagios** - Monitoring system for networks, servers, and applications.
11. **Elasticsearch** - Distributed search and analytics engine.
12. **Logstash** - Server-side data processing pipeline that ingests data from multiple sources.
13. **Kibana** - Data visualization and exploration tool.
14. **Apache Kafka** - Distributed event streaming platform.
15. **Vault** - Tool for securely accessing secrets.
16. **Consul** - Service networking solution for service discovery and configuration.
17. **Nginx** - High-performance HTTP server, reverse proxy, and load balancer.
18. **HAProxy** - High-availability load balancer and proxy server.
19. **Istio** - Service mesh that provides a way to control how microservices share data.
20. **CircleCI** - Continuous integration and delivery platform.
21. **GitLab CI/CD** - Integrated continuous integration and delivery tool.
22. **Travis CI** - Hosted continuous integration service used to build and test software projects.
23. **TeamCity** - Continuous integration and build management system.
24. **Packer** - Tool for creating identical machine images for multiple platforms.
25. **Chef** - Configuration management tool for automating the deployment of applications.
26. **Puppet** - Configuration management tool to automate the provisioning and management of infrastructure.
27. **Vagrant** - Tool for building and managing virtualized development environments.
28. **Spinnaker** - Continuous delivery platform for releasing software changes.
29. **Argo CD** - Declarative continuous delivery tool for Kubernetes.
30. **Drone** - Container-native, continuous delivery platform.
31. **New Relic** - Application performance monitoring and management.
32. **Datadog** - Monitoring and analytics platform for large-scale applications.
33. **Splunk** - Platform for searching, monitoring, and analyzing machine-generated data.
34. **Sentry** - Application monitoring platform that helps developers monitor and fix crashes in real-time.
35. **PagerDuty** - Incident management and on-call scheduling platform.
36. **Opsgenie** - Incident management tool that enables DevOps teams to plan for service disruptions.
37. **Fluentd** - Open-source data collector for a unified logging layer.
38. **Graylog** - Log management tool that makes it easy to capture, store, and analyze machine data.
39. **LogDNA** - Centralized log management solution.
40. **Promtail** - An agent which ships the contents of local logs to a Loki instance.
41. **Loki** - Log aggregation system designed for use with Grafana.
42. **Falco** - Kubernetes runtime security monitoring tool.
43. **Sysdig** - Monitoring, security, and troubleshooting for containers and microservices.
44. **Artifactory** - Universal repository manager supporting all major packaging formats.
45. **Nexus Repository** - Artifact repository manager with support for all types of components.
46. **MinIO** - High-performance object storage system.
47. **Harbor** - Open-source container image registry.
48. **Velero** - Disaster recovery tool for Kubernetes.
49. **Tekton** - Kubernetes-native continuous integration and delivery pipelines.
50. **Thanos** - Highly available Prometheus setup with long-term storage capabilities.


### Testing
The follwing testing official amazon images were used:
-  ami-0e86e20dae9224db8"        #24
-  iam: "ami-0a0e5d9c7acc336f1"  #22.04
-  iam: "ami-032346ab877c418af"  #20.04
-  iam: "ami-064519b8c76274859"  # Debian 12
-  iam: "ami-0182f373e66f89c85" #amazon 2023
-  iam: "ami-0a5c3558529277641" #amazon linux 2

| Item                          | Amazon Linux 2 | Amazon Linux 2023 | Ubuntu 24 | Ubuntu 22 | Ubuntu 20 | CentOS | Fedora | Debian 12 |
|-------------------------------|-----------------|--------------------|-----------|-----------|-----------|--------|--------|-----------|
| Docker Installation           | ✅              | ✅                 | ✅        | ✅        |           |        |        |✅         |
| Grafana                       |                 |                    |           |           |           |        |        |           |
| Prometheus                    |                 |                    |           |           |           |        |        |           |
| SonarQube                     |                 |                    |           |           |           |        |        |           |
| Netdata                       |                 |                    |           |           |           |        |        |           |
| Jenkins                       |                 |                    |           |           |           |        |        |           |
| Docker                        |                 |                    |           |           |           |        |        |           |
| Kubernetes                    |                 |                    |           |           |           |        |        |           |
| Terraform                     |                 |                    |           |           |           |        |        |           |
| Ansible                       |                 |                    |           |           |           |        |        |           |
| Nagios                        |                 |                    |           |           |           |        |        |           |
| Elasticsearch                 |                 |                    |           |           |           |        |        |           |
| Logstash                      |                 |                    |           |           |           |        |        |           |
| Kibana                        |                 |                    |           |           |           |        |        |           |
| Apache Kafka                  |                 |                    |           |           |           |        |        |           |
| Vault                         |                 |                    |           |           |           |        |        |           |
| Consul                        |                 |                    |           |           |           |        |        |           |
| Nginx                         |                 |                    |           |           |           |        |        |           |
| HAProxy                       |                 |                    |           |           |           |        |        |           |
| Istio                         |                 |                    |           |           |           |        |        |           |
| CircleCI                      |                 |                    |           |           |           |        |        |           |
| GitLab CI/CD                  |                 |                    |           |           |           |        |        |           |
| Travis CI                     |                 |                    |           |           |           |        |        |           |
| TeamCity                      |                 |                    |           |           |           |        |        |           |
| Packer                        |                 |                    |           |           |           |        |        |           |
| Chef                          |                 |                    |           |           |           |        |        |           |
| Puppet                        |                 |                    |           |           |           |        |        |           |
| Vagrant                       |                 |                    |           |           |           |        |        |           |
| Spinnaker                     |                 |                    |           |           |           |        |        |           |
| Argo CD                       |                 |                    |           |           |           |        |        |           |
| Drone                         |                 |                    |           |           |           |        |        |           |
| New Relic                     |                 |                    |           |           |           |        |        |           |
| Datadog                       |                 |                    |           |           |           |        |        |           |
| Splunk                        |                 |                    |           |           |           |        |        |           |
| Sentry                        |                 |                    |           |           |           |        |        |           |
| PagerDuty                     |                 |                    |           |           |           |        |        |           |
| Opsgenie                      |                 |                    |           |           |           |        |        |           |
| Fluentd                       |                 |                    |           |           |           |        |        |           |
| Graylog                       |                 |                    |           |           |           |        |        |           |
| LogDNA                        |                 |                    |           |           |           |        |        |           |
| Promtail                      |                 |                    |           |           |           |        |        |           |
| Loki                          |                 |                    |           |           |           |        |        |           |
| Falco                         |                 |                    |           |           |           |        |        |           |
| Sysdig                        |                 |                    |           |           |           |        |        |           |
| Artifactory                   |                 |                    |           |           |           |        |        |           |
| Nexus Repository              |                 |                    |           |           |           |        |        |           |
| MinIO                         |                 |                    |           |           |           |        |        |           |
| Harbor                        |                 |                    |           |           |           |        |        |           |
| Velero                        |                 |                    |           |           |           |        |        |           |
| Tekton                        |                 |                    |           |           |           |        |        |           |
| Thanos                        |                 |                    |           |           |           |        |        |           |





### House rules

- **Join the Discussion:** Use the Issues tab to discuss ideas, report bugs, or ask for help.
- **Follow the Contribution Guidelines:** Before contributing, please read our README.md file.
- **Respect the Code of Conduct:** We expect all contributors to adhere to our Code of Conduct and respect all members.

### Join Our Community

- **[Join our Discord](https://discord.gg/Ddp63ajj8Z)**: Connect with other community members, discuss ideas, and collaborate on projects.

- **[Follow us on LinkedIn](https://www.linkedin.com/company/thenebu)**: Stay updated with the latest news, events, and job opportunities.

### License

This project is licensed under the MIT License.

MIT License Copyright (c) 2024 NEBU

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

Thank you for being a part of this journey. Together, we can build an exceptional repository of DevOps playbooks that benefit the entire community.

**Happy Coding!**

**The Project Nebula team (recruiting volunteers)**
