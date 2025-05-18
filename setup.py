from setuptools import setup, find_packages

setup(
    name="expense-tracker",
    version="0.1.0", 
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "kivy>=2.3.1",
        "matplotlib>=3.10.3",
        "python-dateutil>=2.9.0",
        "Kivy-Garden>=0.1.5",
        "kivy_garden.matplotlib>=0.1.1"
    ],
    package_data={
        "expense_tracker": [
            "main_screen/*.kv",
            "setting_screen/*.kv",
            "upload_screen/*.kv",
            "new_category_screen/*.kv",
            "detail_screen/*.kv",
            "plot_screen/*.kv"
        ]
    }
)