import json
import os
from ProjectInitializer import ProjectInitializer
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