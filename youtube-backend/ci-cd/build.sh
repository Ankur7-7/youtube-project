#Build commands for merge glue job
set -ue

environment=$1 # eg: staging/production

# Packing with dependencies
yum install gcc-c++ python3-devel unixODBC-devel -y
ln -s /usr/libexec/gcc/x86_64-amazon-linux/7.2.1/cc1plus /usr/bin/
python3.9 -m pip install --upgrade pip

echo "========================[ AWS Key Configure ]============="
export AWS_ACCESS_KEY_ID=AKIAYDDAWJVWMLDBXPEJ
export AWS_SECRET_ACCESS_KEY=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

echo "========================[ Create Virtual Env and Activate ]============="
set +u
python3.9 -m venv alpha_app_env
source $CODEBUILD_SRC_DIR/alpha_app_env/bin/activate
set -u

#echo "========================[ Installing Packages ]========================="
pip install zappa
pip install -r $CODEBUILD_SRC_DIR/requirements.txt

echo "========================[ Deploy/Update APIs ]========================="
zappa update $environment

echo "Build.sh completed"