# install puppet-lint -v 2.5.0

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

