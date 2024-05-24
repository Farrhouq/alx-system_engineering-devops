# This puppet manifest is used to configure an ubuntu server

package { 'nginx':
  ensure => installed,
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
}

file { '/var/www/html/custom_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page",
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm;
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    error_page 404 /custom_404.html;
    location 404 {
        root /var/www/html;
        internal;
    }
}",
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
