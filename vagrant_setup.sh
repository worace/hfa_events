set -o nounset -o errexit -o pipefail -o errtrace

# Make it so that `vagrant ssh` goes directly to the correct dir
echo "cd /vagrant" >> /home/vagrant/.bashrc

# Configuring SSH for faster login
if ! grep "UseDNS no" /etc/ssh/sshd_config >/dev/null; then
  echo "UseDNS no" | sudo tee -a /etc/ssh/sshd_config >/dev/null
  sudo service ssh restart
fi

export DEBIAN_FRONTEND=noninteractive

echo "Adding apt repositories and updating..."
sudo apt-get update
sudo apt-get install -y python-software-properties software-properties-common apt-transport-https
sudo apt-get update
sudo apt-get install -y postgresql-9.1 postgresql-client-9.1 postgresql-contrib-9.1
sudo -u postgres createuser vagrant --superuser
sudo -u postgres createdb vagrant
cd /vagrant

# Install Backend app dependencies
sudo apt-get install -y python-virtualenv python-dev python-psycopg2 libpq-dev build-essential

virtualenv env
set +o nounset
source env/bin/activate
set -o nounset

pip install -r backend/requirements.txt
pip install honcho # to run the procfile

cd backend
# Setup backend app db
PG_DUMP_FILE="/vagrant/data.pgdump" python app/db_import.py

# Install frontend app dependencies
sudo apt-get install -y curl
# Add PPA for latest version of node
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install -g webpack webpack-dev-server
