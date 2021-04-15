sudo apt update && sudo apt upgrade -y
sudo apt install python3 

# Optional
sudo apt install python3-pip
pip3 install virtualenv
python3 -m virtualenv env
source env/bin/activate

pip3 install -r requirements.txt 

# Notes 
pip3 freeze > requirements.txt