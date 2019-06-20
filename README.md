This is example of [cookiecutter](https://github.com/audreyr/cookiecutter) automation test template to my talk http://tiny.cc/g7yh8y 
___
### Configuration
* `{{cookiecutter.project_name}}` - should be the same as git repository name
* `{{cookiecutter.project_slug}}` - default package for all non testing stuff
### Usage
1. Create new repository on your gitlab (for example: `dummy-example-tests`)
2. Configure `$BUILD_PATH` variable in repository configuration
3. Clone repository
    ```bash
    > git clone git@{YOUR-GITLAB}:{YOUR-NICKNAME}/dummy-example-tests.git
    ```
4. Execute this command in parent directory of your project
    ``` bash
    > cookiecutter -fc 1.0 git@github.com:v1-wizard/automation-test-template.git
    ```
5. Fill all fields
6. Go to your project and write code
    ``` bash
    > cd dummy-example-tests
    ```
7. Push your changes to gitlab  
6. Enjoy
 