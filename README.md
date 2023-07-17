
# Web Scraping Project: ScentsNStories
This project is focused on scraping data from the ScentsNStories website. The goal is to fetch product information, including product ID, name, description, price, and gender type. The fetched data will be stored in a DataFrame, exported to a CSV file, and finally stored in a MySQL database.






## Prerequisites
- Python 3.x
- Virtual environment (venv) - included in the project repository
- MySQL database

## Deployment

To deploy this project run the following cmd command inside the project folder

```cmd
  .\env\Scripts\activate
```

After running the above command run
```
python web.py
```



## Database configuration
Inside the databse.py change the following according to your system
- db_username
- db_password
- db_host
- db_port
- db_name
## Project Structure
- **web.py** (main file) contains all the scrapping code
- **database.py** connects with mysql and store the dataframe into db as a table
## Contributing
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request
## Installation

By including the venv folder in the repository, the required Python modules are already available. However, if you prefer to create your own virtual environment, you can use the requirements.txt file included in the project to install the necessary modules. Activate the virtual environment and run the following command:
```bash
  pip install -r requirements.txt
```
    
## Authors

- [@Muhammad Osama](https://www.github.com/OcamaAslam)
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ocama-mohamed)

