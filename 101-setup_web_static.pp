# Prepare web servers 

package { 'nginx':
    ensure => installed,
}

file { '/data/web_static/releases/test/':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    recurse => true,
}

file { '/data/web_static/shared/':
    ensure  => directory,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    recurse => true,
}

file { '/data/web_static/releases/test/index.html':
    ensure  => present,
    owner   => 'ubuntu',
    group   => 'ubuntu',
    content => 'Welcome to my configuration test page',
    recurse => true,
}

file { '/data/web_static/current':
    ensure => 'link',
    owner  => 'ubuntu',
    group  => 'ubuntu',
    target => '/data/web_static/releases/test'
}

exec { 'haprox.cfg':
    command  => 'sudo sed -i "60 c\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/curr    ent/;\n\t}"
	    /etc/nginx/sites-available/default',
    provider => shell,
}

service { 'nginx':
    ensure => running,
    enable => true,
}
