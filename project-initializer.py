import os
import json

class ProjectInitializer:
    def __init__(self, project_types, css_frameworks):
        self.project_types = project_types
        self.css_frameworks = css_frameworks

    def display_options(self, options):
        for idx, option in enumerate(options, start=1):
            print(f"{idx}) {option['name']}")

    def choose_option(self, options):
        choice_str="Please choose an option"
        choice = input(choice_str+" : ")
        while not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
            print("Invalid option. Please choose a valid option.")
            choice = input(choice_str+" : ")
        return options[int(choice) - 1]

    def validate_project_name(self, project_name):
        if not project_name:
            return False
        return True

    def init_project(self):
        print("Initializing a project")
        print("Choose the type of project:")
        self.display_options(self.project_types)
        project_type = self.choose_option(self.project_types)

        print("Which CSS tool do you want to use?")
        self.display_options(self.css_frameworks)
        css_framework = self.choose_option(self.css_frameworks)


        enter_project_name_str = "Please enter the project name"
        project_name = input(enter_project_name_str+" : ")
        while not self.validate_project_name(project_name):
            print("Invalid project name. Please enter a valid project name.")
            project_name = input(enter_project_name_str+" : ")

        command = project_type['command'].format(project_name=project_name)
        if css_framework:
            command += f" {css_framework['command']}"

        try:
            os.system(command)
            print("The project has been successfully initialized!")
        except Exception as e:
            print("An error occurred while initializing the project:")
            print(str(e))

def save_config(project_types, css_frameworks):
    config = {
        "project_types": project_types,
        "css_frameworks": css_frameworks
    }
    with open("config.json", "w") as file:
        json.dump(config, file)

def load_config():
    with open("config.json", "r") as file:
        config = json.load(file)
    return config.get("project_types"), config.get("css_frameworks")


def _main():
    if os.path.exists("config.json"):
        project_types, css_frameworks = load_config()
    else:
        # Options de projet par défaut
        project_types = [
            {
                "name": "React",
                "command": "npx create-react-app {project_name}",
                "css_frameworks": True
            },
            {
                "name": "React avec TypeScript (TS)",
                "command": "npx create-react-app {project_name} --template typescript",
                "css_frameworks": True
            },
            {
            "name": "Symfony api",
            "command": "composer create-project symfony/website-skeleton {project_name}",
            "css_frameworks": False
        },
        {
            "name": "Symfony webapp",
            "command": "composer create-project symfony/website-skeleton {project_name} --webapp",
            "css_frameworks": False
        },
            {
                "name": "Laravel",
                "command": "composer create-project --prefer-dist laravel/laravel {project_name}",
                "css_frameworks": False
            },
            {
                "name": "Django",
                "command": "django-admin startproject {project_name}",
                "css_frameworks": False
            },
            {
                "name": "Express.js",
                "command": "npx express-generator --no-view {project_name}",
                "css_frameworks": False
            }
        ]

        css_frameworks = [
            {
                "name": "Bootstrap",
                "command": "--use-bootstrap"
            },
            {
                "name": "Tailwind CSS",
                "command": "--use-tailwind"
            },
            {
                "name": "Aucun (CSS de base)",
                "command": ""
            }
            # Ajouter de nouveaux frameworks CSS ici
        ]

        # Enregistrer les options par défaut dans le fichier de configuration
        save_config(project_types, css_frameworks)

    initializer = ProjectInitializer(project_types, css_frameworks)
    initializer.init_project()
    
    
if __name__ == "__main__":
   _main()