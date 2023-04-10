# Prepare web servers 

$default = "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By ${hostname};
	root /var/www/html;
	index index.html index.htm;

	location /hbnb_static {
		alias /data/web_static/current;
		index index.html index.htm;
	}

	location /redirect_me {
		return 301 http://www.google.com;
	}

	error_page 404 /404.html;
	location /404 {
		root /var/www/html;
		internal;
	}
}"

exec { 'sudo apt-get update':
        provider => 'shell',
}

package { 'nginx':
    ensure   => 'installed',
    provider => 'apt',
}



exec { ' sudo mkdir -p /data/web_static/releases/test/':
    provider => 'shell',
}

exec { 'sudo mkdir -p /data/web_static/shared/':
    provider => 'shell',
}

file { '/data/web_static/releases/test/index.html':
    ensure  => present,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    content => 'Welcome to my configuration test page',
}

file { '/data/web_static/current':
    ensure => 'link',
    owner  => 'ubuntu',
    group  => 'ubuntu',
    target => '/data/web_static/releases/test',
}
file { '/index.html':
    ensure  => 'present',
    content => 'Hello World!',
}

exec { 'sudo cp /index.html /var/www/html/index.html':
    provider => 'shell',
}

file { '/404.html':
    ensure  => 'present',
    content => "Ceci n'est pas une page",
}

exec { 'sudo cp /404.html /var/www/html/404.html':
    provider => 'shell',
}

file { '/default':
    ensure  => 'present',
    content => $default,
}

exec { 'sudo cp /default /etc/nginx/sites-available/default':
    provider => 'shell',
}

exec { 'sudo rm /404.html /default /index.html':
    provider => 'shell',
}

service { 'nginx':
    ensure => 'running',
    enable => 'true',
}
