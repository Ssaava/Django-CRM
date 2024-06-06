# Welcome to Microscope Malaria Diagnosis

## Installation guide

install the [tailwindcss standalone cli tool for your os](https://github.com/tailwindlabs/tailwindcss/releases/latest)
rename the file to anyname if you wish to. eg I named mine to tailwindcss.exe to run the commands easily

## The commands to work with tailwindcss

- To initialize tailwindcss in the project with the tailwind.config.js file

```bash
    ./tailwindcss.exe init
```

- watch the tailwindcss bade file which includes tailwindcss utilities for my case I named it input.css and put it under static folder

```bash
    ./tailwindcss.exe -i ./static/input.css -o static/output.css --watch
```

# Compile and minify your CSS for production

```bash
./tailwindcss.exe -i ./static/input.css -o static/output.css --minify
```

## Read more about configuring tailwindcss [here](https://tailwindcss.com/blog/standalone-cli)

## Load the static files by running the following in the terminal within the same folder

```bash
python manage.py collectstatic
```

- this will load all the necessary static files serving the project and add a new folder to the root directory called staticFiles