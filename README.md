# LinkedIn Scrapy tool with Airflow
## A scraping tool aim at automatically extracting data from LinkedIn using Scrapy framework, Airflow for orchestrating the process and also Docker for containerizing the workspace.

### Overview
This project is a comprehensive web scraping tool designed to extract information from websites automatically and efficiently. It leverages Scrapy for the web scraping tasks, Airflow for scheduling and managing workflows, and Docker for creating a consistent and isolated environment for the tool to run in. This setup allows for scalable, reliable, and automated data extraction processes.

### Note
The element in the CSS selector might be outdated at the time you use this framework since web pages periodically change their elements for privacy purposes. Please redirect to the web link you want to scrape to re-inspect the element.

### Features
- __Scrapy Integration:__ Utilize Scrapy's powerful scraping capabilities for efficient data extraction from various websites.
- **Airflow Scheduling:** Schedule and monitor scraping jobs with Apache Airflow's robust workflow management.
- **Docker Containerization:** Ensure consistent execution environments and simplify deployment processes using Docker.
- **Flexible Configuration:** Easily configure scraping targets, scheduling intervals, and more through simple configuration files.
- **Automated Data Processing:** Automatically process and store extracted data in your preferred format and storage solution.

### Prerequisites
- **Docker Installation**: https://docs.docker.com/get-docker/

### Installation and setup
1. Clone the repository
   
   `git clone https://github.com/embiekhochiu/scrapy_linkedin.git`
   
   `cd scrapy_linkedin`
   
3. Build the docker container
   
   `docker-compose build`

5. Start the service
   
   `docker-compose up`

### Customization Usage
**Configure scraping job**
- Navigate to the scrapy_project directory.
- Edit the Scrapy spiders or create new ones to target the websites you wish to scrape.
- Configure your scraping targets and output preferences in the respective Scrapy settings and pipelines.
- Configure the middlewares to randomly change your proxies for not being banned by the web robot.

**Scheduling jobs with Airflow**
- Navigate to the airflow directory.
- Create new DAGs or edit existing ones to define your scraping workflows and schedules.


