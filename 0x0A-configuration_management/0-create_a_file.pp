# this creates a file in /tmp

file { '/tmp/school':
  thecontent =>'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
} 
