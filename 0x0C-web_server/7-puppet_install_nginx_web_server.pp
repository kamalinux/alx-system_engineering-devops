# Configuring your server with Puppet!

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "46i \\\n\tlocation /redirect_me {\n\t\t return 301 https://github.com/kamalinux;\n\t}\n" /etc/nginx/sites-available/default ; sudo service nginx start',
}
