# this creates a file in /tmp

filepath { '/tmp/school':
  content =>'I love Puppet',
  permision    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
