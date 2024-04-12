# increase nginx limit
exec { 'ncrease-limit':
  command => 'sed -i "s/15/8192/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
