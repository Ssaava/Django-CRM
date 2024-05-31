# Welcome to Microscope Malaria Diagnosis

## Installation guide

install the [tailwindcss standalone cli tool for your os](https://github.com/tailwindlabs/tailwindcss/releases/latest)
rename the file to anyname if you wish to. eg I named mine to tailwindcss.exe to run the commands easily

## The commands to work with tailwindcss

- To initialize tailwindcss in the project with the tailwind.config.js file

```bash
    ./tailwindcss.exe init
```

- watch the tailwindcss bade file which includes tailwindcss utilities for my case I named it input.cssand put it under static folder

```bash
    ./tailwindcss.exe -i ./static/input.css -o static/output.css --watch
```

# Compile and minify your CSS for production

```bash
./tailwindcss.exe -i ./static/input.css -o static/output.css --minify
```
