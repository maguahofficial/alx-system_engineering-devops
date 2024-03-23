# this creates a file in /tmp

filepath { '/tmp/school':
  contentinside =>'I love Puppet',
  permision    => '0744',
  theowner   => 'www-data',
  gtheroup   => 'www-data',
}
