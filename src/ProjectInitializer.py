import re
import os


class ProjectInitializer:
    def __init__(self, project_types: list[dict], css_frameworks: list[dict]):
        self.project_types: list[dict] = project_types
        self.css_frameworks: list[dict] = css_frameworks

    def display_options(self, options: list[dict]) -> None:
        for idx, option in enumerate(options, start=1):
            print(f"{idx}) {option['name']}")

    def choose_option(self, options: list[dict]) -> dict:
        choice_str = "Please choose an option"
        choice = input(choice_str + " : ")
        while not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
            print("Invalid option. Please choose a valid option.")
            choice = input(choice_str + " : ")
        return options[int(choice) - 1]

    def validate_project_name(self, project_name: None | str)->bool:
        if not project_name:
            return False
        if re.search(r'[<>:"/\\|?*\x00-\x1F]', project_name):
            return False
        return True

    def init_project(self):
        print("Initializing a project")
        print("Choose the type of project:")
        self.display_options(self.project_types)
        project_type:dict = self.choose_option(self.project_types)

        print("Which CSS tool do you want to use?")
        self.display_options(self.css_frameworks)
        css_framework:dict = self.choose_option(self.css_frameworks)

        enter_project_name:str = "Please enter the project name"
        project_name: str = input(enter_project_name + " : ")
        while not self.validate_project_name(project_name):
            print("Invalid project name. Please enter a valid project name.")
            project_name = input(enter_project_name+ " : ")

        command = project_type['command'].format(project_name=project_name)
        if css_framework:
            command += f" {css_framework['command']}"

        try:
            os.system(command)
            print("The project has been successfully initialized!")
        except Exception as e:
            print("An error occurred while initializing the project:")
            print(str(e))
