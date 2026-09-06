# comPLEX
Script to check if a text or a .txt file is written by human or ChatGPT

## features:
- lightweight and faster than some heavy models
- Running on a ML model to detect
- Trained with [A hugging face](https://huggingface.co/datasets/Hello-SimpleAI/HC3/viewer/all/train) dataset
- Works for Human vs ChatGPT

## setup:
- First, make sure you have python, if you haven't installed it yet, install it from [here](https://www.python.org/downloads/)
- Download the .zip format of the project from here and extract it or clone this project with `git clone https://github.com/arshia2012/comPLEX` (To clone, you need [git](https://git-scm.com/install/)
- Go to directory where the project is
- Install the libraries with `pip install -r requirements.txt`
- run the model.py once first `python3 model.py`
- Once finished you are ready to run `python3 main.py` and use the app

## How to use:
- To scan a text in the terminal use `-t` flag, e.g: `python3 main.py -t "something"`
- To scan a file in the terminal use `-f` flag, e.g `python3 main.py -f something.txt`
- If you want to see the full error texts, use `-d` flag 

## Example of result:
<img width="1123" height="421" alt="Screenshot 2026-09-06 095123" src="https://github.com/user-attachments/assets/a83a7425-1298-41b6-800d-ce361d74e975" />
