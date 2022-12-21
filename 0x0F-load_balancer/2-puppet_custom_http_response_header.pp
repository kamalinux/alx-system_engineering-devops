# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

exec { 'add_header':
  provider => shell,
  command  => 'sudo sed -i "27i \\\n\tadd_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf',
  before   => Exec['restart Nginx'],
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
