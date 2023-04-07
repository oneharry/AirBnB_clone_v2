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

exec { 'symbolic link':
    command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
    provider => shell,
}

exec { 'haprox.cfg':
    command  => 'sudo sed -i "60 c\\n\tlocation /hbnb_static" 
    "{\n\t\talias /data/web_static/curr    ent/;\n\t}" /etc/nginx/sites-available/default',
    provider => shell,
}

service { 'nginx':
    ensure => running,
    enable => true,
}
